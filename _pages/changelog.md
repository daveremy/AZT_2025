---
layout: page
title: Changelog
permalink: /changelog/
---

# Changelog

This page tracks significant changes and updates to the AZT 2025 planning documentation.

## Recent Changes
- February 23, 2025 11:28 - Fix Beth's Grand Canyon rim-to-rim date to May 15
Major changes:
Git:
Documentation:
Dependencies:
Add new azt_official_data package for managing trail data:
Add initial passages.yml with:
- YAML data writer with proper attribution
- Update total base weight to 207.73 oz (12.98 lbs)
- Update base weight to 13.36 lbs
- Update azt_official_data/requirements.txt with complete dependency list
- Update Still Need section
- Update Kitchen & Water total to 28.1 oz
- Update .gitignore to exclude:
- Trail segment analyzer
- Trail resources and URLs
- Simplify document requirements
- Rewrite azt_official_data/README.md with current architecture
- Remove selenium and webdriver-manager from requirements.txt
- Remove redundant navigation items given existing gear
- Remove old generate_elevation_profiles.py script (replaced by azt_official_data)
- Remove floss from list
- Remove deprecated validate_gpx_files.py as functionality is now in azt_official_data
- Passage data parser from ATA website
- Move ordered items to Small Stuff section with weights
- Mark items already acquired or ordered
- GPX track file downloader and parser
- February 23, 2025 11:26 - Add Google Maps link and update drive time for Oak Tree Canyon Trailhead
- February 23, 2025 11:24 - Add links to shakedown hikes page from index and pre-departure checklist
- February 23, 2025 09:56 - Add shakedown hike plan for Santa Rita Mountains overnight
- February 23, 2025 09:32 - Clarify Platypus bladder usage: contains dirty water that needs filtering
- February 23, 2025 08:57 - Update water bottle configuration: 2x 1L bottles in side pockets, 1L on right strap, Insta360 on left strap
- February 23, 2025 08:50 - Update pack checklist for Kakwa 55: pocket layout, strap configuration, and camera placement
- February 23, 2025 08:46 - Update packing strategy for Kakwa 55 pocket layout
- February 23, 2025 08:44 - Update Kakwa 55 description with 2025 model features
- February 23, 2025 08:35 - Fix header formatting in pack checklist page
- February 23, 2025 08:27 - Add link to interactive pack checklist from gear list
- February 23, 2025 08:25 - Add interactive pack checklist page
- February 23, 2025 08:12 - Enhance passage data handling and visualization - Move debug HTML files to system temp directory - Improve coordinate extraction with support for multiple formats (Google Maps links, DMS, decimal degrees) - Add new passages page with detailed trail info and interactive elements - Update coordinate parsing to prioritize Google Maps links over text parsing - Add comprehensive error handling and logging for coordinate extraction - Update index page to include link to passages page - Clean up changelog formatting
- February 21, 2025 18:05 - docs: update changelog with recent changes
- February 21, 2025 18:04 - chore: remove unused dependencies and old scripts
- February 21, 2025 18:03 - refactor: consolidate trail data processing and cleanup deprecated code
- February 21, 2025 12:50 - refactor: migrate to AZGEO data source - Remove old GPS analysis scripts, update dependencies, add documentation for MultiLineString and Passage 11 handling
- February 21, 2025 11:17 - feat: Add GPS data analysis script - Create script to analyze AZT passage GPS data - Add requirements file for GPS analysis dependencies
- February 21, 2025 11:12 - docs: Comprehensive update to README - Add detailed site overview and structure - Document data organization and separation - List key features and scripts - Improve development and deployment instructions
- February 21, 2025 11:06 - refactor: Remove Books section from resources page - Focus on resources directly used in guide creation
- February 21, 2025 11:04 - feat: Enhance resources page with author information - Add author names for trail guides and blogs - Include publication years for books - Add detailed descriptions of resources - Include recent trail journal examples
- February 21, 2025 11:01 - refactor: Move content to dedicated data files - Add mountain ranges to trail stats - Create permits.yml for permit requirements - Create resupply.yml for gateway communities
- February 21, 2025 10:59 - refactor: Simplify resources page to external links, move content to appropriate data files
- February 21, 2025 10:55 - feat: Add mountain ranges, permits, gear recommendations, and gateway communities from Traveling Nature Journal guide
- February 21, 2025 10:54 - feat: Add seasonal planning info and terminus logistics from USA Adventure Seeker guide
- February 21, 2025 10:52 - feat: Major content update for AZT planning - Add resources page with tools, maps, and guides - Enhance Section 1 with daily breakdowns, water info, camping details, and trail community section - Update trail statistics and timeline - Improve section template
- February 20, 2025 13:51 - fix: remove debug section from homepage
- February 20, 2025 13:47 - feat: reorganize gear list and add Garmin Fenix 6 Pro Solar
- February 20, 2025 12:56 - Refactor gear list: Restore category grouping, add Still Needed section, fix base weight calculation
- February 20, 2025 12:38 - Refactor section data structure: Move section data to _data/sections.yml and simplify section markdown files
- February 20, 2025 12:18 - Add deployment status check script
- February 20, 2025 12:16 - Add gear list CSS file
- February 20, 2025 06:00 - feat: improve gear list summary with card-based layout
- February 19, 2025 17:56 - fix: restore gear list to working version with recent updates
- February 19, 2025 17:14 - feat: Add Repair Kit section with weights
- February 19, 2025 17:07 - feat: Update gear organization and weights
- February 19, 2025 16:43 - feat: Update Still Need section with specific recommendations
- February 19, 2025 16:23 - feat: Update Still Need section with detailed categories
- February 19, 2025 16:21 - feat: Add waterproof matches as backup fire starter
- February 19, 2025 16:20 - feat: Add zip-lock bags to gear list and update base weight
- February 19, 2025 15:50 - Update small items: add product links and details for trowel, Swiss Army knife, bamboo toothbrush, and travel toothpaste
- February 19, 2025 15:33 - Update changelog with recent changes
- February 18, 2025 16:43 - fix: update GitHub Pages url to correct username
- February 18, 2025 16:41 - refactor: update index page to personal note format - Add quick links and status sections, make tone more personal
- February 18, 2025 16:39 - refactor: update pre-departure checklist to personal note format - Streamline and personalize checklist items
- February 18, 2025 16:38 - refactor: update water strategies to personal note format - Simplify and personalize water management approach
- February 18, 2025 16:37 - refactor: update food plan to personal note format - Reorganize content with note-to-self style and practical sections
- February 18, 2025 16:35 - refactor: update packing guide to personal note format - Convert to note-to-self style while maintaining essential information
- February 18, 2025 16:30 - Update gear list with accurate weights and sleep system details - Added specific weights for Performance Bike gloves, updated sleep system with HH tech shirt and NB shorts, added Injinji liner socks, updated calculations
- February 18, 2025 07:16 - Document prepare-commit-msg hook setup and usage
- February 18, 2025 07:15 - Clean up changelog and switch to prepare-commit-msg hook
- February 18, 2025 07:14 - Remove test file
- February 18, 2025 07:13 - Test pre-commit hook
- February 18, 2025 07:10 - Document changelog features and improve deduplication logic
- February 18, 2025 07:07 - Improve duplicate removal in changelog
- February 18, 2025 07:06 - Fix duplicate changelog entries
- February 18, 2025 07:02 - Regenerate clean changelog
- February 18, 2025 05:50 -   Add and improve changelog system
- February 18, 2025 05:49 - Replace Steripen with Aquamira drops and update base weight
- February 16, 2025 10:04 - Add REI Flash Carbon trekking poles and update base weight
- February 16, 2025 09:53 - Add daily ziplock packing list to food wizard
- February 16, 2025 09:50 - Add food planning wizard (work in progress)
- February 16, 2025 09:35 - Fix daily mileage calculation in food wizard
- February 16, 2025 09:32 - Add interactive food planning wizard
- February 16, 2025 09:26 - Replace navigation with theme-integrated header and dropdowns
- February 16, 2025 09:21 - Replace navigation grid with horizontal menu and submenus
- February 16, 2025 09:19 - Add main navigation grid to homepage
- February 16, 2025 09:16 - Add about page with Jeff Garmire acknowledgment and comprehensive food planning system
- February 16, 2025 09:07 - Add logistics page with transportation and resupply planning
- February 15, 2025 22:43 - Add GitHub Pages URL to README
- February 15, 2025 22:35 - Improve development setup: Add start script, remove duplicate workflow, update config for GitHub Pages
- February 15, 2025 21:41 - Initial commit: AZT 2025 Planning Site
- Expand Still Need into organized categories
- Elevation statistics calculator
- Elevation profiles and statistics
- Create dedicated Repair Kit section with estimated weights\n- Update total base weight to include repair kit\n- Mark Tenacious Tape as ordered
- Complete passage data from ATA
- Add zip-lock strategy note for organization
- Add waterproof matches (0.2 oz) to Kitchen section
- Add water source scoop to toiletries section
- Add specific product recommendations for sun protection, toiletries, and repair kit
- Add specific items needed for each category
- Add notes about additional items to consider
- Add note about Smart water bottle modification
- Add comprehensive documentation for GPX track files in README
- Add 3 gallon bags (0.6 oz) and 2 quart bags (0.2 oz) to Small Stuff section
- Access points with GPS coordinates
*Note: All times are Pacific Time (PT)*
  * Virtual environments
  * Specify version requirements
  * Size: ~12MB total
  * Regeneration instructions
  * Python build artifacts
  * Not included in git repo
  * Location: scripts/azt_official_data/data/gpx/
  * GPX track files
  * Example YAML structure
  * Development guidelines
  * Detailed data sources
  * Clear workflow instructions
  * Cache directories
  * Add scipy for elevation smoothing
  * Add geopandas and related dependencies

