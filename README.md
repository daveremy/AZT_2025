# AZT 2025 Thru-Hike Plan

This repository contains the planning documentation for my Arizona Trail thru-hike starting March 15, 2025. The site is built with Jekyll and hosted on GitHub Pages.

## Local Development

To run this site locally:

1. Install Ruby and Bundler
2. Clone this repository
3. Run `bundle install` to install dependencies
4. Run `bundle exec jekyll serve` to start the local server
5. Visit `http://localhost:4000/azt-2025` in your browser

## Directory Structure

- `_pages/`: Main content pages
- `_sections/`: Individual trail section plans
- `_layouts/`: HTML templates
- `assets/`: CSS, images, and other static files
- `_includes/`: Reusable HTML components
- `scripts/`: Automation scripts, including changelog generation

## Features

### Automated Changelog
The site maintains an automated changelog that tracks all significant changes. The changelog is:
- Automatically updated with each commit via Git hooks
- Includes timestamps in PT
- Maintains a clean, deduplicated history
- Can be regenerated from git history

After cloning the repository, run these commands to enable automatic changelog updates:
```bash
chmod +x scripts/update_changelog.sh
cp scripts/update_changelog.sh .git/hooks/prepare-commit-msg
chmod +x .git/hooks/prepare-commit-msg
```

See [scripts/README.md](scripts/README.md) for more details on the changelog automation.

## Contributing

This is a personal planning site, but if you notice any errors or have suggestions, please feel free to open an issue.

## License

© 2024 Dave Remy. All rights reserved.

## GitHub Pages

This site is deployed to GitHub Pages and can be accessed at: https://dremy.github.io/AZT_2025/ 