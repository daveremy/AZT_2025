"""
DEPRECATED: This module is no longer used as we now get all trail data from GPX files.
This module was originally used for parsing geographic data from AZGEO sources but has
been superseded by direct GPX track processing.

Kept for reference but should be removed in future updates.
"""

import json
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import geopandas as gpd
import numpy as np
from shapely.geometry import LineString, Point
from shapely.wkt import loads as wkt_loads

from .azgeo_downloader import download_trail_data, process_feature

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class PassageGeometry:
    """Geographic data for a passage from AZGEO."""
    number: str
    length_miles: float
    min_elevation_ft: float
    max_elevation_ft: float
    start_coords: Tuple[float, float]  # (lon, lat)
    end_coords: Tuple[float, float]    # (lon, lat)
    geometry: LineString

def load_azgeo_data(force_refresh: bool = False) -> Dict[str, PassageGeometry]:
    """Load passage geometry data from AZGEO GeoJSON file.
    
    Args:
        force_refresh: Whether to force a fresh download from AZGEO.
        
    Returns:
        Dict mapping passage numbers to PassageGeometry objects.
        
    Raises:
        FileNotFoundError: If the GeoJSON file doesn't exist.
        ValueError: If the GeoJSON file is invalid or missing required data.
    """
    logger.info("Loading AZGEO data...")
    
    # Download or load cached data
    data = download_trail_data(force_refresh)
    
    passages: Dict[str, PassageGeometry] = {}
    
    # Process each feature
    for feature in data['features']:
        processed = process_feature(feature)
        if not processed:
            continue
            
        # Convert processed data to PassageGeometry
        try:
            geometry = LineString(processed['geometry']['coordinates'])
            passage = PassageGeometry(
                number=processed['number'],
                length_miles=processed['length_miles'],
                min_elevation_ft=processed['min_elevation_ft'],
                max_elevation_ft=processed['max_elevation_ft'],
                start_coords=processed['start_coords'][::-1],  # Reverse (lat,lon) to (lon,lat)
                end_coords=processed['end_coords'][::-1],     # Reverse (lat,lon) to (lon,lat)
                geometry=geometry
            )
            passages[passage.number] = passage
            
        except Exception as e:
            logger.error(f"Error creating PassageGeometry for passage {processed['number']}: {e}")
            continue
    
    logger.info(f"Loaded geometry data for {len(passages)} passages")
    return passages

def get_passage_elevation_profile(
    passage: PassageGeometry,
    dem_path: Optional[Path] = None
) -> List[Tuple[float, float]]:
    """Generate elevation profile for a passage.
    
    Args:
        passage: PassageGeometry object containing the passage geometry.
        dem_path: Optional path to DEM (Digital Elevation Model) data.
        
    Returns:
        List of (distance, elevation) tuples representing the elevation profile.
    """
    return [] 