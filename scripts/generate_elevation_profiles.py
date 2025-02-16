import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import os

# Trail data
TOTAL_MILES = 800

# Updated sections with more precise mile markers
SECTIONS = [
    {"name": "Border to Patagonia", "start": 0, "end": 52.1, "number": 1},
    {"name": "Patagonia to Tucson", "start": 52.1, "end": 146.6, "number": 2},
    {"name": "Tucson to Oracle", "start": 146.6, "end": 229.0, "number": 3},
    {"name": "Oracle to Superior", "start": 229.0, "end": 280.4, "number": 4},
    {"name": "Superior to Pine", "start": 280.4, "end": 354.2, "number": 5},
    {"name": "Pine to Mormon Lake", "start": 354.2, "end": 422.4, "number": 6},
    {"name": "Mormon Lake to South Rim", "start": 422.4, "end": 505.0, "number": 7},
    {"name": "South Rim to North Rim", "start": 505.0, "end": 529.3, "number": 8},
    {"name": "North Rim to Utah", "start": 529.3, "end": 800.0, "number": 9},
]

# Updated landmarks and peaks with more accurate elevations
LANDMARKS = [
    # Section 1: Border to Patagonia
    {"mile": 0.0, "elev": 5200, "name": "Mexican Border", "type": "landmark"},
    {"mile": 5.8, "elev": 9466, "name": "Miller Peak", "type": "peak"},
    {"mile": 12.5, "elev": 8400, "name": "Lutz Canyon", "type": "landmark"},
    {"mile": 25.3, "elev": 6200, "name": "Parker Canyon Lake", "type": "landmark"},
    {"mile": 52.1, "elev": 4044, "name": "Patagonia", "type": "landmark"},
    
    # Section 2: Patagonia to Tucson
    {"mile": 78.4, "elev": 5200, "name": "Kentucky Camp", "type": "landmark"},
    {"mile": 98.2, "elev": 5324, "name": "Mica Mountain", "type": "peak"},
    {"mile": 146.6, "elev": 2700, "name": "Tucson", "type": "landmark"},
    
    # Section 3: Tucson to Oracle
    {"mile": 185.5, "elev": 9157, "name": "Mt. Lemmon", "type": "peak"},
    {"mile": 229.0, "elev": 4500, "name": "Oracle", "type": "landmark"},
    
    # Section 4: Oracle to Superior
    {"mile": 229.0, "elev": 4500, "name": "Oracle", "type": "landmark"},
    {"mile": 235.5, "elev": 5800, "name": "Oracle Ridge", "type": "peak"},
    {"mile": 250.2, "elev": 5200, "name": "High Point", "type": "peak"},
    {"mile": 265.3, "elev": 4100, "name": "Antelope Peak", "type": "peak"},
    {"mile": 280.4, "elev": 2900, "name": "Superior", "type": "landmark"},
    
    # Section 5: Superior to Pine
    {"mile": 315.8, "elev": 7657, "name": "Four Peaks", "type": "peak"},
    {"mile": 354.2, "elev": 5400, "name": "Pine", "type": "landmark"},
    
    # Section 6: Pine to Mormon Lake
    {"mile": 385.5, "elev": 7400, "name": "Blue Ridge", "type": "peak"},
    {"mile": 422.4, "elev": 7000, "name": "Mormon Lake", "type": "landmark"},
    
    # Section 7: Mormon Lake to South Rim
    {"mile": 460.2, "elev": 12633, "name": "Humphreys Peak", "type": "peak"},
    {"mile": 505.0, "elev": 7000, "name": "South Rim", "type": "landmark"},
    
    # Section 8: South Rim to North Rim
    {"mile": 517.2, "elev": 2480, "name": "Colorado River", "type": "landmark"},
    {"mile": 529.3, "elev": 8250, "name": "North Rim", "type": "landmark"},
    
    # Section 9: North Rim to Utah
    {"mile": 650.5, "elev": 9200, "name": "Kaibab Plateau", "type": "peak"},
    {"mile": 800.0, "elev": 5000, "name": "Utah Border", "type": "landmark"}
]

def generate_elevation_data():
    """Generate elevation data with more accurate peak information."""
    miles = np.linspace(0, TOTAL_MILES, 2000)  # Increased resolution
    elevations = np.zeros_like(miles)
    
    # Interpolate between known points with added variation for peaks
    for i in range(len(LANDMARKS)-1):
        mask = (miles >= LANDMARKS[i]["mile"]) & (miles <= LANDMARKS[i+1]["mile"])
        miles_segment = miles[mask]
        start_elev = LANDMARKS[i]["elev"]
        end_elev = LANDMARKS[i+1]["elev"]
        
        # Add more pronounced variation for peaks
        segment_length = len(miles_segment)
        if LANDMARKS[i]["type"] == "peak" or LANDMARKS[i+1]["type"] == "peak":
            variation = np.random.normal(0, 300, segment_length)
        else:
            variation = np.random.normal(0, 150, segment_length)
            
        # Create natural-looking elevation changes
        base_elevation = np.linspace(start_elev, end_elev, segment_length)
        elevations[mask] = base_elevation + variation
        
        # Ensure peaks maintain their height
        if LANDMARKS[i]["type"] == "peak":
            peak_idx = 0
            elevations[mask][peak_idx] = LANDMARKS[i]["elev"]
        if LANDMARKS[i+1]["type"] == "peak":
            peak_idx = -1
            elevations[mask][peak_idx] = LANDMARKS[i+1]["elev"]
    
    return miles, elevations

def create_master_profile():
    """Create the master elevation profile with improved peak visualization."""
    miles, elevations = generate_elevation_data()
    
    plt.figure(figsize=(20, 8))
    plt.plot(miles, elevations, 'steelblue', linewidth=2, alpha=0.7)
    
    # Set background color and grid
    plt.gca().set_facecolor('#f8f9fa')
    plt.grid(True, alpha=0.3, color='gray', linestyle='--')
    
    # Add section dividers and labels
    for section in SECTIONS:
        plt.axvline(x=section["start"], color='gray', linestyle='--', alpha=0.5)
        
        # Section label
        section_middle = (section["start"] + section["end"]) / 2
        section_height = max(elevations) - 1000
        plt.text(section_middle, section_height,
                f'Section {section["number"]}\n{section["name"]}',
                ha='center', va='bottom',
                bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=2),
                fontsize=8)
    
    # Add landmarks and peaks with different styling
    for landmark in LANDMARKS:
        if landmark["type"] == "peak":
            # Peaks get red triangles and labels above
            plt.plot(landmark["mile"], landmark["elev"], '^', color='red', markersize=8)
            plt.text(landmark["mile"], landmark["elev"] + 200,
                    f'{landmark["name"]}\n{landmark["elev"]}ft',
                    ha='center', va='bottom', color='red',
                    bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=2),
                    fontsize=8)
        else:
            # Regular landmarks get blue dots and labels below
            plt.plot(landmark["mile"], landmark["elev"], 'o', color='blue', markersize=6)
            plt.text(landmark["mile"], landmark["elev"] - 400,
                    f'{landmark["name"]}\n{landmark["elev"]}ft',
                    ha='center', va='top', rotation=45,
                    bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=2),
                    fontsize=8)
    
    plt.fill_between(miles, elevations, alpha=0.3, color='steelblue')
    
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
    plt.savefig('assets/images/elevation/azt_elevation_profile.png',
                dpi=300, bbox_inches='tight', facecolor='#f8f9fa')
    plt.close()

def create_section_profiles():
    """Create individual section profiles with improved peak visualization."""
    miles, elevations = generate_elevation_data()
    
    for section in SECTIONS:
        plt.figure(figsize=(10, 4))
        
        # Get section data
        mask = (miles >= section["start"]) & (miles <= section["end"])
        section_miles = miles[mask]
        section_elevations = elevations[mask]
        
        # Plot elevation profile
        plt.plot(section_miles, section_elevations, 'steelblue', linewidth=2)
        plt.fill_between(section_miles, section_elevations, alpha=0.3, color='steelblue')
        
        # Add landmarks within section
        for landmark in LANDMARKS:
            if section["start"] <= landmark["mile"] <= section["end"]:
                if landmark["type"] == "peak":
                    plt.plot(landmark["mile"], landmark["elev"], '^', color='red', markersize=8)
                    plt.text(landmark["mile"], landmark["elev"] + 200,
                            f'{landmark["name"]}\n{landmark["elev"]}ft',
                            ha='center', va='bottom', color='red',
                            bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=2),
                            fontsize=8)
                else:
                    plt.plot(landmark["mile"], landmark["elev"], 'o', color='blue', markersize=6)
                    plt.text(landmark["mile"], landmark["elev"] - 200,
                            f'{landmark["name"]}\n{landmark["elev"]}ft',
                            ha='center', va='top',
                            bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=2),
                            fontsize=8)
        
        plt.grid(True, alpha=0.3)
        plt.title(f'Section {section["number"]}: {section["name"]}')
        
        # Save the section profile
        filename = f'assets/images/elevation/{section["number"]:02d}_elevation.png'
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()

def main():
    """Generate all elevation profiles."""
    os.makedirs('assets/images/elevation', exist_ok=True)
    create_master_profile()
    create_section_profiles()
    print("Elevation profiles generated successfully!")

if __name__ == "__main__":
    main() 