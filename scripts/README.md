# Scripts Directory

This directory contains automation scripts for the AZT 2025 planning documentation.

## Changelog Automation

### update_changelog.sh
This script automatically updates the changelog whenever you make a commit. It is integrated with Git's prepare-commit-msg hook system to capture all changes.

#### Features
- Automatically adds every commit to the changelog
- Captures commit messages with timestamps (PT)
- Maintains reverse chronological order
- Removes duplicate entries
- Automatically stages changelog updates
- Includes error handling and path resolution

#### Usage
The script can be used in two ways:

1. **Automatic Mode** (via prepare-commit-msg hook)
   - Stage your files for commit (`git add`)
   - When you run `git commit`, the hook automatically:
     - Captures your commit message
     - Adds it to the changelog
     - Includes the updated changelog in your commit
   - The changelog entry is timestamped and added before the commit is finalized

2. **Manual Regeneration**
   - Run `./scripts/update_changelog.sh --regenerate` to rebuild the entire changelog from git history
   - This is useful if the changelog gets out of sync or needs cleanup
   - The regenerated changelog will be automatically staged for commit

Each changelog entry includes:
- Timestamp in PT
- Commit message

#### Installation
To set up the automatic changelog:

1. Ensure the script is executable:
   ```bash
   chmod +x scripts/update_changelog.sh
   ```

2. Set up the Git hook:
   ```bash
   cp scripts/update_changelog.sh .git/hooks/prepare-commit-msg
   chmod +x .git/hooks/prepare-commit-msg
   ```

#### Time Zone
All timestamps are in Pacific Time (PT). The script automatically adjusts for this.

#### Error Handling
The script includes robust error handling for:
- Missing changelog file
- Path resolution issues
- Git command failures
- Missing commit messages
- Invalid file paths
- Sorting and formatting issues

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