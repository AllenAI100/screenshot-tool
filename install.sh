#!/bin/bash
# Quick Install Script for Screenshot Tool

echo "🚀 Installing Screenshot Tool..."
echo ""

# Check Python version
echo "📋 Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.6 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "✅ Python $PYTHON_VERSION found"

# Install Playwright
echo ""
echo "📦 Installing Playwright..."
pip3 install playwright

# Install Chromium
echo ""
echo "🌐 Installing Chromium browser..."
playwright install chromium

# Make script executable
echo ""
echo "🔧 Setting permissions..."
chmod +x capture_web.py

# Test installation
echo ""
echo "🧪 Testing installation..."
python3 capture_web.py https://example.com

echo ""
echo "✅ Installation complete!"
echo ""
echo "Quick start:"
echo "  python3 capture_web.py https://example.com"
echo ""
echo "For more info, see README.md"
