---
name: screenshot-tool
description: Powerful full-page screenshot tool for websites and HTML files. Handles scroll-triggered animations, supports custom viewports (desktop/mobile), and works with both URLs and local files.
license: MIT
---

This skill provides tools for capturing high-quality full-page screenshots from websites or local HTML files, with special handling for modern web animations and scroll-triggered content.

## Use Cases

Use this skill when the user asks to:
- Capture a screenshot of a website
- Take a full-page screenshot of a webpage
- Create screenshots for documentation or presentations
- Capture responsive designs (desktop, tablet, mobile)
- Save web pages as images
- Archive website designs
- Create visual documentation
- Compare website versions
- Test responsive layouts

## Features

### URL Screenshots
- Capture any live website
- Auto-detects URL vs local file
- Handles JavaScript-heavy sites
- Customizable wait time for slow-loading pages
- Works with SPAs and modern web apps

### Local File Screenshots
- Capture HTML files without server
- Perfect for design mockups
- Works with locally saved webpages
- Fast and lightweight

### Animation Handling
- Automatically triggers scroll animations
- Forces all elements visible before capture
- Handles lazy-loaded content
- Supports Intersection Observer patterns
- Works with popular animation libraries (AOS, GSAP, etc.)

### Customization
- Desktop viewports (1920px, 1440px)
- Tablet viewports (1024px)
- Mobile viewports (390px, 414px)
- Custom wait times
- Full-page or viewport-only captures

## Quick Start

### Installation

```bash
pip3 install playwright
playwright install chromium
```

### Basic Usage

```bash
# Capture a website
python capture_web.py https://example.com

# Capture with custom output
python capture_web.py https://example.com screenshot.png

# Mobile view
python capture_web.py https://example.com mobile.png 390

# Slow-loading site
python capture_web.py https://example.com output.png 1920 10
```

### Python API

```python
from capture_web import capture_screenshot

# Basic
capture_screenshot('https://example.com')

# Advanced
capture_screenshot(
    source='https://example.com',
    output_path='screenshot.png',
    width=1920,
    wait_time=3
)
```

## Common Viewport Sizes

- **1920px** - Standard desktop
- **1440px** - Laptop
- **1024px** - Tablet (iPad)
- **390px** - Mobile (iPhone)
- **414px** - Mobile (iPhone Plus/Pro)

## Tips

1. **Slow Sites**: Increase wait time to 5-10 seconds
2. **Heavy JavaScript**: Use wait_time=10 or higher
3. **Lazy Loading**: The tool handles this automatically
4. **Blocked Content**: Some sites block headless browsers - try saving as HTML first
5. **Login Required**: Save page as HTML manually, then capture the file

## Error Handling

The tool includes comprehensive error handling for:
- Network timeouts
- Invalid URLs
- Missing files
- Browser crashes
- Screenshot failures

Errors are reported clearly with suggestions for resolution.

## Output

- **Format**: PNG (lossless quality)
- **Size**: Typically 1-5MB for full pages
- **Naming**: Auto-generated from URL or customizable
- **Dimensions**: Matches actual page size (not viewport)

## Files Included

- `capture_web.py` - Main screenshot tool (URL + local files)
- `requirements.txt` - Python dependencies
- `README.md` - Full documentation
- `examples/` - Example usage scripts
