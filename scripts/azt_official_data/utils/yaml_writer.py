"""
Utilities for writing passage data to YAML format.

This module handles the generation of the passages.yml file, combining data
from the ATA website and GPX track files with proper attribution and formatting.
"""

import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
import numpy as np

import yaml

from .ata_parser import PassageResources
from .gpx_parser import parse_gpx_file, ElevationStats

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Add numpy float representer
def numpy_float_representer(dumper, data):
    return dumper.represent_float(float(data))

yaml.add_representer(np.float64, numpy_float_representer)

def write_passages_yaml(
    output_path: Path,
    ata_passages: List[PassageResources],
    data_dir: Path
) -> None:
    """Write passage data to YAML file.
    
    Args:
        output_path: Path to write YAML file to
        ata_passages: List of passage data from ATA website
        data_dir: Base directory for data files
        
    Raises:
        OSError: If output file cannot be written
        ValueError: If passage data is invalid
    """
    logger.info(f"Writing passage data to {output_path}")
    
    # Prepare metadata
    data = {
        'metadata': {
            'last_updated': datetime.now().strftime('%Y-%m-%d'),
            'data_sources': [
                {
                    'name': 'Arizona Trail Association (ATA)',
                    'description': 'Official passage information, maps, and resources',
                    'url': 'https://aztrail.org/explore/passages/',
                    'last_updated': datetime.now().strftime('%Y-%m-%d')
                }
            ]
        },
        'passages': []
    }
    
    # Process each passage
    for ata_passage in ata_passages:
        passage_data = {
            'number': str(ata_passage.number),
            'name': ata_passage.name,
            'resources': {
                'info_page': ata_passage.info_page,
                'map_url': ata_passage.map_url,
                'profile_url': ata_passage.profile_url,
                'track_url': ata_passage.gpx_url
            }
        }
        
        # Add access points if available
        if ata_passage.access_points:
            passage_data['access_points'] = []
            for ap in ata_passage.access_points:
                access_point = {
                    'type': ap['type'],
                    'name': ap['name']
                }
                if ap['coordinates']:
                    access_point['coordinates'] = ap['coordinates']
                if ap['notes']:
                    access_point['notes'] = ap['notes']
                passage_data['access_points'].append(access_point)
        
        # Try to load GPX track data
        passage_num = str(ata_passage.number).zfill(2)  # Zero-pad to 2 digits
        gpx_path = data_dir / 'gpx' / f'passage_{passage_num}.gpx'
        try:
            stats = parse_gpx_file(gpx_path)
            passage_data.update({
                'length_miles': float(round(stats.total_distance_mi, 1)),
                'elevation': {
                    'start_ft': float(round(stats.start_elevation_ft)),
                    'end_ft': float(round(stats.end_elevation_ft)),
                    'min_ft': float(round(stats.min_elevation_ft)),
                    'max_ft': float(round(stats.max_elevation_ft)),
                    'total_gain_ft': float(round(stats.total_gain_ft)),
                    'total_loss_ft': float(round(stats.total_loss_ft)),
                    'avg_grade_pct': float(round(stats.avg_grade_pct, 1)),
                    'max_grade_pct': float(round(stats.max_grade_pct, 1)),
                    'per_mile_ft': float(round(stats.elevation_per_mile_ft, 1))
                },
                'coordinates': {
                    'start': {
                        'lat': float(round(stats.points[0].latitude, 5)),
                        'lon': float(round(stats.points[0].longitude, 5))
                    },
                    'end': {
                        'lat': float(round(stats.points[-1].latitude, 5)),
                        'lon': float(round(stats.points[-1].longitude, 5))
                    }
                }
            })
        except Exception as e:
            logger.warning(f"Could not load GPX data for passage {ata_passage.number}: {e}")
        
        data['passages'].append(passage_data)
    
    # Write YAML file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        yaml.safe_dump(data, f, sort_keys=False, indent=2)
    
    logger.info(f"Wrote {len(data['passages'])} passages to {output_path}")

def read_passages_yaml(yaml_path: Path) -> Dict:
    """Read passages from YAML file.
    
    Args:
        yaml_path: Path to the YAML file.
        
    Returns:
        Dict containing the YAML data.
        
    Raises:
        FileNotFoundError: If the YAML file doesn't exist.
        ValueError: If the YAML file is invalid.
    """
    logger.info(f"Reading passages from {yaml_path}")
    
    if not yaml_path.exists():
        raise FileNotFoundError(f"YAML file not found: {yaml_path}")
    
    try:
        with open(yaml_path) as f:
            data = yaml.safe_load(f)
    except Exception as e:
        raise ValueError(f"Error reading YAML file: {e}")
    
    # Validate structure
    if not isinstance(data, dict):
        raise ValueError("Invalid YAML structure: root must be a dict")
    
    if 'metadata' not in data or 'passages' not in data:
        raise ValueError("Invalid YAML structure: missing metadata or passages")
    
    if not isinstance(data['passages'], list):
        raise ValueError("Invalid YAML structure: passages must be a list")
    
    return data 