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
import tempfile

import requests
from bs4 import BeautifulSoup, Tag

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Changed to DEBUG for more info
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
    """
    Extract GPS coordinates from text in various formats:
    - Google Maps link format: https://www.google.com/maps/dir/31.6001955,-110.7244627/
    - Google Maps link format: http://maps.google.com/maps?saddr=31.71873°+N,+110.75704°+W
    - Decimal degrees format: 31.33367° N, 110.28276° W
    - Degrees/minutes/seconds format: 31°36'1.23"N, 110°43'26.83"W
      Also handles curly quotes (″) and HTML entities
    - Decimal degrees in parentheses format: (31.33367, -110.28276)
    
    Returns:
    - Dictionary with 'lat' and 'lon' keys if coordinates found
    - None if no coordinates found
    """
    if not text:
        return None
        
    # Try Google Maps link format first (direct coordinates)
    maps_pattern = r'google\.com/maps/dir/(-?\d+\.\d+),(-?\d+\.\d+)/'
    maps_match = re.search(maps_pattern, text)
    if maps_match:
        lat = float(maps_match.group(1))
        lon = float(maps_match.group(2))
        return {'lat': lat, 'lon': lon}
    
    # Try Google Maps saddr format
    saddr_pattern = r'maps\?saddr=(\d+\.\d+)°\+([NS]),\+(\d+\.\d+)°\+([EW])'
    saddr_match = re.search(saddr_pattern, text)
    if saddr_match:
        lat = float(saddr_match.group(1))
        lat = lat if saddr_match.group(2) == 'N' else -lat
        lon = float(saddr_match.group(3))
        lon = -lon if saddr_match.group(4) == 'W' else lon
        return {'lat': lat, 'lon': lon}
    
    # Try decimal degrees format
    dd_pattern = r'(\d+\.\d+)°\s*([NS])\s*,\s*(\d+\.\d+)°\s*([EW])'
    dd_match = re.search(dd_pattern, text)
    if dd_match:
        lat = float(dd_match.group(1))
        lat = lat if dd_match.group(2) == 'N' else -lat
        lon = float(dd_match.group(3))
        lon = -lon if dd_match.group(4) == 'W' else lon
        return {'lat': lat, 'lon': lon}
    
    # Try degrees/minutes/seconds format with HTML entities and rendered forms
    dms_pattern = r'(\d+)°(\d+)(?:&#8217;|\')(\d+(?:\.\d+)?)(?:&#8243;|″)([NS])\s*,\s*(\d+)°(\d+)(?:&#8217;|\')(\d+(?:\.\d+)?)(?:&#8243;|″)([EW])'
    dms_match = re.search(dms_pattern, text)
    if dms_match:
        lat_deg = int(dms_match.group(1))
        lat_min = int(dms_match.group(2))
        lat_sec = float(dms_match.group(3))
        lat = lat_deg + lat_min/60 + lat_sec/3600
        lat = lat if dms_match.group(4) == 'N' else -lat
        
        lon_deg = int(dms_match.group(5))
        lon_min = int(dms_match.group(6))
        lon_sec = float(dms_match.group(7))
        lon = lon_deg + lon_min/60 + lon_sec/3600
        lon = -lon if dms_match.group(8) == 'W' else lon
        
        return {'lat': lat, 'lon': lon}
    
    # Try decimal degrees in parentheses format
    paren_pattern = r'\((\d+\.\d+)\s*,\s*-?(\d+\.\d+)\)'
    paren_match = re.search(paren_pattern, text)
    if paren_match:
        lat = float(paren_match.group(1))
        lon = float(paren_match.group(2))
        return {'lat': lat, 'lon': lon}
    
    logging.debug(f"Could not extract coordinates from text: {text}")
    return None

def find_access_point_section(soup: BeautifulSoup, point_type: str) -> Optional[Tag]:
    """Find a section containing access point information.
    
    Args:
        soup: BeautifulSoup object of the page
        point_type: 'southern' or 'northern'
        
    Returns:
        Tag containing the access point section, or None if not found
    """
    # Try different header formats
    for header in soup.find_all(['h2', 'h3', 'h4']):
        text = header.get_text().lower()
        if point_type in text and ('access' in text or 'terminus' in text or 'trailhead' in text):
            logger.debug(f"Found {point_type} access point header: {header.get_text()}")
            return header
            
    # Try looking in paragraphs
    for p in soup.find_all('p'):
        text = p.get_text().lower()
        if point_type in text and ('access' in text or 'terminus' in text or 'trailhead' in text):
            logger.debug(f"Found {point_type} access point in paragraph: {p.get_text()[:100]}...")
            return p
            
    return None

def extract_access_point_info(element: Tag, point_type: str) -> Optional[Dict]:
    """Extract access point information from an HTML element.
    
    Args:
        element: BeautifulSoup Tag containing access point info
        point_type: 'southern' or 'northern'
        
    Returns:
        Dict with access point info or None if not enough info found
    """
    # Get all text in this section until the next header
    text_blocks = []
    for sibling in element.find_next_siblings():
        if sibling.name in ['h2', 'h3', 'h4']:
            break
        text_blocks.append(sibling.get_text().strip())
    
    full_text = ' '.join(text_blocks)
    logger.debug(f"Processing {point_type} access point text: {full_text[:200]}...")
    
    # Try to find a name in the header or nearby text
    name = element.get_text().split(':', 1)[1].strip() if ':' in element.get_text() else None
    if not name:
        # Look for common name patterns
        name_match = re.search(r'([\w\s-]+(?:Trailhead|TH|Terminus|Access))', full_text)
        if name_match:
            name = name_match.group(1).strip()
    
    if not name:
        logger.warning(f"Could not find name for {point_type} access point")
        return None
        
    # Look for coordinates in href attributes first
    coords = None
    for sibling in element.find_next_siblings():
        if sibling.name in ['h2', 'h3', 'h4']:
            break
        for link in sibling.find_all('a', href=True):
            href = link['href']
            coords = extract_coordinates(href)
            if coords:
                break
        if coords:
            break
    
    # If no coordinates found in hrefs, try text content
    if not coords:
        for text in text_blocks:
            coords = extract_coordinates(text)
            if coords:
                break
    
    # Extract notes
    notes = []
    for text in text_blocks:
        # Skip coordinate lines
        if coords and any(str(c) in text for c in coords.values()):
            continue
        # Skip empty lines and headers
        if text and not text.lower().startswith(('access:', 'note:', 'gps')):
            notes.append(text)
    
    return {
        'type': point_type,
        'name': name,
        'coordinates': coords,
        'notes': notes
    }

def get_passage_details(passage: PassageResources) -> bool:
    """Get additional details about a passage from its info page."""
    logger.info(f"Fetching details for Passage {passage.number}: {passage.name}")
    
    try:
        response = requests.get(passage.info_page, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Save HTML for debugging in temp directory
        if logger.getEffectiveLevel() <= logging.DEBUG:
            debug_dir = Path(tempfile.gettempdir()) / 'azt_debug' / 'ata_pages'
            debug_dir.mkdir(parents=True, exist_ok=True)
            debug_file = debug_dir / f'passage_{passage.number}.html'
            with open(debug_file, 'w') as f:
                f.write(response.text)
            logger.debug(f"Saved debug HTML to {debug_file}")
        
        # Initialize access points list
        passage.access_points = []
        
        # Look for both southern and northern access points
        for point_type in ['southern', 'northern']:
            section = find_access_point_section(soup, point_type)
            if section:
                access_point = extract_access_point_info(section, point_type)
                if access_point:
                    passage.access_points.append(access_point)
                    logger.info(f"Added {point_type} access point: {access_point['name']}")
                    if access_point['coordinates']:
                        logger.info(f"  Coordinates: {access_point['coordinates']}")
                    if access_point['notes']:
                        logger.info(f"  Notes: {len(access_point['notes'])} items")
        
        if not passage.access_points:
            logger.warning(f"No access points found for passage {passage.number}")
            
        return True
        
    except Exception as e:
        logger.error(f"Error fetching passage {passage.number} details: {str(e)}")
        return False 