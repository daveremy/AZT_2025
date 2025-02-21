# AZT Official Data Processor

Downloads and processes official Arizona Trail data from AZGEO to generate validated GPX files and update passage data.

## Data Source
Primary data comes from the [Arizona National Scenic Trail Polyline](https://azgeo-open-data-agic.hub.arcgis.com/datasets/azgeo::arizona-national-scenic-trail-polyline) dataset, maintained by the Arizona Geographic Information Council (AGIC) and Arizona Trail Association.

Last updated: February 14, 2025

## Usage

1. Install requirements:
```bash
pip install -r requirements.txt
```

2. Run the processor:
```bash
python process_azt_data.py
```

This will:
- Download latest trail data from AZGEO
- Generate validated GPX files in `../../data/gpx/`
- Update passage data in `../../data/passages/`

## Data Processing Details

### MultiLineString Handling
Some passages in the AZGEO data are represented as MultiLineString geometries rather than single LineStrings. This occurs when:
1. A passage has natural breaks or discontinuities
2. The trail has alternate routes or bypasses
3. The data was collected in segments

Our approach:
- Merge all segments into a single continuous LineString
- Preserve the segment order from the source data
- Log gaps between segments for verification
- Generate a single GPX file per passage

Implications:
- Pros:
  * Simpler data structure (one GPX per passage)
  * Maintains compatibility with most GPS devices
  * Easier to calculate total distances
  * Consistent with other passage formats
- Cons:
  * May create artificial connections between physically separated segments
  * Could mask natural breaks in the trail
  * Gap distances need manual verification

### Passage 11 Handling
The Santa Catalina Mountains section (Passage 11) has multiple variants in the official data:
- **Passage 11**: Main route through Pusch Ridge Wilderness
  * Traditional AZT route
  * More challenging terrain
  * Higher elevation gain/loss
  * Passes through designated wilderness area

- **Passage 11a**: Pusch Ridge Wilderness Bypass (West)
  * Alternative route west of wilderness
  * Used when wilderness permits unavailable
  * Lower elevation option
  * More accessible terrain

- **Passage 11e**: Pusch Ridge Wilderness Bypass (East)
  * Alternative route east of wilderness
  * Emergency/alternate route
  * Less commonly used
  * Connects to different trail systems

Our Processing Approach:
1. Process only the main Passage 11 route
2. Skip both 11a and 11e bypass variants
3. Generate single GPX file for Passage 11
4. Maintain consistent passage numbering

Rationale for this approach:
- **Simplicity**: Single clear route for planning
- **Authenticity**: Follows traditional AZT alignment
- **Consistency**: Matches typical thru-hiker experience
- **Data Management**: Cleaner data structure
- **Planning**: Easier to calculate distances and timelines

Implications:
- Users need wilderness permits for Pusch Ridge
- Bypass variants not included in generated data
- Distance calculations based on main route
- Section planning assumes wilderness traverse

Note: While bypass options exist and may be necessary in some cases (fire closures, permit issues, etc.), our data processing focuses on the primary AZT route. Users should consult the Arizona Trail Association website for current conditions and bypass information when needed.

### Data Structure
The processor generates three types of files:
1. GPX files in `data/gpx/`
   - One file per passage
   - Continuous track representation
   - Compatible with most GPS devices

2. YAML files in `data/passages/`
   - Passage metadata
   - Start/end coordinates
   - Official and calculated distances
   - Last update timestamp

3. Summary JSON in `data/metadata/`
   - Processing timestamp
   - Passage statistics
   - Gap analysis results

## Attribution
   - Gap analysis results 