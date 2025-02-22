"""
Utilities for analyzing arbitrary segments of the Arizona Trail.

This module provides functions for calculating elevation and distance statistics
between any two points on the trail, using the downloaded GPX track files.
"""

import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import math

from .gpx_parser import (
    ElevationPoint, ElevationStats, parse_gpx_file,
    find_nearest_point, get_section_stats
)

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class TrailPoint:
    """A point along the trail with optional description."""
    latitude: float
    longitude: float
    description: Optional[str] = None

@dataclass
class TrailSegment:
    """A segment of the trail between two points."""
    start_point: TrailPoint
    end_point: TrailPoint
    passages: List[int]
    stats: ElevationStats

def load_passage_points(data_dir: Path) -> Dict[int, List[ElevationPoint]]:
    """Load all passage points from GPX files.

    Args:
        data_dir: Directory containing GPX files

    Returns:
        Dictionary mapping passage number to list of track points
    """
    passage_points = {}
    gpx_dir = data_dir / 'gpx'
    logger.debug(f"Loading GPX files from {gpx_dir}")
    
    if not gpx_dir.exists():
        logger.error(f"GPX directory {gpx_dir} does not exist")
        return passage_points
        
    for gpx_file in gpx_dir.glob('passage_*.gpx'):
        try:
            passage_num = int(gpx_file.stem.split('_')[1])
            logger.debug(f"Loading passage {passage_num} from {gpx_file}")
            points = parse_gpx_file(gpx_file)
            if points:
                passage_points[passage_num] = points.points
                logger.debug(f"Loaded {len(points.points)} points for passage {passage_num}")
            else:
                logger.warning(f"No points found in {gpx_file}")
        except (ValueError, IndexError) as e:
            logger.error(f"Error parsing {gpx_file}: {e}")
            continue
    
    logger.debug(f"Loaded {len(passage_points)} passages")
    return passage_points

def find_containing_passage(
    point: TrailPoint,
    passage_points: Dict[int, List[ElevationPoint]],
    max_distance_mi: float = 0.5  # Increased from 0.1 to 0.5 miles
) -> Optional[int]:
    """Find which passage contains a given point.
    
    Args:
        point: Point to locate
        passage_points: Dict of passage points
        max_distance_mi: Maximum distance in miles to consider point part of passage
        
    Returns:
        Passage number containing the point, or None if not found
    """
    min_dist = float('inf')
    best_passage = None
    
    for passage_num, points in passage_points.items():
        # Find nearest point in this passage
        idx = find_nearest_point(points, point.latitude, point.longitude)
        nearest = points[idx]
        
        # Calculate distance
        from .gpx_parser import haversine_distance
        dist = haversine_distance(
            point.latitude, point.longitude,
            nearest.latitude, nearest.longitude
        )
        
        logger.info(
            f"Distance from point {point.description} to nearest point in passage {passage_num}: {dist:.2f} miles"
        )
        
        if dist < min_dist and dist <= max_distance_mi:
            min_dist = dist
            best_passage = passage_num
    
    if best_passage:
        logger.info(f"Found containing passage {best_passage} at distance {min_dist:.2f} miles")
    else:
        logger.warning(
            f"No passage found within {max_distance_mi} miles of point {point.description}"
        )
    
    return best_passage

def analyze_segment(
    start: TrailPoint,
    end: TrailPoint,
    data_dir: Path
) -> Optional[TrailSegment]:
    """Analyze a segment of trail between two points.

    Args:
        start: Starting point
        end: Ending point
        data_dir: Directory containing GPX files

    Returns:
        TrailSegment object with statistics, or None if segment invalid
        
    Raises:
        ValueError: If points are not near the trail
    """
    # Load all passage points
    passage_points = load_passage_points(data_dir)
    
    # Find containing passages
    start_passage = find_containing_passage(start, passage_points, max_distance_mi=0.5)
    end_passage = find_containing_passage(end, passage_points, max_distance_mi=0.5)

    if not start_passage or not end_passage:
        raise ValueError("Points must be within 0.5 miles of the trail")
    
    # Get all passages in the segment
    passages = list(range(
        min(start_passage, end_passage),
        max(start_passage, end_passage) + 1
    ))
    
    # Find nearest points in start/end passages
    start_idx = find_nearest_point(
        passage_points[start_passage],
        start.latitude, start.longitude
    )
    end_idx = find_nearest_point(
        passage_points[end_passage],
        end.latitude, end.longitude
    )
    
    # Combine points from all passages
    all_points = []
    for passage_num in passages:
        if passage_num == start_passage:
            # Include points from nearest start
            all_points.extend(passage_points[passage_num][start_idx:])
        elif passage_num == end_passage:
            # Include points up to nearest end
            all_points.extend(passage_points[passage_num][:end_idx+1])
        else:
            # Include all points
            all_points.extend(passage_points[passage_num])
    
    # Calculate statistics
    stats = get_section_stats(all_points, 0, len(all_points)-1)
    
    return TrailSegment(
        start_point=start,
        end_point=end,
        passages=passages,
        stats=stats
    )

def main():
    """Example usage of the trail analyzer."""
    # Example: Analyze segment between two points
    start = TrailPoint(
        passage_num=14,
        latitude=34.3139,
        longitude=-111.4518,
        description="Pine Trailhead"
    )
    end = TrailPoint(
        passage_num=15,
        latitude=34.3985,
        longitude=-111.4549,
        description="East Verde River"
    )
    
    data_dir = Path(__file__).parent.parent / 'data'
    segment = analyze_segment(start, end, data_dir)
    
    print(f"\nAnalyzing trail segment:")
    print(f"From: {start.description} ({start.latitude}, {start.longitude})")
    print(f"To: {end.description} ({end.latitude}, {end.longitude})")
    print(f"\nSegment spans passages: {segment.passages}")
    print(f"\nStatistics:")
    print(f"Distance: {segment.stats.total_distance_mi:.1f} miles")
    print(f"Elevation gain: {segment.stats.total_gain_ft:.0f} ft")
    print(f"Elevation loss: {segment.stats.total_loss_ft:.0f} ft")
    print(f"Starting elevation: {segment.start_point.latitude:.0f} ft")
    print(f"Ending elevation: {segment.end_point.latitude:.0f} ft")
    print(f"Average grade: {segment.stats.avg_grade_pct:.1f}%")
    print(f"Maximum grade: {segment.stats.max_grade_pct:.1f}%")

if __name__ == '__main__':
    main() 