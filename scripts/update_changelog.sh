#!/bin/bash

# Exit on error
set -e

# Get the git root directory
GIT_ROOT=$(git rev-parse --show-toplevel)
CHANGELOG_FILE="$GIT_ROOT/_pages/changelog.md"

# Function to generate the entire changelog from git history
generate_full_changelog() {
    {
        echo "---
layout: page
title: Changelog
permalink: /changelog/
---

# Changelog

This page tracks significant changes and updates to the AZT 2025 planning documentation.

## Recent Changes"
        
        # Get commit messages with dates, deduplicate based on timestamps first
        git log --pretty=format:"- %ad - %s" --date=format:"%B %d, %Y %H:%M" |
        awk '!seen[$1 $2 $3 $4 $5]++' |  # Deduplicate based on date/time components
        sort -r |                         # Sort in reverse chronological order
        sed 's/   - /- /'                # Clean up extra spaces
        
        echo -e "\n\n*Note: All times are Pacific Time (PT)*"
    } > "$CHANGELOG_FILE"
}

# Function to add a single entry
add_changelog_entry() {
    local current_date=$(git log -1 --pretty=format:"%ad" --date=format:"%B %d, %Y %H:%M")
    local commit_message="$1"
    
    # Create a new changelog with the latest entry at the top
    {
        head -n 11 "$CHANGELOG_FILE"
        echo "- $current_date - $commit_message"
        tail -n +12 "$CHANGELOG_FILE" |
        awk '!seen[$1 $2 $3 $4 $5]++' |  # Deduplicate based on date/time components
        sort -r                           # Sort in reverse chronological order
    } > "${CHANGELOG_FILE}.tmp"
    mv "${CHANGELOG_FILE}.tmp" "$CHANGELOG_FILE"
}

# Check if we should regenerate the entire changelog
if [ "$1" = "--regenerate" ]; then
    generate_full_changelog
else
    # Get the commit message
    commit_msg_file=".git/COMMIT_EDITMSG"
    if [ -f "$commit_msg_file" ]; then
        commit_message=$(cat "$commit_msg_file")
    else
        commit_message=$(ps -o command= -p $PPID | grep -o '".*"' | sed 's/"//g')
    fi

    if [ -z "$commit_message" ]; then
        echo "Error: Could not determine commit message"
        exit 1
    fi

    # Add the entry
    add_changelog_entry "$commit_message"
fi

# Stage the updated changelog
git add "$CHANGELOG_FILE"

echo "Changelog updated successfully!"
exit 0 