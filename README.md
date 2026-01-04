# 🖼️ Screenshot Tool

A powerful full-page screenshot tool for capturing websites and HTML files with perfect handling of scroll animations and responsive designs.

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Playwright](https://img.shields.io/badge/Playwright-Latest-orange.svg)

## ✨ Features

- 🌐 **Capture Websites** - Screenshot any live website
- 📄 **Local Files** - Capture HTML files without a server
- 🎭 **Animation Support** - Handles scroll-triggered animations perfectly
- 📱 **Responsive** - Desktop, tablet, and mobile viewports
- ⏱️ **Customizable** - Adjustable wait times for slow sites
- 🎯 **Auto-Detection** - Automatically detects URLs vs local files
- 🚀 **Fast** - Efficient headless browser capture
- 💎 **High Quality** - Lossless PNG output

## 📦 Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Install Dependencies

```bash
# Install Playwright
pip3 install playwright

# Install Chromium browser
playwright install chromium
```

That's it! You're ready to take screenshots.

## 🚀 Quick Start

### Basic Usage

```bash
# Capture a website (auto-generates filename)
python3 capture_web.py https://example.com

# Specify output filename
python3 capture_web.py https://example.com my-screenshot.png

# Desktop view (1920px wide)
python3 capture_web.py https://github.com github.png 1920

# Mobile view (390px wide)
python3 capture_web.py https://github.com github-mobile.png 390
```

### Advanced Usage

```bash
# Slow-loading website (wait 10 seconds)
python3 capture_web.py https://heavy-site.com output.png 1920 10

# Local HTML file
python3 capture_web.html design.html design-screenshot.png

# Tablet view
python3 capture_web.py https://example.com tablet.png 1024

# Larger mobile device
python3 capture_web.py https://example.com mobile-large.png 414
```

## 📖 Usage Examples

### Example 1: Capture Competitor Site

```bash
python3 capture_web.py https://competitor.com
# Output: competitor_com_screenshot.png
```

### Example 2: Mobile Preview

```bash
python3 capture_web.py https://mysite.com mobile-preview.png 390
```

### Example 3: Design Inspiration

```bash
python3 capture_web.py https://dribbble.com dribbble.png 1920
```

### Example 4: Slow JavaScript Site

```bash
python3 capture_web.py https://react-app.com output.png 1920 15
```

### Example 5: Local Design Mockup

```bash
python3 capture_web.py my-design.html design.png
```

## 🐍 Python API

```python
from capture_web import capture_screenshot

# Basic usage
capture_screenshot('https://example.com')

# With parameters
capture_screenshot(
    source='https://example.com',
    output_path='screenshot.png',
    width=1920,
    wait_time=3
)

# Mobile view
capture_screenshot(
    source='https://example.com',
    output_path='mobile.png',
    width=390,
    wait_time=5
)

# Local file
capture_screenshot('design.html', 'design.png')
```

## 📐 Viewport Sizes

| Device | Width | Use Case |
|--------|-------|----------|
| Desktop (Full) | 1920px | Standard desktop monitors |
| Desktop (Laptop) | 1440px | Laptop computers |
| Tablet | 1024px | iPad and tablets |
| Mobile (iPhone) | 390px | iPhone 12/13/14 |
| Mobile (Large) | 414px | iPhone Plus/Max models |

## 🔧 How It Works

The tool solves a common problem: modern websites use scroll-triggered animations where elements are hidden by default. Standard screenshot tools miss these elements.

**The Solution:**

1. **Load Page** - Opens URL or file in headless browser
2. **Wait** - Allows JavaScript and assets to load
3. **Scroll** - Slowly scrolls entire page to trigger animations
4. **Force Visible** - Injects CSS to ensure all elements are shown
5. **Capture** - Takes full-page screenshot
6. **Save** - Outputs high-quality PNG

This ensures **every element** is visible in the final screenshot.

## 💡 Tips

### For Slow Sites

If a site takes a long time to load:

```bash
python3 capture_web.py https://slow-site.com output.png 1920 10
#                                                                    ↑
#                                                            Wait 10 seconds
```

### For Heavy JavaScript Sites

SPAs, React apps, Vue apps often need more time:

```bash
python3 capture_web.py https://react-app.com output.png 1920 15
```

### For Sites with Lazy Loading

The tool automatically handles lazy-loaded images and content by scrolling through the entire page.

### For Blocked Content

Some sites block headless browsers (cloudflare, etc.):

**Solution:** Save the page in your browser (Cmd+S / Ctrl+S), then:

```bash
python3 capture_web.py saved-page.html screenshot.png
```

### For Login-Required Pages

The tool doesn't support authentication. Instead:

1. Log in to the site in your browser
2. Save the page as HTML (Cmd+S)
3. Capture the saved HTML file

## 🐛 Troubleshooting

### Problem: "Page load had issues"

**Not critical!** The screenshot will still be captured. Try:
- Increase wait time: `python3 capture_web.py URL output.png 1920 10`
- Check if site loads in your browser

### Problem: Screenshot is blank

The site might be blocking headless browsers:
- Increase wait time significantly
- Save page as HTML and capture the file

### Problem: Elements are missing

Increase scroll delay:
1. Edit `capture_web.py`
2. Find `time.sleep(0.05)`
3. Change to `time.sleep(0.1)` or `time.sleep(0.15)`

### Problem: Timeout error

Site is too slow or blocking:
- Increase wait time to 10-15 seconds
- Check if site loads normally in browser
- Use local HTML file approach

### Problem: Images not loading

Increase wait time to give images time to load:

```bash
python3 capture_web.py URL output.png 1920 8
```

## 📊 Output

- **Format**: PNG (lossless quality)
- **Size**: Typically 1-5MB for full pages
- **Dimensions**: Matches actual page size (not viewport)
- **Naming**: Auto-generated from URL or customizable

## 🔒 Privacy & Security

- **No Tracking**: No data is sent to external servers
- **Local Processing**: Everything runs on your machine
- **No Cloud**: Screenshots are saved locally
- **Open Source**: Fully transparent code

## 📝 Requirements

```
Python >= 3.6
playwright >= 1.40.0
Chromium browser (auto-installed by Playwright)
```

## 📄 License

MIT License - see [LICENSE.txt](LICENSE.txt) for details.

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 🌟 Use Cases

- **Competitor Analysis** - Archive competitor websites
- **Design Inspiration** - Save designs from Dribbble, Behance, etc.
- **Documentation** - Create visual documentation
- **Presentations** - Include website screenshots in decks
- **Responsive Testing** - Compare mobile vs desktop layouts
- **Regression Testing** - Compare before/after screenshots
- **Archiving** - Save web pages before they change
- **Client Work** - Share website mockups with clients

## 📞 Support

For issues, questions, or suggestions:

- Open an issue on GitHub
- Check existing issues for solutions
- Read the troubleshooting guide above

## 🎯 Roadmap

- [ ] Add PDF export option
- [ ] Support for authentication
- [ ] Batch screenshot mode
- [ ] Web UI interface
- [ ] Docker support
- [ ] CI/CD integration

## ⭐ Star This Project

If you find this tool useful, please consider starring it on GitHub!

---

**Made with ❤️ for the web development community**
