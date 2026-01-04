#!/usr/bin/env python3
"""
Basic Usage Examples for Screenshot Tool
"""

from capture_web import capture_screenshot

# Example 1: Capture a simple website
print("Capturing example.com...")
capture_screenshot('https://example.com')

# Example 2: Capture with custom output
print("\nCapturing example.com with custom name...")
capture_screenshot(
    source='https://example.com',
    output_path='example.png'
)

# Example 3: Mobile view
print("\nCapturing mobile view of example.com...")
capture_screenshot(
    source='https://example.com',
    output_path='example-mobile.png',
    width=390
)

print("\n✅ All screenshots completed!")
print("Check the current directory for the output files.")
