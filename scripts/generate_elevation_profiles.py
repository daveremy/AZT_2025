#!/usr/bin/env python3
"""
Generate elevation profiles for the Arizona Trail using data from the azt_official_data package.

This script creates:
1. A master elevation profile for the entire trail
2. Individual section profiles for each passage

Usage:
    python3 generate_elevation_profiles.py

Dependencies:
    - numpy
    - matplotlib
    - pyyaml
"""

import os
import sys
import yaml
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import json

# Constants
OUTPUT_DIR = Path('assets/images/elevation')
DATA_FILE = Path('_data/passages.yml')
COLORS = {
    'line': 'steelblue',
    'fill': 'steelblue',
    'peak': 'red',
    'landmark': 'blue',
    'grid': 'gray',
    'background': '#f8f9fa'
}

def load_passage_data():
    """Load passage data from the YAML file."""
    with open(DATA_FILE, 'r') as f:
        data = yaml.safe_load(f)
    return data['passages']

def calculate_total_miles(passages):
    """Calculate the total trail miles."""
    return sum(passage.get('length_miles', 0) for passage in passages)

def validate_passage(passage):
    """Check if a passage has all the required fields."""
    required_fields = ['number', 'name', 'length_miles', 'elevation']
    if not all(field in passage for field in required_fields):
        return False
    
    # Check elevation fields
    elevation_fields = ['start_ft', 'end_ft', 'min_ft', 'max_ft', 'total_gain_ft']
    if not all(field in passage['elevation'] for field in elevation_fields):
        return False
    
    return True

def generate_elevation_data(passages):
    """Generate elevation data points for plotting."""
    # Filter out passages without required data
    valid_passages = []
    for i, passage in enumerate(passages):
        if validate_passage(passage):
            valid_passages.append(passage)
        else:
            print(f"Skipping passage {i+1} due to missing data: {passage.get('name', 'Unknown')}")
    
    # Calculate cumulative miles for each passage
    cumulative_miles = 0
    passage_markers = []
    
    for passage in valid_passages:
        start_mile = cumulative_miles
        cumulative_miles += passage['length_miles']
        
        passage_markers.append({
            'name': passage['name'],
            'number': passage['number'],
            'start_mile': start_mile,
            'end_mile': cumulative_miles,
            'start_elev': passage['elevation']['start_ft'],
            'end_elev': passage['elevation']['end_ft'],
            'min_elev': passage['elevation']['min_ft'],
            'max_elev': passage['elevation']['max_ft']
        })
    
    # Create interpolated elevation data
    total_miles = cumulative_miles
    miles = np.linspace(0, total_miles, int(total_miles * 10))  # 10 points per mile
    elevations = np.zeros_like(miles)
    
    # Interpolate elevations between passage endpoints
    for i, mile in enumerate(miles):
        # Find which passage this mile is in
        for marker in passage_markers:
            if marker['start_mile'] <= mile <= marker['end_mile']:
                # Calculate position within passage (0 to 1)
                passage_length = marker['end_mile'] - marker['start_mile']
                if passage_length == 0:
                    position = 0
                else:
                    position = (mile - marker['start_mile']) / passage_length
                
                # Linear interpolation between start and end elevations
                base_elevation = marker['start_elev'] + position * (marker['end_elev'] - marker['start_elev'])
                
                # Add some natural variation (more pronounced near max elevation points)
                # This is a simplified approach - the real trail has more complex elevation patterns
                max_variation = 300 * (1 - abs(2 * position - 1))  # More variation in the middle
                variation = np.random.normal(0, max_variation)
                
                # Ensure we don't go below min or above max for the passage
                elevation = base_elevation + variation
                elevation = max(elevation, marker['min_elev'])
                elevation = min(elevation, marker['max_elev'])
                
                elevations[i] = elevation
                break
    
    return miles, elevations, passage_markers, valid_passages

def identify_landmarks_and_peaks(passages):
    """Identify major landmarks and peaks along the trail."""
    landmarks = []
    cumulative_miles = 0
    
    for passage in passages:
        # Add passage start point as landmark if it has a southern access point
        if passage['number'] == '1' and 'access_points' in passage:  # First passage
            for ap in passage['access_points']:
                if ap['type'] == 'southern':
                    landmarks.append({
                        'mile': 0,
                        'elev': passage['elevation']['start_ft'],
                        'name': ap['name'],
                        'type': 'landmark'
                    })
                    break
        
        # Add passage end point as landmark if it's the last passage
        last_passage_number = max(int(p['number']) for p in passages)
        if int(passage['number']) == last_passage_number and 'access_points' in passage:
            for ap in passage['access_points']:
                if ap['type'] == 'northern':
                    landmarks.append({
                        'mile': cumulative_miles + passage['length_miles'],
                        'elev': passage['elevation']['end_ft'],
                        'name': ap['name'],
                        'type': 'landmark'
                    })
                    break
        
        # Add passage midpoint with max elevation as a peak
        if passage['elevation']['max_ft'] > 8000:  # Only add significant peaks
            # Assume the max elevation is roughly in the middle of the passage
            landmarks.append({
                'mile': cumulative_miles + (passage['length_miles'] / 2),
                'elev': passage['elevation']['max_ft'],
                'name': f"{passage['name']} High Point",
                'type': 'peak'
            })
        
        # Add northern access point as landmark
        if 'access_points' in passage:
            for ap in passage['access_points']:
                if ap['type'] == 'northern' and int(passage['number']) % 5 == 0:  # Only add every 5th passage to avoid crowding
                    landmarks.append({
                        'mile': cumulative_miles + passage['length_miles'],
                        'elev': passage['elevation']['end_ft'],
                        'name': ap['name'],
                        'type': 'landmark'
                    })
                    break
        
        cumulative_miles += passage['length_miles']
    
    return landmarks

def create_master_profile(passages):
    """Create the master elevation profile for the entire trail."""
    miles, elevations, passage_markers, valid_passages = generate_elevation_data(passages)
    landmarks = identify_landmarks_and_peaks(valid_passages)
    
    plt.figure(figsize=(20, 8))
    plt.plot(miles, elevations, color=COLORS['line'], linewidth=2, alpha=0.7)
    plt.fill_between(miles, elevations, alpha=0.3, color=COLORS['fill'])
    
    # Set background color and grid
    plt.gca().set_facecolor(COLORS['background'])
    plt.grid(True, alpha=0.3, color=COLORS['grid'], linestyle='--')
    
    # Add passage dividers and labels
    for marker in passage_markers:
        plt.axvline(x=marker['start_mile'], color=COLORS['grid'], linestyle='--', alpha=0.5)
        
        # Add passage label for every 5th passage to avoid crowding
        if int(marker['number']) % 5 == 0:
            section_middle = (marker['start_mile'] + marker['end_mile']) / 2
            section_height = max(elevations) - 1000
            plt.text(section_middle, section_height,
                    f'Passage {marker["number"]}\n{marker["name"]}',
                    ha='center', va='bottom',
                    bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=2),
                    fontsize=8)
    
    # Add landmarks and peaks
    for landmark in landmarks:
        if landmark['type'] == 'peak':
            # Peaks get red triangles and labels above
            plt.plot(landmark['mile'], landmark['elev'], '^', color=COLORS['peak'], markersize=8)
            plt.text(landmark['mile'], landmark['elev'] + 200,
                    f'{landmark["name"]}\n{int(landmark["elev"])}ft',
                    ha='center', va='bottom', color=COLORS['peak'],
                    bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=2),
                    fontsize=8)
        else:
            # Regular landmarks get blue dots and labels below
            plt.plot(landmark['mile'], landmark['elev'], 'o', color=COLORS['landmark'], markersize=6)
            plt.text(landmark['mile'], landmark['elev'] - 400,
                    f'{landmark["name"]}\n{int(landmark["elev"])}ft',
                    ha='center', va='top', rotation=45,
                    bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=2),
                    fontsize=8)
    
    # Customize axes
    plt.xlabel('Miles', fontsize=10, fontweight='bold')
    plt.ylabel('Elevation (ft)', fontsize=10, fontweight='bold')
    plt.title('Arizona Trail Elevation Profile', fontsize=14, fontweight='bold', pad=20)
    
    # Add elevation range text
    elevation_range = f'Elevation Range: {int(min(elevations))} - {int(max(elevations))} ft'
    plt.text(0.02, 0.98, elevation_range,
            transform=plt.gca().transAxes,
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=2),
            fontsize=8)
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'azt_elevation_profile.png',
                dpi=300, bbox_inches='tight', facecolor=COLORS['background'])
    plt.close()

def create_section_profiles(passages):
    """Create individual elevation profiles for each passage."""
    cumulative_miles = 0
    
    for passage in passages:
        # Skip passages without required data
        if not validate_passage(passage):
            continue
        
        plt.figure(figsize=(10, 4))
        
        # Create a simple elevation profile for this passage
        passage_length = passage['length_miles']
        miles = np.linspace(0, passage_length, int(passage_length * 10))  # 10 points per mile
        
        # Create a more natural-looking elevation profile
        # Start and end at the correct elevations
        start_elev = passage['elevation']['start_ft']
        end_elev = passage['elevation']['end_ft']
        min_elev = passage['elevation']['min_ft']
        max_elev = passage['elevation']['max_ft']
        
        # Base profile is a combination of linear trend and a sine wave
        base_profile = np.linspace(start_elev, end_elev, len(miles))
        
        # Add a peak in the middle if max elevation is significantly higher
        if max_elev > max(start_elev, end_elev) + 500:
            peak_factor = 0.5  # Peak in the middle
            peak_shape = np.sin(np.linspace(0, np.pi, len(miles)))
            peak_height = max_elev - max(start_elev, end_elev)
            base_profile += peak_shape * peak_height
        
        # Add some random variation
        variation = np.random.normal(0, 100, len(miles))
        elevations = base_profile + variation
        
        # Ensure we stay within min/max bounds
        elevations = np.clip(elevations, min_elev, max_elev)
        
        # Plot the profile
        plt.plot(miles, elevations, color=COLORS['line'], linewidth=2)
        plt.fill_between(miles, elevations, alpha=0.3, color=COLORS['fill'])
        
        # Add landmarks
        if 'access_points' in passage:
            for ap in passage['access_points']:
                if ap['type'] == 'southern':
                    plt.plot(0, start_elev, 'o', color=COLORS['landmark'], markersize=6)
                    plt.text(0, start_elev - 200,
                            f'{ap["name"]}\n{int(start_elev)}ft',
                            ha='center', va='top',
                            bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=2),
                            fontsize=8)
                elif ap['type'] == 'northern':
                    plt.plot(passage_length, end_elev, 'o', color=COLORS['landmark'], markersize=6)
                    plt.text(passage_length, end_elev - 200,
                            f'{ap["name"]}\n{int(end_elev)}ft',
                            ha='center', va='top',
                            bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=2),
                            fontsize=8)
        
        # Add high point if it's significant
        if max_elev > max(start_elev, end_elev) + 500:
            high_point_mile = passage_length / 2  # Approximate
            plt.plot(high_point_mile, max_elev, '^', color=COLORS['peak'], markersize=8)
            plt.text(high_point_mile, max_elev + 200,
                    f'High Point\n{int(max_elev)}ft',
                    ha='center', va='bottom', color=COLORS['peak'],
                    bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=2),
                    fontsize=8)
        
        plt.grid(True, alpha=0.3)
        plt.title(f'Passage {passage["number"]}: {passage["name"]}')
        
        # Add elevation stats
        stats_text = (
            f'Length: {passage["length_miles"]:.1f} miles\n'
            f'Elevation: {int(min_elev)} - {int(max_elev)} ft\n'
            f'Gain: {int(passage["elevation"]["total_gain_ft"])} ft'
        )
        plt.text(0.02, 0.98, stats_text,
                transform=plt.gca().transAxes,
                bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=2),
                fontsize=8)
        
        # Save the section profile
        filename = f'{int(passage["number"]):02d}_elevation.png'
        plt.savefig(OUTPUT_DIR / filename, dpi=300, bbox_inches='tight')
        plt.close()
        
        cumulative_miles += passage_length

def main():
    """Generate all elevation profiles."""
    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Load passage data
    passages = load_passage_data()
    
    # Debug: print the number of passages
    print(f"Loaded {len(passages)} passages")
    
    # Create profiles
    print("Generating master elevation profile...")
    create_master_profile(passages)
    
    print("Generating individual passage profiles...")
    create_section_profiles(passages)
    
    print("Elevation profiles generated successfully!")

if __name__ == "__main__":
    main() 