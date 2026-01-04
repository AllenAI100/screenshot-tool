#!/usr/bin/env python3
"""
Advanced Usage Examples for Screenshot Tool
"""

from capture_web import capture_screenshot
import time

# Example 1: Multiple viewport sizes
print("Example 1: Capturing multiple viewports...")
url = 'https://example.com'
viewports = [
    (1920, 'desktop'),
    (1440, 'laptop'),
    (1024, 'tablet'),
    (390, 'mobile')
]

for width, name in viewports:
    print(f"  Capturing {name} view ({width}px)...")
    capture_screenshot(
        source=url,
        output_path=f'example-{name}.png',
        width=width
    )

# Example 2: Slow-loading website
print("\nExample 2: Capturing slow-loading site...")
capture_screenshot(
    source='https://example.com',
    output_path='example-slow.png',
    width=1920,
    wait_time=10  # Wait 10 seconds
)

# Example 3: Design inspiration sites
print("\nExample 3: Capturing design inspiration...")
design_sites = [
    'https://dribbble.com',
    'https://behance.net',
    'https://awwwards.com'
]

for site in design_sites:
    try:
        print(f"  Capturing {site}...")
        capture_screenshot(
            source=site,
            output_path=f'{site.replace("https://", "").replace(".", "_")}.png',
            width=1920,
            wait_time=5
        )
        time.sleep(2)  # Pause between captures
    except Exception as e:
        print(f"  ⚠️  Failed to capture {site}: {e}")

print("\n✅ Advanced examples completed!")
