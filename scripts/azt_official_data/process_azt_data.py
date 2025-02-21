#!/usr/bin/env python3

import json
import logging
import math
import os
import argparse
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import gpxpy
import gpxpy.gpx
import requests
import yaml

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
AZGEO_URL = "https://services3.arcgis.com/IKBBLZOXy58PXgpl/arcgis/rest/services/Arizona_National_Scenic_Trail_Feature_Layers_view/FeatureServer/3/query"
QUERY_PARAMS = {
    "outFields": "*",
    "where": "1=1",
    "f": "geojson"
}
DATA_DIR = Path('../../data')
CACHE_DIR = DATA_DIR / 'cache'
CACHE_FILE = CACHE_DIR / 'azt_polyline.geojson'

@dataclass
class PassageStats:
    """Statistics for a trail passage."""
    passage_num: int
    name: str
    official_miles: float
    calculated_miles: float
    point_count: int
    max_gap_miles: float
    min_elevation_ft: float
    max_elevation_ft: float
    start_lat: float
    start_lon: float
    end_lat: float
    end_lon: float

def download_trail_data(force_refresh: bool = False) -> dict:
    """Download or load trail data, with option to force refresh."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    
    if CACHE_FILE.exists() and not force_refresh:
        logger.info("Loading cached trail data...")
        with open(CACHE_FILE) as f:
            data = json.load(f)
            logger.info(f"Loaded {len(data['features'])} features from cache")
            return data
    
    logger.info("Downloading fresh trail data from AZGEO...")
    response = requests.get(AZGEO_URL, params=QUERY_PARAMS)
    response.raise_for_status()
    data = response.json()
    
    # Save to cache
    with open(CACHE_FILE, 'w') as f:
        json.dump(data, f, indent=2)
    logger.info(f"Downloaded and cached {len(data['features'])} features")
    
    return data

def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculate distance between two points in miles."""
    R = 3959.87433  # Earth's radius in miles

    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    return R * c

def process_coordinates(coordinates: List[List[float]]) -> Tuple[float, float, List[Tuple[float, float, float]]]:
    """Process coordinates to calculate distance and extract points.
    
    Args:
        coordinates: List of [longitude, latitude] pairs from ArcGIS response
        
    Returns:
        Tuple of (total_distance, max_gap, processed_points)
        where processed_points is a list of (latitude, longitude, elevation) tuples
    """
    total_distance = 0
    max_gap = 0
    processed_points = []
    
    for i in range(len(coordinates)):
        # ArcGIS provides coordinates as [longitude, latitude]
        # Some points may have additional data we need to ignore
        point = coordinates[i]
        if not point or len(point) < 2:
            logging.warning(f"Invalid point at index {i}: {point}")
            continue
            
        lon = point[0]  # Longitude is first in ArcGIS format
        lat = point[1]  # Latitude is second
        elevation_ft = 0  # Elevation data not provided in AZGEO
        
        if i > 0:
            prev_point = coordinates[i-1]
            prev_lon = prev_point[0]
            prev_lat = prev_point[1]
            gap = haversine_distance(prev_lat, prev_lon, lat, lon)
            total_distance += gap
            max_gap = max(max_gap, gap)
            
        processed_points.append((lat, lon, elevation_ft))
    
    if not processed_points:
        raise ValueError("No valid coordinates found in input data")
        
    return total_distance, max_gap, processed_points

def create_gpx(passage_num: int, name: str, points: List[Tuple[float, float, float]]) -> str:
    """Create GPX file for a passage."""
    gpx = gpxpy.gpx.GPX()
    gpx_track = gpxpy.gpx.GPXTrack()
    gpx.tracks.append(gpx_track)
    gpx_segment = gpxpy.gpx.GPXTrackSegment()
    gpx_track.segments.append(gpx_segment)

    for lat, lon, elevation in points:
        gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(lat, lon, elevation=elevation))

    return gpx.to_xml()

def merge_multilinestring(coordinates: List[List[List[float]]]) -> List[List[float]]:
    """Merge MultiLineString segments into a single LineString.
    
    Args:
        coordinates: List of line segments, each containing [longitude, latitude] pairs
        
    Returns:
        Single list of [longitude, latitude] pairs
    """
    if not coordinates:
        return []
        
    # Start with the first segment
    merged = coordinates[0]
    
    # For each additional segment
    for segment in coordinates[1:]:
        if not segment:
            continue
            
        # Calculate distances between end of current and start of next
        end_point = merged[-1]
        start_point = segment[0]
        gap = haversine_distance(
            end_point[1], end_point[0],  # lat, lon of end point
            start_point[1], start_point[0]  # lat, lon of start point
        )
        
        # Log the gap for debugging
        logger.debug(f"Gap between segments: {gap:.2f} miles")
        
        # Add the segment to merged coordinates
        merged.extend(segment)
    
    return merged

def process_passage(feature: dict) -> Optional[PassageStats]:
    """Process a single passage feature from ArcGIS response."""
    try:
        properties = feature.get('properties', {})
        if not properties:
            logger.error("Feature missing properties")
            return None
            
        passage_str = str(properties.get('Passage', ''))
        if not passage_str:
            logger.error("Feature missing Passage number")
            return None
        
        # Skip Pusch Ridge bypass variants
        if passage_str in ['11a', '11e']:
            logger.info(f"Skipping Pusch Ridge bypass variant ({passage_str})")
            return None
            
        # Handle passage number
        try:
            passage_num = int(passage_str)
        except ValueError:
            logger.error(f"Invalid passage number format: {passage_str}")
            return None
            
        name = properties.get('Name', f'Passage {passage_str}')
        
        try:
            official_miles = float(properties.get('Miles', 0))
        except (ValueError, TypeError):
            logger.warning(f"Invalid Miles value for passage {passage_str}, using 0")
            official_miles = 0
        
        geometry = feature.get('geometry', {})
        if not geometry:
            logger.error(f"Missing geometry for passage {passage_str}")
            return None
            
        geom_type = geometry.get('type')
        coordinates = geometry.get('coordinates', [])
        
        # Handle different geometry types
        if geom_type == 'LineString':
            # Single line segment, use as is
            pass
        elif geom_type == 'MultiLineString':
            # Multiple segments, merge them
            logger.info(f"Merging {len(coordinates)} segments for passage {passage_str}")
            coordinates = merge_multilinestring(coordinates)
        else:
            logger.error(f"Unsupported geometry type for passage {passage_str}: {geom_type}")
            return None
            
        if not coordinates:
            logger.error(f"No coordinates found for passage {passage_str}")
            return None
            
        # Inspect coordinate structure
        if not isinstance(coordinates, list):
            logger.error(f"Coordinates not in list format for passage {passage_str}: {type(coordinates)}")
            return None
            
        if coordinates and not isinstance(coordinates[0], list):
            logger.error(f"Invalid coordinate format for passage {passage_str}: {coordinates[:2]}")
            return None
            
        # Log coordinate details for debugging
        logger.debug(f"Passage {passage_str} coordinate count: {len(coordinates)}")
        if coordinates:
            logger.debug(f"First coordinate format: {coordinates[0]}")
            
        total_distance, max_gap, points = process_coordinates(coordinates)
        
        if len(points) < 2:
            logger.error(f"Insufficient valid points for passage {passage_str}")
            return None
        
        # Create stats object
        stats = PassageStats(
            passage_num=passage_num,
            name=name,
            official_miles=official_miles,
            calculated_miles=total_distance,
            point_count=len(points),
            max_gap_miles=max_gap,
            min_elevation_ft=0,  # Elevation data not provided in AZGEO
            max_elevation_ft=0,  # Elevation data not provided in AZGEO
            start_lat=points[0][0],
            start_lon=points[0][1],
            end_lat=points[-1][0],
            end_lon=points[-1][1]
        )
        
        # Create and save GPX file
        gpx_dir = DATA_DIR / 'gpx'
        gpx_dir.mkdir(parents=True, exist_ok=True)
        gpx_content = create_gpx(passage_num, name, points)
        gpx_path = gpx_dir / f'passage_{passage_num:02d}.gpx'
        gpx_path.write_text(gpx_content)
        
        return stats
        
    except Exception as e:
        passage_id = properties.get('Passage', 'unknown') if 'properties' in locals() else 'unknown'
        logger.error(f"Error processing passage {passage_id}: {str(e)}")
        return None

def update_passage_yaml(stats: PassageStats):
    """Update passage YAML file with official data."""
    yaml_dir = DATA_DIR / 'passages'
    yaml_dir.mkdir(parents=True, exist_ok=True)
    yaml_path = yaml_dir / f'passage_{stats.passage_num:02d}.yml'
    
    # Create or update YAML data
    data = {
        'name': stats.name,
        'number': stats.passage_num,
        'stats': {
            'length_miles': stats.official_miles,
            'endpoints': {
                'start': {
                    'lat': stats.start_lat,
                    'lon': stats.start_lon
                },
                'end': {
                    'lat': stats.end_lat,
                    'lon': stats.end_lon
                }
            }
        },
        'last_updated': datetime.now().strftime('%Y-%m-%d')
    }
    
    # Preserve existing data if file exists
    if yaml_path.exists():
        try:
            with open(yaml_path) as f:
                existing_data = yaml.safe_load(f)
                if existing_data:
                    # Update only the fields we want to change
                    existing_data['stats'].update(data['stats'])
                    existing_data['last_updated'] = data['last_updated']
                    data = existing_data
        except Exception as e:
            logger.warning(f"Could not read existing YAML for passage {stats.passage_num}: {str(e)}")
    
    # Write updated YAML
    with open(yaml_path, 'w') as f:
        yaml.dump(data, f, sort_keys=False, default_flow_style=False)

def save_summary(stats_list: List[PassageStats]):
    """Save processing summary to JSON."""
    summary = {
        'processed_at': datetime.now().isoformat(),
        'passages': [
            {
                'number': s.passage_num,
                'name': s.name,
                'official_miles': s.official_miles,
                'calculated_miles': s.calculated_miles,
                'point_count': s.point_count,
                'max_gap_miles': s.max_gap_miles
            }
            for s in stats_list
        ]
    }
    
    metadata_dir = DATA_DIR / 'metadata'
    metadata_dir.mkdir(parents=True, exist_ok=True)
    with open(metadata_dir / 'azt_official_summary.json', 'w') as f:
        json.dump(summary, f, indent=2)

def main():
    """Main processing function."""
    parser = argparse.ArgumentParser(description='Process AZT trail data')
    parser.add_argument('--refresh', action='store_true', help='Force download of fresh data')
    parser.add_argument('--debug', action='store_true', help='Enable debug logging')
    args = parser.parse_args()
    
    # Set logging level
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
    
    try:
        # Download or load data
        trail_data = download_trail_data(force_refresh=args.refresh)
        
        # Process each passage
        stats_list = []
        for feature in trail_data['features']:
            stats = process_passage(feature)
            if stats:
                stats_list.append(stats)
                update_passage_yaml(stats)
                logger.info(f"Processed passage {stats.passage_num}: {stats.name}")
        
        # Save summary
        save_summary(stats_list)
        logger.info(f"Successfully processed {len(stats_list)} passages")
        
    except Exception as e:
        logger.error(f"Processing failed: {str(e)}")
        raise

if __name__ == '__main__':
    main() 