#!/usr/bin/env python3
"""
Main script for updating the passages.yml file with data from multiple sources.

This script fetches data from the Arizona Trail Association (ATA) website and
combines it with elevation data from GPX track files to create a comprehensive
passages.yml file.

Usage:
    python3 update_passages.py [--output OUTPUT] [--data-dir DATA_DIR]

Options:
    --output OUTPUT   Output path for passages.yml [default: _data/passages.yml]
    --data-dir DATA_DIR Base directory for data files [default: azt_official_data/data]
"""

import argparse
import logging
import os
import sys
from pathlib import Path

try:
    # When running as a module
    from .utils.ata_parser import extract_passage_info, get_passage_details
    from .utils.yaml_writer import write_passages_yaml
except ImportError:
    # When running as a script
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from azt_official_data.utils.ata_parser import extract_passage_info, get_passage_details
    from azt_official_data.utils.yaml_writer import write_passages_yaml

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Update passages.yml with data from ATA website and GPX files.'
    )
    parser.add_argument(
        '--output',
        type=Path,
        default=Path(__file__).parent.parent.parent / '_data' / 'passages.yml',
        help='Output path for passages.yml'
    )
    parser.add_argument(
        '--data-dir',
        type=Path,
        default=Path(__file__).parent / 'data',
        help='Base directory for intermediate data files'
    )
    parser.add_argument(
        '--test',
        action='store_true',
        help='Test mode: only process passages 1-5'
    )
    return parser.parse_args()

def main():
    """Main entry point."""
    args = parse_args()
    
    # Create data directories
    args.data_dir.mkdir(parents=True, exist_ok=True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    
    # Extract passage info from ATA website
    passages = extract_passage_info()
    
    # In test mode, only process first 5 passages
    if args.test:
        passages = [p for p in passages if int(p.number) <= 5]
        logger.info(f"Test mode: processing {len(passages)} passages")
    
    # Get additional details for each passage
    for passage in passages:
        details = get_passage_details(passage)
        if details:
            logger.info(f"Got details for passage {passage.number}")
            if passage.access_points:
                for ap in passage.access_points:
                    logger.info(f"  Found {ap['type']}: {ap['name']}")
    
    # Write combined data to YAML
    write_passages_yaml(args.output, passages, args.data_dir)

if __name__ == '__main__':
    main() 