#!/bin/bash

# Kill any running Jekyll processes
echo "Stopping any running Jekyll servers..."
pkill -f jekyll

# Wait a moment to ensure ports are freed
sleep 1

# Start Jekyll with both configs and livereload
echo "Starting Jekyll server..."
bundle exec jekyll serve --config _config.yml,_config_development.yml --livereload

# Note: The script will stay running until you press Ctrl+C 