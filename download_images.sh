#!/bin/bash

# Create directories if they don't exist
mkdir -p assets/images/sections

# Download and process hero image
curl "https://placehold.co/1920x1080/2a4b7c/ffffff.jpg?text=Arizona+Trail+Hero" -o "assets/images/azt-hero.jpg"

# Download section images
# 1. Border to Patagonia
curl "https://placehold.co/800x400/2a4b7c/ffffff.jpg?text=Border+to+Patagonia" -o "assets/images/sections/01_border_to_patagonia.jpg"

# 2. Patagonia to Tucson
curl "https://placehold.co/800x400/2a4b7c/ffffff.jpg?text=Patagonia+to+Tucson" -o "assets/images/sections/02_patagonia_to_tucson.jpg"

# 3. Tucson to Oracle
curl "https://placehold.co/800x400/2a4b7c/ffffff.jpg?text=Tucson+to+Oracle" -o "assets/images/sections/03_tucson_to_oracle.jpg"

# 4. Oracle to Superior
curl "https://placehold.co/800x400/2a4b7c/ffffff.jpg?text=Oracle+to+Superior" -o "assets/images/sections/04_oracle_to_superior.jpg"

# 5. Superior to Pine
curl "https://placehold.co/800x400/2a4b7c/ffffff.jpg?text=Superior+to+Pine" -o "assets/images/sections/05_superior_to_pine.jpg"

# 6. Pine to Mormon Lake
curl "https://placehold.co/800x400/2a4b7c/ffffff.jpg?text=Pine+to+Mormon+Lake" -o "assets/images/sections/06_pine_to_mormon_lake.jpg"

# 7. Mormon Lake to South Rim
curl "https://placehold.co/800x400/2a4b7c/ffffff.jpg?text=Mormon+Lake+to+South+Rim" -o "assets/images/sections/07_mormon_lake_to_south_rim.jpg"

# 8. South Rim to North Rim
curl "https://placehold.co/800x400/2a4b7c/ffffff.jpg?text=South+Rim+to+North+Rim" -o "assets/images/sections/08_south_rim_to_north_rim.jpg"

# 9. North Rim to Utah
curl "https://placehold.co/800x400/2a4b7c/ffffff.jpg?text=North+Rim+to+Utah" -o "assets/images/sections/09_north_rim_to_utah.jpg"

echo "Placeholder images downloaded successfully!" 