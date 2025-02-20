#!/bin/bash

echo "Checking deployment status every 15 seconds..."
echo "Press Ctrl+C to stop"
echo ""

while true; do
    # Get the latest deployment status
    status=$(curl -s https://api.github.com/repos/daveremy/AZT_2025/actions/runs | grep -m 1 '"status":' | cut -d'"' -f4)
    
    # Get the timestamp
    timestamp=$(date '+%H:%M:%S')
    
    if [ "$status" = "completed" ]; then
        echo "[$timestamp] ✅ Latest deployment completed!"
        exit 0
    elif [ "$status" = "in_progress" ]; then
        echo "[$timestamp] 🔄 Deployment in progress..."
    else
        echo "[$timestamp] ❓ Status: $status"
    fi
    
    sleep 15
done 