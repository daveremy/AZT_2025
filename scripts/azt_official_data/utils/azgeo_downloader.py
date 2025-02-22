"""
DEPRECATED: This module is no longer used as we now get all trail data from GPX files.
This module was originally used for downloading trail geometry data from AZGEO but has
been superseded by direct GPX track processing.

Kept for reference but should be removed in future updates.

This module handles fetching and caching of trail geometry data from the
Arizona Geographic Information Council (AZGEO) ArcGIS service.
"""

import json
import logging
import math
import os
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import re

import requests

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

# Package-local cache directory
PACKAGE_DIR = Path(__file__).parent.parent
CACHE_DIR = PACKAGE_DIR / 'cache'
AZGEO_CACHE_FILE = CACHE_DIR / 'azt_polyline.geojson'

def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculate distance between two points in miles.
    
    Args:
        lat1: Latitude of first point
        lon1: Longitude of first point
        lat2: Latitude of second point
        lon2: Longitude of second point
        
    Returns:
        Distance in miles between the points
    """
    R = 3959.87433  # Earth's radius in miles

    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    return R * c

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

def download_trail_data(force_refresh: bool = False) -> Dict:
    """Download or load trail data from AZGEO.
    
    Args:
        force_refresh: Whether to force a fresh download
        
    Returns:
        Dict containing the GeoJSON data
        
    Raises:
        requests.RequestException: If the download fails
        json.JSONDecodeError: If the response is invalid JSON
        ValueError: If the response data is invalid
    """
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    
    if AZGEO_CACHE_FILE.exists() and not force_refresh:
        logger.info("Loading cached trail data...")
        with open(AZGEO_CACHE_FILE) as f:
            data = json.load(f)
            logger.info(f"Loaded {len(data['features'])} features from cache")
            return data
    
    logger.info("Downloading fresh trail data from AZGEO...")
    response = requests.get(AZGEO_URL, params=QUERY_PARAMS)
    response.raise_for_status()
    data = response.json()
    
    # Validate response structure
    if not isinstance(data, dict) or 'features' not in data:
        raise ValueError("Invalid response format from AZGEO")
    
    # Save to cache
    with open(AZGEO_CACHE_FILE, 'w') as f:
        json.dump(data, f, indent=2)
    logger.info(f"Downloaded and cached {len(data['features'])} features")
    
    return data

def process_feature(feature: Dict) -> Optional[Dict]:
    """Process a single feature from the AZGEO data.
    
    Args:
        feature: Dict containing a GeoJSON feature
        
    Returns:
        Dict containing processed geometry and properties,
        or None if the feature should be skipped
    """
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
        
    # Calculate statistics
    try:
        total_distance, max_gap, points = process_coordinates(coordinates)
    except ValueError as e:
        logger.error(f"Error processing coordinates for passage {passage_str}: {e}")
        return None
    
    # Extract elevation data from GPX file
    gpx_path = Path('data/gpx') / f'passage_{passage_str}_gps.gpx'
    min_elevation = float('inf')
    max_elevation = float('-inf')
    
    if gpx_path.exists():
        try:
            with open(gpx_path) as f:
                gpx_data = f.read()
                for ele_match in re.finditer(r'<ele>(\d+\.?\d*)</ele>', gpx_data):
                    elevation = float(ele_match.group(1))
                    min_elevation = min(min_elevation, elevation)
                    max_elevation = max(max_elevation, elevation)
                
                if min_elevation == float('inf'):
                    min_elevation = 0
                    max_elevation = 0
        except Exception as e:
            logger.error(f"Error reading elevation data from GPX for passage {passage_str}: {e}")
            min_elevation = 0
            max_elevation = 0
    else:
        logger.warning(f"No GPX file found for passage {passage_str}")
        min_elevation = 0
        max_elevation = 0
    
    # Return processed data
    return {
        'number': passage_str,
        'name': properties.get('Name', f'Passage {passage_str}'),
        'length_miles': float(properties.get('Miles', total_distance)),
        'min_elevation_ft': min_elevation,
        'max_elevation_ft': max_elevation,
        'calculated_miles': total_distance,
        'max_gap_miles': max_gap,
        'point_count': len(points),
        'start_coords': points[0][:2],  # (lat, lon)
        'end_coords': points[-1][:2],   # (lat, lon)
        'geometry': {
            'type': 'LineString',
            'coordinates': [[lon, lat] for lat, lon, _ in points]
        }
    } 