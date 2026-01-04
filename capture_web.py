#!/usr/bin/env python3
"""
Web Screenshot Tool
===================

A powerful screenshot tool for capturing full-page screenshots from:
- Local HTML files
- Live website URLs
- HTML content strings

With special handling for scroll-triggered animations.

Requirements:
    pip3 install playwright
    playwright install chromium

Usage:
    # Capture a website
    python capture_web.py https://example.com

    # Capture a website with custom output
    python capture_web.py https://example.com screenshot.png

    # Capture a website with custom width
    python capture_web.py https://example.com screenshot.png 1920

    # Capture local HTML file
    python capture_web.py design.html

    # Capture with mobile viewport
    python capture_web.py https://example.com mobile.png 390

Examples:
    python capture_web.py https://listenhub.ai
    python capture_web.py https://google.com google.png
    python capture_web.py design.html design-screenshot.png
"""

from playwright.sync_api import sync_playwright
import sys
import time
import os
import re
from datetime import datetime
from urllib.parse import urlparse


def is_url(input_string):
    """Check if input string is a URL."""
    try:
        result = urlparse(input_string)
        return all([result.scheme, result.netloc])
    except:
        return False


def generate_filename_from_url(url):
    """Generate a filename from URL."""
    parsed = urlparse(url)
    domain = parsed.netloc.replace('www.', '')
    # Clean domain name
    domain = re.sub(r'[^\w\-]', '_', domain)
    return f"{domain}_screenshot.png"


def capture_screenshot(source, output_path=None, width=1920, wait_time=3):
    """
    Capture a full-page screenshot from URL or HTML file.

    This function handles scroll-triggered animations by:
    1. Loading the page (URL or local file)
    2. Slowly scrolling through entire page to trigger animations
    3. Injecting CSS to force all elements visible
    4. Taking the full page screenshot

    Args:
        source: URL (https://...) or local HTML file path
        output_path: Path for the output PNG
        width: Viewport width in pixels (default: 1920)
        wait_time: Seconds to wait after page load (default: 3)
    """

    source_is_url = is_url(source)

    if not source_is_url and not os.path.exists(source):
        print(f"❌ Error: File not found: {source}")
        sys.exit(1)

    # Generate output path if not provided
    if output_path is None:
        if source_is_url:
            output_path = generate_filename_from_url(source)
        else:
            html_path_obj = Path(source)
            output_path = html_path_obj.stem + '-screenshot.png'

    # Convert to absolute paths
    if not source_is_url:
        source = os.path.abspath(source)
    output_path = os.path.abspath(output_path)

    source_type = "🌐 Website" if source_is_url else "📄 Local file"
    print(f"🚀 Starting screenshot capture...")
    print(f"{source_type}: {source}")
    print(f"📸 Output: {output_path}")
    print(f"📐 Width: {width}px")

    with sync_playwright() as p:
        # Launch browser
        print("\n🌐 Launching browser...")
        browser = p.chromium.launch(
            headless=True,
            args=['--no-sandbox', '--disable-setuid-sandbox']
        )

        # Create page with viewport
        page = browser.new_page(viewport={'width': width, 'height': 1080})

        # Load the page
        if source_is_url:
            page_url = source
            print(f"⏳ Loading website...")
        else:
            page_url = f'file://{source}'
            print(f"⏳ Loading local file...")

        # For websites, wait longer for all resources to load
        wait_until = 'networkidle' if source_is_url else 'domcontentloaded'

        try:
            page.goto(page_url, wait_until=wait_until, timeout=60000)
        except Exception as e:
            print(f"⚠️  Warning: Page load had issues: {e}")
            print("⏳ Continuing anyway...")

        # Wait for initial content and animations
        print(f"⏳ Waiting for content to load... ({wait_time}s)")
        time.sleep(wait_time)

        # Get page height
        try:
            page_height = page.evaluate('() => document.body.scrollHeight')
            print(f"📐 Page height: {page_height}px")
        except:
            print("⚠️  Warning: Could not determine page height")
            page_height = 10000

        # Scroll through entire page to trigger reveal animations
        print("📜 Scrolling to trigger all animations...")
        scroll_increment = 500
        scroll_steps = max(1, (page_height + scroll_increment) // scroll_increment)

        for i, scroll_pos in enumerate(range(0, page_height + scroll_increment, scroll_increment)):
            try:
                page.evaluate(f'window.scrollTo(0, {scroll_pos})')
                # Show progress for long pages
                if scroll_steps > 20 and i % (scroll_steps // 10) == 0:
                    progress = int((i / scroll_steps) * 100)
                    print(f"   Progress: {progress}%")
            except:
                pass
            time.sleep(0.05)

        # Scroll back to top
        print("⬆️  Returning to top...")
        try:
            page.evaluate('window.scrollTo(0, 0)')
        except:
            pass
        time.sleep(1)

        # Inject CSS to force all reveal elements visible
        print("✨ Ensuring all elements are visible...")
        page.add_style_tag(content='''
            /* Force all reveal animations to completed state */
            .reveal, .reveal.active {
                opacity: 1 !important;
                transform: translateY(0) !important;
            }

            /* Handle common animation patterns */
            [data-reveal], .animate-in, .fade-in,
            [data-aos], .aos-animate, .aos-init {
                opacity: 1 !important;
                transform: none !important;
            }

            /* Intersection Observer animations */
            .visible, .is-visible, .in-view,
            .is-visible, .is-in-viewport {
                opacity: 1 !important;
                transform: none !important;
            }

            /* Common lazy loading placeholders */
            [data-lazy-loaded="true"] {
                opacity: 1 !important;
            }
        ''')

        time.sleep(1)

        # Get final page dimensions
        try:
            dimensions = page.evaluate('''() => {
                const body = document.body;
                const html = document.documentElement;

                return {
                    width: Math.max(
                        body.scrollWidth,
                        body.offsetWidth,
                        html.clientWidth,
                        html.scrollWidth,
                        html.offsetWidth
                    ),
                    height: Math.max(
                        body.scrollHeight,
                        body.offsetHeight,
                        html.clientHeight,
                        html.scrollHeight,
                        html.offsetHeight
                    )
                };
            }''')
            print(f"📐 Final dimensions: {dimensions['width']} x {dimensions['height']}px")
        except:
            dimensions = {'width': width, 'height': page_height}
            print(f"📐 Using dimensions: {dimensions['width']} x {dimensions['height']}px")

        # Take screenshot
        print("📸 Capturing screenshot...")
        try:
            page.screenshot(
                path=output_path,
                full_page=True
            )
        except Exception as e:
            print(f"⚠️  Screenshot failed: {e}")
            browser.close()
            sys.exit(1)

        # Get file size
        file_size = os.path.getsize(output_path)
        file_size_mb = file_size / (1024 * 1024)

        print(f"\n✅ Screenshot saved successfully!")
        print(f"📁 Path: {output_path}")
        print(f"📏 Size: {dimensions['width']} x {dimensions['height']} pixels")
        print(f"💾 File size: {file_size_mb:.1f} MB")

        browser.close()

    return output_path


def main():
    """Command line interface."""
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    source = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    width = int(sys.argv[3]) if len(sys.argv) > 3 else 1920
    wait = int(sys.argv[4]) if len(sys.argv) > 4 else 3

    try:
        capture_screenshot(source, output_file, width, wait)
    except KeyboardInterrupt:
        print("\n\n⚠️  Screenshot cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
