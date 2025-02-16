#!/bin/bash

# Check if ImageMagick is installed
if ! command -v convert &> /dev/null; then
    echo "ImageMagick is not installed. Please install it first."
    echo "On macOS: brew install imagemagick"
    exit 1
fi

# Create directories if they don't exist
mkdir -p assets/images/sections
mkdir -p temp_images

# Function to process an image
process_image() {
    input=$1
    output=$2
    width=$3
    height=$4
    
    convert "$input" -resize "${width}x${height}^" \
        -gravity center -extent "${width}x${height}" \
        -quality 85 "$output"
    
    echo "Processed: $output"
}

# Process hero image if it exists in temp_images
if [ -f "temp_images/hero.jpg" ]; then
    process_image "temp_images/hero.jpg" "assets/images/azt-hero.jpg" 1920 1080
fi

# Process section images if they exist
for i in {1..9}; do
    padded_num=$(printf "%02d" $i)
    if [ -f "temp_images/section_${padded_num}.jpg" ]; then
        process_image "temp_images/section_${padded_num}.jpg" \
            "assets/images/sections/${padded_num}_$(echo $section_name | tr ' ' '_' | tr '[:upper:]' '[:lower:]').jpg" \
            800 400
    fi
done

echo "Image processing complete!" 