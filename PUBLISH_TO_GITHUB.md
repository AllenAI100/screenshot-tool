# 📤 Publishing to GitHub Guide

This guide will help you publish the Screenshot Tool skill to GitHub.

## 📋 Prerequisites

- GitHub account
- Git installed locally
- GitHub CLI (optional but recommended)

## 🚀 Step-by-Step Publishing

### Step 1: Initialize Git Repository

```bash
cd /Users/allenlai/.claude/skills/screenshot-tool
git init
```

### Step 2: Create GitHub Repository

**Option A: Using GitHub CLI (Recommended)**

```bash
# Login to GitHub (first time only)
gh auth login

# Create repository
gh repo create screenshot-tool --public --source=. --remote=origin --push
```

**Option B: Manual Creation**

1. Go to https://github.com/new
2. Repository name: `screenshot-tool`
3. Description: `Powerful full-page screenshot tool for websites and HTML files`
4. Set as **Public**
5. Don't initialize with README (we already have one)
6. Click "Create repository"
7. Follow the instructions shown

### Step 3: Add Files and Make First Commit

```bash
# Add all files
git add .

# Commit
git commit -m "Initial commit: Screenshot Tool with full-page capture support

Features:
- Capture websites and local HTML files
- Handle scroll-triggered animations
- Custom viewport sizes (desktop, tablet, mobile)
- Auto-detect URL vs file input
- Comprehensive error handling
- Python API and CLI support
- Full documentation and examples"

# Add remote (if not using gh CLI)
git remote add origin https://github.com/YOUR_USERNAME/screenshot-tool.git

# Push to GitHub
git push -u origin main
```

**Note**: If your default branch is `master` instead of `main`, use `git push -u origin master`

### Step 4: Configure Repository Settings

Go to your repository on GitHub and:

1. **Settings → General**
   - Description: `🖼️ Powerful full-page screenshot tool for websites and HTML files with scroll animation support`
   - Website: `https://github.com/YOUR_USERNAME/screenshot-tool`
   - Topics: Add tags like:
     - screenshot
     - web-scraping
     - playwright
     - python
     - automation
     - web-design
     - responsive-design
     - screenshot-tool

2. **Settings → Branches**
   - Set main branch as default
   - Enable branch protection rules (optional)

3. **Settings → Actions**
   - Enable workflows (if you add CI/CD later)

### Step 5: Add Repository Badges (Optional)

Add these badges to your README.md for visibility:

```markdown
![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Playwright](https://img.shields.io/badge/Playwright-Latest-orange.svg)
```

### Step 6: Create First Release

1. Go to **Releases** → **Create a new release**
2. Tag version: `v1.0.0`
3. Release title: `v1.0.0 - Initial Release`
4. Description:

```markdown
## 🎉 First Release

Screenshot Tool v1.0.0 is now available!

### Features
- ✅ Capture any website or HTML file
- ✅ Handle scroll animations perfectly
- ✅ Custom viewport sizes (1920, 1440, 1024, 390, 414px)
- ✅ Auto-detect URL vs file input
- ✅ Python API and CLI
- ✅ Comprehensive documentation

### Installation

```bash
pip install playwright
playwright install chromium
python3 capture_web.py https://example.com
```

### What's New
- Initial public release
- Full-page screenshot support
- Animation handling
- Mobile/desktop/tablet views
- Example scripts

### Documentation
See [README.md](https://github.com/YOUR_USERNAME/screenshot-tool/blob/main/README.md) for full documentation.
```

5. Click **Publish release**

### Step 7: Add Claude Skill Integration (Optional)

If you want to use this as a Claude Code skill:

1. The repository is ready to use as a skill
2. Install via Claude Code CLI:
```bash
claude skill install https://github.com/YOUR_USERNAME/screenshot-tool
```

### Step 8: Promote Your Project

1. **Share on Social Media**
   - Twitter: "Just published my open-source screenshot tool! 🖼️"
   - LinkedIn: Professional announcement
   - Reddit: r/webdev, r/Python, r/web_scraping

2. **Add to Portfolios**
   - GitHub profile
   - Personal website
   - Resume/CV

3. **Write a Blog Post** (Optional)
   - Problem it solves
   - How it works
   - Use cases
   - Technical details

## 📝 Post-Publishing Checklist

- [ ] Repository created on GitHub
- [ ] All files pushed
- [ ] Repository settings configured
- [ ] Topics/tags added
- [ ] First release created
- [ ] README.md looks good
- [ ] Tested installation instructions
- [ ] License is correct
- [ ] Contributing guidelines present
- [ ] Shared with community

## 🔗 Useful Links

- Your repository: `https://github.com/YOUR_USERNAME/screenshot-tool`
- Git documentation: https://git-scm.com/doc
- GitHub documentation: https://docs.github.com
- GitHub CLI: https://cli.github.com

## 💡 Tips

1. **Use Semantic Versioning**: v1.0.0, v1.1.0, v2.0.0, etc.
2. **Keep CHANGELOG.md**: Track changes between releases
3. **Respond to Issues**: Engage with users quickly
4. **Review PRs Carefully**: Maintain code quality
5. **Celebrate Contributors**: Thank people who help

## 🆘 Troubleshooting

### Problem: Git push fails

```bash
# Check remote
git remote -v

# Fix remote URL
git remote set-url origin https://github.com/YOUR_USERNAME/screenshot-tool.git
```

### Problem: Permission denied

```bash
# Check SSH key or use personal access token
# Or use GitHub CLI
gh auth status
```

### Problem: Files not showing

```bash
# Check what's committed
git log --oneline

# Check what's pushed
git ls-remote origin
```

## 🎉 Congratulations!

Once published, your tool will be available to:
- GitHub community
- Claude Code users (as a skill)
- Python developers
- Web designers and developers
- Anyone who needs website screenshots

Happy publishing! 🚀
