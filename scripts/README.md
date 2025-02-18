# Scripts Directory

This directory contains automation scripts for the AZT 2025 planning documentation.

## Changelog Automation

### update_changelog.sh
This script automatically updates the changelog whenever you make a commit. It is integrated with Git's pre-commit hook system to capture all changes.

#### Features
- Automatically adds every commit to the changelog
- Captures commit messages and file changes
- Formats entries with timestamps (PT)
- Maintains reverse chronological order
- Automatically stages changelog updates
- Includes error handling and path resolution

#### Usage
The script runs automatically with every commit. Each changelog entry includes:
- Timestamp in PT
- Commit message
- List of changed files

#### Workflow
1. Stage your files for commit (`git add`)
2. Make your commit as usual (`git commit -m "Your message"`)
3. The changelog is automatically updated with:
   - Current date and time
   - Your commit message
   - List of changed files
4. The updated changelog is included in your commit

#### Time Zone
All timestamps are in Pacific Time (PT). The script automatically adjusts for this.

#### Error Handling
The script includes robust error handling for:
- Missing changelog file
- Path resolution issues
- Git command failures
- Missing commit messages

The `update_changelog.sh` script automates the process of maintaining the project's changelog. 

### Features

- Automatically detects staged files for commit
- Maintains proper chronological order (newest entries first)
- Formats entries with timestamps and file changes
- Preserves header and footer sections
- Automatically stages changelog updates

### Error Handling

The script includes robust error handling for:
- Missing changelog file
- Unable to determine commit message
- Invalid file paths
- Sorting and formatting issues 