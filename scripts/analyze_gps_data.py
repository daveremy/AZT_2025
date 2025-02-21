#!/usr/bin/env python3
"""
Analyze GPS data availability for Arizona Trail passages.
This script checks available GPS files and validates passage information.
"""

import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import gpxpy
import json
from pathlib import Path

class AZTPassageAnalyzer:
    def __init__(self):
        self.base_url = "https://aztrail.org/explore/passages/"
        self.data_dir = Path("data/passages")
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
    def scrape_passage_info(self):
        """Scrape passage information from the AZT website."""
        print("Fetching passage information...")
        response = requests.get(self.base_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        passages = []
        # Find passage tables (North, Central, South sections)
        for table in soup.find_all('table'):
            rows = table.find_all('tr')[1:]  # Skip header row
            for row in rows:
                cols = row.find_all('td')
                if len(cols) >= 4:
                    passage = {
                        'number': cols[0].text.strip(),
                        'name': cols[1].text.strip(),
                        'length': cols[2].text.strip(),
                        'description': cols[3].text.strip(),
                        'gpx_link': None,
                        'milepoint_link': None
                    }
                    
                    # Find GPS and milepoint links
                    for link in cols[1].find_all('a'):
                        href = link.get('href', '')
                        if 'gpx' in href.lower():
                            passage['gpx_link'] = href
                        elif 'milepoint' in href.lower():
                            passage['milepoint_link'] = href
                            
                    passages.append(passage)
        
        return passages

    def download_passage_data(self, passages):
        """Download GPX and milepoint files for each passage."""
        print("\nDownloading passage data...")
        for passage in passages:
            passage_dir = self.data_dir / f"passage_{passage['number'].zfill(2)}"
            passage_dir.mkdir(exist_ok=True)
            
            # Download GPX file
            if passage['gpx_link']:
                gpx_path = passage_dir / 'track.gpx'
                if not gpx_path.exists():
                    try:
                        response = requests.get(passage['gpx_link'])
                        with open(gpx_path, 'wb') as f:
                            f.write(response.content)
                        print(f"Downloaded GPX for Passage {passage['number']}")
                    except Exception as e:
                        print(f"Error downloading GPX for Passage {passage['number']}: {e}")
            
            # Download milepoint file
            if passage['milepoint_link']:
                milepoint_path = passage_dir / 'milepoints.json'
                if not milepoint_path.exists():
                    try:
                        response = requests.get(passage['milepoint_link'])
                        with open(milepoint_path, 'wb') as f:
                            f.write(response.content)
                        print(f"Downloaded milepoints for Passage {passage['number']}")
                    except Exception as e:
                        print(f"Error downloading milepoints for Passage {passage['number']}: {e}")

    def analyze_gpx_data(self, passages):
        """Analyze downloaded GPX files for distance and elevation data."""
        print("\nAnalyzing GPX data...")
        analysis = []
        
        for passage in passages:
            passage_dir = self.data_dir / f"passage_{passage['number'].zfill(2)}"
            gpx_path = passage_dir / 'track.gpx'
            
            passage_analysis = {
                'number': passage['number'],
                'name': passage['name'],
                'stated_length': passage['length'],
                'gpx_available': False,
                'milepoints_available': False,
                'calculated_length': None,
                'elevation_gain': None,
                'elevation_loss': None,
                'max_elevation': None,
                'min_elevation': None
            }
            
            # Check GPX availability and analyze if present
            if gpx_path.exists():
                passage_analysis['gpx_available'] = True
                try:
                    with open(gpx_path, 'r') as gpx_file:
                        gpx = gpxpy.parse(gpx_file)
                        
                        # Calculate statistics
                        length_km = gpx.length_3d() / 1000
                        passage_analysis['calculated_length'] = f"{length_km:.1f} km"
                        
                        # Calculate elevation data
                        elevation_data = [(point.elevation, point.latitude, point.longitude) 
                                        for track in gpx.tracks 
                                        for segment in track.segments 
                                        for point in segment.points 
                                        if point.elevation is not None]
                        
                        if elevation_data:
                            elevations = [e[0] for e in elevation_data]
                            passage_analysis['max_elevation'] = f"{max(elevations):.1f}m"
                            passage_analysis['min_elevation'] = f"{min(elevations):.1f}m"
                            
                            # Calculate elevation gain/loss
                            gain = loss = 0
                            for i in range(1, len(elevations)):
                                diff = elevations[i] - elevations[i-1]
                                if diff > 0:
                                    gain += diff
                                else:
                                    loss += abs(diff)
                            
                            passage_analysis['elevation_gain'] = f"{gain:.1f}m"
                            passage_analysis['elevation_loss'] = f"{loss:.1f}m"
                except Exception as e:
                    print(f"Error analyzing GPX for Passage {passage['number']}: {e}")
            
            # Check milepoints availability
            milepoint_path = passage_dir / 'milepoints.json'
            passage_analysis['milepoints_available'] = milepoint_path.exists()
            
            analysis.append(passage_analysis)
        
        return analysis

    def save_analysis(self, analysis):
        """Save analysis results to JSON file."""
        output_file = self.data_dir / 'passage_analysis.json'
        with open(output_file, 'w') as f:
            json.dump(analysis, f, indent=2)
        print(f"\nAnalysis saved to {output_file}")
        
        # Create summary DataFrame
        df = pd.DataFrame(analysis)
        print("\nSummary of available data:")
        print(f"Total passages analyzed: {len(df)}")
        print(f"Passages with GPX data: {df['gpx_available'].sum()}")
        print(f"Passages with milepoint data: {df['milepoints_available'].sum()}")
        
        # Save summary to CSV
        csv_file = self.data_dir / 'passage_analysis.csv'
        df.to_csv(csv_file, index=False)
        print(f"Detailed analysis saved to {csv_file}")

def main():
    analyzer = AZTPassageAnalyzer()
    
    # Scrape passage information
    passages = analyzer.scrape_passage_info()
    print(f"Found {len(passages)} passages")
    
    # Download data
    analyzer.download_passage_data(passages)
    
    # Analyze data
    analysis = analyzer.analyze_gpx_data(passages)
    
    # Save results
    analyzer.save_analysis(analysis)

if __name__ == "__main__":
    main() 