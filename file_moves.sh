#!/bin/bash

# Create necessary directories if they don't exist
mkdir -p _sections _pages

# Move main content pages to _pages
mv overall_plan.md _pages/overall-plan.md
mv water_strategies.md _pages/water-strategies.md
mv pre_departure_checklist.md _pages/pre-departure-checklist.md
mv immediate_actions.md _pages/immediate-actions.md

# Move section plans to _sections
mv section_plans/* _sections/

# Add front matter to pages if needed
for file in _pages/*.md; do
  if ! grep -q "^---" "$file"; then
    title=$(basename "$file" .md | tr '-' ' ' | awk '{for(i=1;i<=NF;i++)sub(/./,toupper(substr($i,1,1)),$i)}1')
    sed -i '' "1i\\
---\\
layout: page\\
title: $title\\
---\\
\\
" "$file"
  fi
done

# Add front matter to sections if needed
for file in _sections/*.md; do
  if ! grep -q "^---" "$file"; then
    title=$(basename "$file" .md | tr '-' ' ' | awk '{for(i=1;i<=NF;i++)sub(/./,toupper(substr($i,1,1)),$i)}1')
    sed -i '' "1i\\
---\\
layout: section\\
title: $title\\
---\\
\\
" "$file"
  fi
done 