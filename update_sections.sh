#!/bin/bash

# Update each section file
for file in _sections/[0-9][0-9]_*.md; do
  # Skip if file doesn't exist
  [ -f "$file" ] || continue
  
  # Get the base filename without extension
  filename=$(basename "$file" .md)
  
  # Extract section number (remove leading zero)
  section_num=$(echo "$filename" | cut -d'_' -f1)
  section_num=$((10#${section_num}))
  
  # Create title from filename (convert underscores to spaces and capitalize each word)
  title=$(echo "$filename" | cut -d'_' -f2- | tr '_' ' ' | awk '{for(i=1;i<=NF;i++)sub(/./,toupper(substr($i,1,1)),$i)}1')
  
  # Extract the content after the front matter
  content=$(awk '/^---/{p++;next} p==2{exit} p>=1{print}' "$file")
  
  # Create new file with updated front matter and preserved content
  cat > "${file}.tmp" << EOL
---
layout: section
title: "$title"
section_number: $section_num
permalink: /sections/$filename/
---

$content
EOL
  
  # Replace original file with new version
  mv "${file}.tmp" "$file"
done

# Clean up
rm -f temp_front_matter.md 2>/dev/null 