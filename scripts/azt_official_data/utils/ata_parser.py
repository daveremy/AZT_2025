"""
Utilities for parsing data from the Arizona Trail Association (ATA) website.

This module provides functions for extracting passage information and details
from the official ATA website (aztrail.org).
"""

import logging
import re
from dataclasses import dataclass
from typing import Dict, List, Optional
from urllib.parse import urljoin
from pathlib import Path

import requests
from bs4 import BeautifulSoup

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
ATA_BASE_URL = "https://aztrail.org"
PASSAGES_URL = urljoin(ATA_BASE_URL, "/explore/passages/")

# Request headers to mimic a browser
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
}

@dataclass
class PassageResources:
    """Resources and metadata for an AZT passage from the ATA website."""
    number: int
    name: str
    info_page: str
    map_url: Optional[str] = None
    profile_url: Optional[str] = None
    gpx_url: Optional[str] = None
    access_points: Optional[List[Dict[str, any]]] = None

def clean_url(url: str) -> str:
    """Clean and normalize a URL."""
    if not url.startswith('http'):
        url = f"https://aztrail.org{url}"
    return url.rstrip('/')

def extract_passage_info() -> List[PassageResources]:
    """Extract passage information from the ATA passages page.
    
    Returns:
        List of PassageResources objects containing passage data
        
    Raises:
        requests.RequestException: If the ATA website request fails
        ValueError: If the page structure is invalid or missing required data
    """
    logger.info(f"Fetching passages list from {PASSAGES_URL}")
    response = requests.get(PASSAGES_URL, headers=HEADERS)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    passages = []
    
    # Find all passage headers (h3 elements)
    for h3 in soup.find_all('h3'):
        text = h3.get_text().strip()
        if not text.startswith('Passage '):
            continue
            
        try:
            # Extract passage number and name
            match = re.match(r'Passage (\d+[e]?):?\s*(.+)', text)
            if not match:
                continue
                
            num = match.group(1)
            name = match.group(2).strip()
            
            # Skip passage 11e (Pusch Ridge bypass)
            if num == '11e':
                continue
            
            # Find the list of resources that follows this header
            resource_list = h3.find_next('ul')
            if not resource_list:
                continue
            
            passage = PassageResources(
                number=int(num),
                name=name,
                info_page=''  # Will be set below
            )
            
            # Extract resources from list items
            for li in resource_list.find_all('li'):
                text = li.get_text().strip()
                links = li.find_all('a')
                
                # Handle special case of multiple maps/profiles
                if text.startswith('MAPS (2):') or text.startswith('PROFILES (2):'):
                    for link in links:
                        href = link.get('href', '')
                        link_text = link.get_text().strip()
                        if link_text == 'North':
                            if text.startswith('MAPS'):
                                passage.map_url = href
                            else:
                                passage.profile_url = href
                    continue
                
                # Handle waypoints (GPS and MP)
                if text.startswith('Waypoints:'):
                    for link in links:
                        href = link.get('href', '')
                        link_text = link.get_text().strip().upper()
                        if 'GPS' in link_text:
                            passage.gpx_url = href
                        elif 'MP' in link_text:
                            passage.gpx_url = href
                    continue
                
                # Handle single links
                link = li.find('a')
                if not link:
                    continue
                    
                href = link.get('href', '')
                text = link.get_text().strip()
                
                if 'Passage Information Page' in text:
                    passage.info_page = clean_url(href)
                elif text == 'MAP':
                    passage.map_url = href
                elif text == 'PROFILE':
                    passage.profile_url = href
                elif 'History' in text:
                    passage.gpx_url = href
            
            if passage.info_page:  # Only add if we found the info page
                passages.append(passage)
            
        except Exception as e:
            logger.warning(f"Error processing passage {text}: {e}")
            continue
    
    logger.info(f"Found {len(passages)} passages")
    return sorted(passages, key=lambda p: p.number)

def extract_coordinates(text: str) -> Optional[Dict[str, float]]:
    """Extract GPS coordinates from text.
    
    Handles formats like:
    - 31.33367° N, 110.28276° W
    - 31.33367, -110.28276
    """
    # First try the degree format
    match = re.search(r'(\d+\.\d+)°\s*N,\s*(\d+\.\d+)°\s*W', text)
    if match:
        return {
            'latitude': float(match.group(1)),
            'longitude': -float(match.group(2))  # Convert to negative for west
        }
    
    # Try decimal format
    match = re.search(r'(\d+\.\d+),\s*([-−]?\d+\.\d+)', text)
    if match:
        return {
            'latitude': float(match.group(1)),
            'longitude': float(match.group(2))
        }
    
    return None

def get_passage_details(passage: PassageResources) -> bool:
    """Get additional details about a passage from its info page."""
    logger.info(f"Fetching details for Passage {passage.number}: {passage.name}")
    
    try:
        response = requests.get(passage.info_page, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Initialize access points list
        passage.access_points = []
        
        # Look for access point headers
        for header in soup.find_all('h3'):
            header_text = header.get_text().lower()
            
            # Determine access point type
            point_type = None
            if 'southern' in header_text:
                point_type = 'southern'
            elif 'northern' in header_text:
                point_type = 'northern'
                
            if point_type:
                logger.info(f"Found {point_type} access point header: {header.get_text()}")
                
                # Get the name from the header
                name = header.get_text().split(':', 1)[1].strip() if ':' in header.get_text() else header.get_text()
                
                # Find the following ul element
                ul = header.find_next('ul')
                if not ul:
                    continue
                
                access_point = {
                    'type': point_type,
                    'name': name,
                    'coordinates': None,
                    'notes': []
                }
                
                # Process list items
                for li in ul.find_all('li'):
                    text = li.get_text().strip()
                    
                    # Look for GPS coordinates
                    if 'GPS Coordinates' in text:
                        coords = extract_coordinates(text)
                        if coords:
                            access_point['coordinates'] = coords
                    # Look for access notes
                    elif 'Access:' in text:
                        access_point['notes'].append(text.split('Access:', 1)[1].strip())
                    # Look for general notes
                    elif 'NOTE:' in text:
                        access_point['notes'].append(text.split('NOTE:', 1)[1].strip())
                    else:
                        access_point['notes'].append(text)
                
                if access_point['coordinates'] or access_point['notes']:
                    passage.access_points.append(access_point)
                    logger.info(f"Added {point_type} access point with coordinates: {access_point['coordinates']}")
        
        if not passage.access_points:
            logger.warning(f"No access points found for passage {passage.number}")
            
        return True
        
    except Exception as e:
        logger.error(f"Error fetching passage {passage.number} details: {str(e)}")
        return False 