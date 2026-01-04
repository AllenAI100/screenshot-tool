# Contributing to Screenshot Tool

Thank you for your interest in contributing! This document provides guidelines for contributing to the Screenshot Tool project.

## How to Contribute

### Reporting Bugs

1. Check existing issues first
2. Create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Python version, etc.)
   - Screenshots if applicable

### Suggesting Features

1. Check if the feature already exists
2. Search for similar feature requests
3. Create a detailed issue explaining:
   - The problem you're trying to solve
   - Proposed solution
   - Alternative approaches considered
   - Use cases

### Submitting Code

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Write/update tests if applicable
5. Commit with clear messages
6. Push to your fork
7. Create a pull request

### Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and small
- Add comments for complex logic

### Commit Messages

Use clear, descriptive commit messages:

```
Good: "Add support for custom user agents"
Bad: "Update stuff"
```

## Development Setup

1. Clone your fork:
```bash
git clone https://github.com/your-username/screenshot-tool.git
cd screenshot-tool
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
playwright install chromium
```

4. Run tests:
```bash
python capture_web.py https://example.com
```

## Testing

Test your changes with:
- Different URLs (HTTP, HTTPS)
- Local HTML files
- Various viewport sizes
- Slow-loading sites
- Sites with animations
- Mobile views

## Documentation

Keep documentation in sync with code changes:
- Update README.md for user-facing changes
- Update SKILL.md for skill changes
- Add examples for new features
- Update inline code comments

## Pull Request Process

1. Ensure your code follows the project style
2. Update documentation as needed
3. Include tests if applicable
4. Update the CHANGELOG.md if it exists
5. Your PR will be reviewed and feedback provided

## Questions?

Feel free to open an issue with your question, and we'll do our best to help!

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
