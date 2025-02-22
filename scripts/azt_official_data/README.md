# AZT Official Data Scripts

This directory contains scripts for fetching and combining data about the Arizona Trail from official sources:

1. Arizona Trail Association (ATA) website: https://aztrail.org/explore/passages/
2. Arizona Geographic Information Council (AZGEO): https://azgeo.az.gov/

## Directory Structure

```
azt_official_data/
├── README.md                 # This file
├── __init__.py              # Package initialization
├── update_passages.py       # Main script to update passages.yml
├── data/                    # Data directory
│   ├── passages.yml        # Combined passage data
│   ├── gpx/               # Downloaded GPX track files
│   └── cache/             # Cache for AZGEO data
└── utils/
    ├── __init__.py         # Utils package initialization
    ├── ata_parser.py       # Parser for ATA website data
    ├── azgeo_parser.py     # Parser for AZGEO geographic data
    ├── gpx_downloader.py   # GPX file downloader
    ├── gpx_parser.py       # GPX file parser
    └── yaml_writer.py      # YAML file writer
```

## Workflow

The workflow to recreate the data is:

1. Download GPX track files from ATA:
```bash
python3 -m azt_official_data.utils.gpx_downloader
```

2. Update passages.yml with combined data:
```bash
python3 -m azt_official_data.update_passages
```

This will:
- Create the data directory structure if it doesn't exist
- Download GPX track files from the ATA website
- Parse elevation data from the GPX files
- Combine all data into passages.yml

## Data Sources

### ATA Website Data
The following data is fetched from the ATA website:
- Passage name and number
- Info page URL
- History document URL
- Map PDF URL
- Elevation profile URL
- Track (GPX) URL
- Waypoint files (GPS and MP)

### GPX Track Data
The following data is extracted from GPX files:
- Total distance in miles
- Elevation data (start, end, min, max)
- Total elevation gain/loss
- Average and maximum grade
- Start/end coordinates

## Output Format

The script generates a YAML file with the following structure:

```yaml
metadata:
  last_updated: '2025-02-21'
  data_sources:
    - name: Arizona Trail Association (ATA)
      description: Official passage information, maps, and resources
      url: https://aztrail.org/explore/passages/
      last_updated: '2025-02-21'

passages:
  - number: '1'
    name: Huachuca Mountains
    resources:
      info_page: https://aztrail.org/...
      history_url: https://aztrailmedia.s3...
      map_url: https://aztrailmedia.s3...
      profile_url: https://aztrailmedia.s3...
      track_url: https://aztrailmedia.s3...
      waypoints_gps_url: https://aztrailmedia.s3...
      waypoints_mp_url: https://aztrailmedia.s3...
    length_miles: 20.3
    elevation:
      start_ft: 5905.0
      end_ft: 5667.0
      min_ft: 5517.0
      max_ft: 9098.0
      total_gain_ft: 4682.0
      total_loss_ft: 4919.0
      avg_grade_pct: 11.5
      max_grade_pct: 74.8
      per_mile_ft: 11.7
    coordinates:
      start:
        lat: 31.33361
        lon: -110.28276
      end:
        lat: 31.41941
        lon: -110.4419
```

## Dependencies

Required Python packages:
- requests
- beautifulsoup4
- geopandas
- numpy
- pyyaml
- shapely

Install dependencies with:
```bash
pip install requests beautifulsoup4 geopandas numpy pyyaml shapely
```

## Development

When modifying the code:
1. Each module should have comprehensive docstrings
2. Use type hints for function parameters and return values
3. Handle errors gracefully with appropriate logging
4. Update tests when adding new functionality
5. Keep the README updated with any architectural changes 