# AZT 2025 Thru-Hike Plan

Personal planning documentation for my Arizona Trail thru-hike starting March 15, 2025. Built with Jekyll and hosted on GitHub Pages.

## Site Overview

This site serves as a comprehensive planning tool for my upcoming Arizona Trail thru-hike. It separates data from presentation, using Jekyll's data files and templates to create a maintainable and flexible planning resource.

### Key Features
- Section-by-section trail breakdown with daily planning
- Interactive elevation profiles
- Detailed gear lists with weight calculations
- Water and resupply strategies
- Dynamic countdown to start date
- Mobile-responsive design

## Directory Structure

### Content Pages (`_pages/`)
- `gear-list.md`: Complete gear inventory with weights
- `food-plan.md`: Resupply and nutrition strategy
- `water-strategies.md`: Water management and sources
- `pre-departure-checklist.md`: Final preparation tasks
- `packing-your-backpack.md`: Personal packing system
- `resources.md`: Curated list of planning resources

### Trail Sections (`_sections/`)
- Individual markdown files for each trail section
- Consistent template structure
- Daily mileage and camping recommendations
- Water sources and resupply points
- Elevation data and key landmarks

### Data Files (`_data/`)
- `trail_stats.yml`: Core trail statistics and timeline
- `gear.yml`: Detailed gear inventory with weights
- `sections.yml`: Section-specific data
- `permits.yml`: Permit requirements and details
- `resupply.yml`: Town and resupply information
- `water.yml`: Water source data

### Layouts (`_layouts/`)
- `default.html`: Base template
- `page.html`: Standard page layout
- `section.html`: Trail section template with elevation profile

### Assets
- `assets/css/`: Stylesheets including `gear-list.css`
- `assets/images/elevation/`: Generated elevation profiles
- `assets/js/`: JavaScript utilities

### Scripts
- `start.sh`: Local development server startup
  ```bash
  ./start.sh  # Runs Jekyll with development config and livereload
  ```
- `scripts/generate_elevation_profiles.py`: Creates elevation visualizations
  ```bash
  python scripts/generate_elevation_profiles.py
  ```
- `scripts/check_deploy.sh`: Monitors deployment status
  ```bash
  ./scripts/check_deploy.sh  # Polls GitHub Actions status
  ```
- `scripts/update_changelog.sh`: Maintains automated changelog

## Data Organization

The site emphasizes separation of data and presentation:

1. **Trail Data**: Core statistics, distances, and timelines in `_data/trail_stats.yml`
2. **Equipment**: Comprehensive gear list in `_data/gear.yml`
3. **Locations**: Town and resupply info in `_data/resupply.yml`
4. **Regulations**: Permit requirements in `_data/permits.yml`

This structure allows for easy updates and maintenance while keeping content pages focused on presentation and analysis.

## Local Development

1. Install dependencies:
   ```bash
   bundle install
   ```

2. Start development server:
   ```bash
   ./start.sh
   ```

3. View site at `http://localhost:4000`

### Configuration
- `_config.yml`: Production settings
- `_config_development.yml`: Local development overrides

## Deployment

The site is automatically deployed to GitHub Pages on push to main:

1. Push changes:
   ```bash
   git add .
   git commit -m "Description of changes"
   git push origin main
   ```

2. Monitor deployment:
   ```bash
   ./scripts/check_deploy.sh
   ```

3. View live site at: https://dremy.github.io/AZT_2025/

## Changelog Management

Changes are automatically tracked via Git hooks:

1. Enable automatic changelog updates:
   ```bash
   chmod +x scripts/update_changelog.sh
   cp scripts/update_changelog.sh .git/hooks/prepare-commit-msg
   ```

2. Each commit automatically updates the changelog with:
   - Timestamp
   - Author
   - Description
   - Files changed

## Contributing

This is a personal planning site, but if you notice any errors or have suggestions:

1. Open an issue describing the problem or suggestion
2. Fork the repository
3. Create a branch for your changes
4. Submit a pull request

## License

© 2024 Dave Remy. All rights reserved.

# Arizona Trail 2025 Data Project

This repository contains tools and data for managing Arizona Trail (AZT) passage information from official sources.

## Project Structure

```
.
├── README.md                  # This file
├── _data/
│   └── passages.yml          # Combined passage data from all sources
├── data/
│   ├── cache/                # Cached data from external sources
│   │   └── azt_polyline.geojson  # AZGEO trail geometry data
│   └── passages/             # Individual passage data files
└── scripts/
    └── azt_official_data/    # Scripts for fetching and combining official data
        ├── README.md         # Detailed documentation of the data scripts
        ├── requirements.txt  # Python package dependencies
        ├── update_passages.py  # Main script to update passages.yml
        └── utils/            # Utility modules for data processing
            ├── ata_parser.py   # Parser for ATA website data
            ├── azgeo_parser.py # Parser for AZGEO geographic data
            └── yaml_writer.py  # YAML file writer with attribution
```

## Data Sources

The project combines data from two authoritative sources:

1. **Arizona Trail Association (ATA)**
   - Official passage information, maps, and resources
   - Source: https://aztrail.org/explore/passages/
   - Data includes: passage descriptions, maps, waypoints, etc.

2. **Arizona Geographic Information Council (AZGEO)**
   - Official trail geometry and passage statistics
   - Source: https://azgeo-open-data-agic.hub.arcgis.com/
   - Data includes: trail geometry, elevation data, passage lengths

3. **GPX Track Files**
   - Generated GPX files for each passage
   - Located in: `scripts/azt_official_data/data/gpx/`
   - Not included in git repository (regenerated as needed)
   - Total size: ~12MB for all passages

To regenerate GPX files:
```bash
# Update passages.yml and regenerate GPX files
python3 -m azt_official_data.update_passages --fetch-details
```

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AZT_2025.git
   cd AZT_2025
   ```

2. Install Python dependencies:
   ```bash
   cd scripts/azt_official_data
   pip install -r requirements.txt
   ```

3. Ensure the AZGEO data file exists at `data/cache/azt_polyline.geojson`

## Usage

The main workflow is managed by the `azt_official_data` package:

```bash
# Update passages.yml with latest data
python3 -m azt_official_data.update_passages

# Include additional passage details
python3 -m azt_official_data.update_passages --fetch-details

# Specify custom output location
python3 -m azt_official_data.update_passages --output custom/path.yml
```

See the [scripts/azt_official_data/README.md](scripts/azt_official_data/README.md) for detailed documentation of the data processing scripts.

## Data Format

The main output is `_data/passages.yml`, which combines data from all sources with proper attribution. Example structure:

```yaml
metadata:
  last_updated: "2025-02-21"
  data_sources:
    ata:
      name: "Arizona Trail Association"
      description: "Official passage information and resources"
      # ... additional metadata
    azgeo:
      name: "Arizona Geographic Information Council"
      description: "Geographic and elevation data"
      # ... additional metadata

passages:
  - number: "1"
    name: "Huachuca Mountains"
    # ... passage data with source attribution
```

## Development

The codebase follows these principles:
1. Clear separation of concerns between data sources
2. Proper source attribution for all data
3. Comprehensive logging and error handling
4. Type hints and docstrings for all functions
5. Modular architecture for easy maintenance

When contributing:
1. Follow the existing code style
2. Add tests for new functionality
3. Update documentation as needed
4. Use meaningful commit messages

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Arizona Trail Association (ATA) for maintaining the official trail resources
- Arizona Geographic Information Council (AZGEO) for providing geographic data
- All contributors to the open-source packages used in this project