#!/bin/bash

for file in _sections/[0-9][0-9]_*.md; do
  # Skip if file doesn't exist
  [ -f "$file" ] || continue
  
  # Get filename and create title
  filename=$(basename "$file" .md)
  section_num=$(echo "$filename" | cut -d'_' -f1)
  section_num=$((10#${section_num}))
  title=$(echo "$filename" | cut -d'_' -f2- | tr '_' ' ' | awk '{for(i=1;i<=NF;i++)sub(/./,toupper(substr($i,1,1)),$i)}1')
  
  # Create temporary file
  temp_file="${file}.tmp"
  
  # Write new front matter
  echo "---" > "$temp_file"
  echo "layout: section" >> "$temp_file"
  echo "title: \"$title\"" >> "$temp_file"
  echo "section_number: $section_num" >> "$temp_file"
  echo "permalink: /sections/$filename/" >> "$temp_file"
  echo "---" >> "$temp_file"
  echo "" >> "$temp_file"
  
  # Append content after second --- marker
  sed -n '/^---/,/^---/!p' "$file" >> "$temp_file"
  
  # Replace original with new file
  mv "$temp_file" "$file"
done 