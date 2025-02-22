"""
Utilities for downloading GPX track files from the ATA website.

This module provides functions for downloading and saving GPX track files
from the Arizona Trail Association website.
"""

import argparse
import logging
import os
from pathlib import Path
import time
from typing import Dict, List, Optional

import requests
import yaml

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Request headers to mimic a browser
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
}

def download_gpx_tracks(yaml_path: Path, output_dir: Path) -> None:
    """Download GPX track files from URLs in passages.yml.
    
    Args:
        yaml_path: Path to passages.yml file
        output_dir: Directory to save GPX files in
        
    Raises:
        FileNotFoundError: If yaml_path doesn't exist
        yaml.YAMLError: If yaml_path is invalid
        requests.RequestException: If download fails
    """
    logger.info(f"Loading passage data from {yaml_path}")
    
    # Load passages.yml
    with open(yaml_path) as f:
        data = yaml.safe_load(f)
    
    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Download each track file
    for passage in data['passages']:
        num = passage['number']
        track_url = passage['resources'].get('track_url')
        
        if not track_url:
            logger.warning(f"No track URL for passage {num}")
            continue
        
        # Construct output path
        output_path = output_dir / f"passage_{num.zfill(2)}.gpx"
        
        try:
            logger.info(f"Downloading track for passage {num} from {track_url}")
            
            # Download file with headers
            response = requests.get(track_url, headers=HEADERS)
            response.raise_for_status()
            
            # Save to file
            with open(output_path, 'wb') as f:
                f.write(response.content)
            
            logger.info(f"Saved track to {output_path}")
            
            # Add delay between downloads
            time.sleep(1)
            
        except requests.RequestException as e:
            logger.error(f"Failed to download track for passage {num}: {e}")
            continue
        except OSError as e:
            logger.error(f"Failed to save track for passage {num}: {e}")
            continue
    
    logger.info("Finished downloading track files")

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Download GPX track files from ATA website.'
    )
    parser.add_argument(
        '--yaml-path',
        type=Path,
        default=Path(__file__).parent.parent.parent.parent / '_data' / 'passages.yml',
        help='Path to passages.yml file'
    )
    parser.add_argument(
        '--output-dir',
        type=Path,
        default=Path(__file__).parent.parent / 'data' / 'gpx',
        help='Directory to save GPX files in'
    )
    return parser.parse_args()

def main():
    """Main entry point."""
    args = parse_args()
    download_gpx_tracks(args.yaml_path, args.output_dir)

if __name__ == '__main__':
    main() 