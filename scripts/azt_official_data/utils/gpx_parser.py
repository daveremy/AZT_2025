"""
Utilities for parsing GPX track files and calculating elevation statistics.

This module provides functions for extracting detailed elevation data from GPX
track files, including elevation gain/loss, grade statistics, and the ability
to calculate statistics between any two points on the trail.
"""

import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import xml.etree.ElementTree as ET
import math

import gpxpy
import numpy as np
from scipy import signal

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class ElevationPoint:
    """A point along the trail with distance and elevation data."""
    latitude: float
    longitude: float
    elevation_ft: float
    distance_from_start_mi: float
    grade_pct: Optional[float] = None  # Grade to next point

@dataclass
class ElevationStats:
    """Statistics about a section of trail."""
    total_distance_mi: float
    start_elevation_ft: float
    end_elevation_ft: float
    min_elevation_ft: float
    max_elevation_ft: float
    total_gain_ft: float
    total_loss_ft: float
    avg_grade_pct: float
    max_grade_pct: float
    elevation_per_mile_ft: float  # Net elevation change per mile
    points: List[ElevationPoint]  # All points in the section

def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculate distance between two points in miles."""
    R = 3959.87433  # Earth's radius in miles

    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    return R * c

def smooth_elevation_data(elevations: List[float], window_size: int = 5) -> List[float]:
    """Apply a moving average smoothing to elevation data to reduce GPS noise."""
    return list(signal.savgol_filter(elevations, window_size, 2))

def calculate_grade(dist_change_mi: float, ele_change_ft: float) -> float:
    """Calculate grade as a percentage."""
    if dist_change_mi == 0:
        return 0
    # Convert distance to feet for grade calculation
    dist_ft = dist_change_mi * 5280
    return (ele_change_ft / dist_ft) * 100

def parse_gpx_file(gpx_path: Path) -> ElevationStats:
    """Parse a GPX file and extract elevation statistics.
    
    Args:
        gpx_path: Path to the GPX file
        
    Returns:
        ElevationStats object containing elevation data and statistics
        
    Raises:
        FileNotFoundError: If the GPX file doesn't exist
        ValueError: If the GPX file is invalid or contains no track points
    """
    logger.info(f"Parsing GPX file: {gpx_path}")
    
    if not gpx_path.exists():
        raise FileNotFoundError(f"GPX file not found: {gpx_path}")
    
    # Parse GPX file
    with open(gpx_path) as f:
        gpx = gpxpy.parse(f)
    
    points: List[ElevationPoint] = []
    total_distance = 0.0
    prev_lat = prev_lon = prev_ele = None
    
    # Process all track points
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                # Convert elevation to feet
                ele_ft = point.elevation * 3.28084
                
                # Calculate distance from previous point
                if prev_lat is not None:
                    distance = haversine_distance(
                        prev_lat, prev_lon,
                        point.latitude, point.longitude
                    )
                    total_distance += distance
                    
                    # Calculate grade
                    ele_change = ele_ft - prev_ele
                    grade = calculate_grade(distance, ele_change)
                else:
                    grade = None
                
                # Create elevation point
                ele_point = ElevationPoint(
                    latitude=point.latitude,
                    longitude=point.longitude,
                    elevation_ft=ele_ft,
                    distance_from_start_mi=total_distance,
                    grade_pct=grade
                )
                points.append(ele_point)
                
                # Update previous point
                prev_lat = point.latitude
                prev_lon = point.longitude
                prev_ele = ele_ft
    
    if not points:
        raise ValueError(f"No track points found in GPX file: {gpx_path}")
    
    # Smooth elevation data
    elevations = [p.elevation_ft for p in points]
    smoothed = smooth_elevation_data(elevations)
    for point, smooth_ele in zip(points, smoothed):
        point.elevation_ft = smooth_ele
    
    # Calculate elevation changes
    total_gain = 0.0
    total_loss = 0.0
    grades = []
    
    for i in range(1, len(points)):
        ele_change = points[i].elevation_ft - points[i-1].elevation_ft
        if ele_change > 0:
            total_gain += ele_change
        else:
            total_loss += abs(ele_change)
        if points[i].grade_pct is not None:
            grades.append(abs(points[i].grade_pct))
    
    # Calculate statistics
    stats = ElevationStats(
        total_distance_mi=total_distance,
        start_elevation_ft=points[0].elevation_ft,
        end_elevation_ft=points[-1].elevation_ft,
        min_elevation_ft=min(p.elevation_ft for p in points),
        max_elevation_ft=max(p.elevation_ft for p in points),
        total_gain_ft=total_gain,
        total_loss_ft=total_loss,
        avg_grade_pct=np.mean(grades) if grades else 0,
        max_grade_pct=max(grades) if grades else 0,
        elevation_per_mile_ft=abs(points[-1].elevation_ft - points[0].elevation_ft) / total_distance if total_distance > 0 else 0,
        points=points
    )
    
    return stats

def get_section_stats(
    points: List[ElevationPoint],
    start_idx: int,
    end_idx: int
) -> ElevationStats:
    """Calculate elevation statistics for a section of trail.
    
    Args:
        points: List of all trail points
        start_idx: Index of section start point
        end_idx: Index of section end point
        
    Returns:
        ElevationStats object for the section
    """
    section = points[start_idx:end_idx+1]
    if not section:
        raise ValueError("No points in section")
    
    # Calculate distance (section distance is relative to section start)
    total_distance = section[-1].distance_from_start_mi - section[0].distance_from_start_mi
    
    # Calculate elevation changes
    total_gain = 0.0
    total_loss = 0.0
    grades = []
    
    for i in range(1, len(section)):
        ele_change = section[i].elevation_ft - section[i-1].elevation_ft
        if ele_change > 0:
            total_gain += ele_change
        else:
            total_loss += abs(ele_change)
        if section[i].grade_pct is not None:
            grades.append(abs(section[i].grade_pct))
    
    return ElevationStats(
        total_distance_mi=total_distance,
        start_elevation_ft=section[0].elevation_ft,
        end_elevation_ft=section[-1].elevation_ft,
        min_elevation_ft=min(p.elevation_ft for p in section),
        max_elevation_ft=max(p.elevation_ft for p in section),
        total_gain_ft=total_gain,
        total_loss_ft=total_loss,
        avg_grade_pct=np.mean(grades) if grades else 0,
        max_grade_pct=max(grades) if grades else 0,
        elevation_per_mile_ft=abs(section[-1].elevation_ft - section[0].elevation_ft) / total_distance if total_distance > 0 else 0,
        points=section
    )

def find_nearest_point(
    points: List[ElevationPoint],
    latitude: float,
    longitude: float
) -> int:
    """Find the index of the nearest track point to given coordinates.
    
    Args:
        points: List of track points
        latitude: Target latitude
        longitude: Target longitude
        
    Returns:
        Index of the nearest point
    """
    min_dist = float('inf')
    min_idx = 0
    
    for i, point in enumerate(points):
        dist = haversine_distance(
            latitude, longitude,
            point.latitude, point.longitude
        )
        if dist < min_dist:
            min_dist = dist
            min_idx = i
    
    return min_idx 