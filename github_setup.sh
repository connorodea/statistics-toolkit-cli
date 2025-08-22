#!/bin/bash

# Complete GitHub Repository Setup for Statistics Toolkit CLI
# Username: connorodea
# Repository: statistics-toolkit-cli

# =============================================================================
# STEP 1: Prepare the Repository Locally
# =============================================================================

echo "📁 Setting up local Git repository..."

# Make sure you're in the project directory
cd statistics-toolkit-cli

# Create a proper .gitignore file
cat > .gitignore << 'EOF'
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Virtual environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# User data
.statstoolkit/

# Matplotlib cache
.matplotlib/

# Jupyter Notebook
.ipynb_checkpoints

# pyenv
.python-version

# Log files
*.log
EOF

# Create LICENSE file
cat > LICENSE << 'EOF'
MIT License

Copyright (c) 2024 Connor O'Dea

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOF

# Update README.md with GitHub-specific content
cat > README.md << 'EOF'
# Statistics Toolkit CLI 📊

> A comprehensive command-line statistics learning and analysis tool with step-by-step explanations

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub issues](https://img.shields.io/github/issues/connorodea/statistics-toolkit-cli)](https://github.com/connorodea/statistics-toolkit-cli/issues)

## 🎯 Overview

Transform your terminal into a comprehensive statistics education platform! This toolkit provides step-by-step explanations for statistical concepts, making it perfect for students, educators, and anyone who wants to understand the "why" behind statistical calculations.

## ✨ Features

- **📈 Descriptive Statistics**: Mean, median, mode, variance, standard deviation, five-number summary, outlier detection
- **🧪 Hypothesis Testing**: One-sample and two-sample t-tests with complete explanations
- **📊 Data Visualization**: Histograms, box plots, scatter plots with statistical overlays
- **💾 Data Management**: CSV import/export, save/load datasets
- **🎓 Educational Focus**: Every calculation shows mathematical steps and reasoning
- **🖥️ Interactive CLI**: User-friendly menu-driven interface

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/connorodea/statistics-toolkit-cli.git
cd statistics-toolkit-cli

# Install dependencies
pip install -r requirements.txt

# Run the toolkit
python stats_cli.py
```

### One-Line Setup

```bash
curl -sSL https://raw.githubusercontent.com/connorodea/statistics-toolkit-cli/main/setup_stats_toolkit.sh | bash
```

## 📖 Usage Examples

### Interactive Menu
```bash
python stats_cli.py
```

### Sample Data Demo
```bash
python stats_cli.py --demo
```

### Quick Analysis
```
Enter values: 85 92 78 88 95 82 79 91 87 84

=== MEASURES OF CENTER ===
Sample size: n = 10
MEAN CALCULATION:
x̄ = Σx/n = 861/10 = 86.1000

MEDIAN CALCULATION:
Sorted data: [78 79 82 84 85 87 88 91 92 95]
n is even: median = (85 + 87)/2 = 86.0000
```

## 🎓 Educational Philosophy

This toolkit is designed for **learning statistics**, not just computing answers. Every calculation shows:

- 📝 **The formula being used**
- 🔢 **Step-by-step substitution of values**  
- 📊 **Intermediate calculations**
- 💡 **Interpretation of results**
- ✅ **Assumption checking**

## 📁 Project Structure

```
statistics-toolkit-cli/
├── stats_cli.py              # Main application
├── requirements.txt          # Python dependencies
├── setup.py                  # Package installation
├── Makefile                  # Development commands
├── examples/
│   ├── data/                 # Sample CSV datasets
│   └── create_sample_data.py # Generate sample data
├── tests/
│   └── test_basic.py         # Unit tests
└── docs/                     # Documentation
```

## 🛠️ Development

### Setup Development Environment
```bash
# Clone and setup
git clone https://github.com/connorodea/statistics-toolkit-cli.git
cd statistics-toolkit-cli

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install as editable package
pip install -e .
```

### Available Commands
```bash
make run          # Run the CLI tool
make demo         # Run sample data demo
make test         # Run tests
make sample-data  # Generate sample datasets
make clean        # Clean build artifacts
make help         # Show all commands
```

### Running Tests
```bash
python -m pytest tests/ -v
# or
make test
```

## 📊 Sample Datasets

The toolkit includes sample datasets for practice:

- **`test_scores.csv`** - Student academic performance data
- **`sales_data.csv`** - Business sales and advertising data  
- **`study_vs_scores.csv`** - Study time vs exam performance

Generate fresh sample data:
```bash
make sample-data
```

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**
4. **Add tests** for new functionality
5. **Run tests**: `make test`
6. **Commit your changes**: `git commit -m 'Add amazing feature'`
7. **Push to the branch**: `git push origin feature/amazing-feature`
8. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guidelines
- Add docstrings to new functions
- Include tests for new features
- Update README if adding major features
- Maintain the educational focus of explanations

## 🐛 Issues & Support

- **Bug Reports**: [Create an issue](https://github.com/connorodea/statistics-toolkit-cli/issues/new?template=bug_report.md)
- **Feature Requests**: [Create an issue](https://github.com/connorodea/statistics-toolkit-cli/issues/new?template=feature_request.md)
- **Questions**: [Start a discussion](https://github.com/connorodea/statistics-toolkit-cli/discussions)

## 📚 Documentation

- [Installation Guide](docs/installation.md)
- [User Manual](docs/user_manual.md)
- [Developer Guide](docs/developer_guide.md)
- [API Reference](docs/api_reference.md)

## 🏆 Inspiration

Originally inspired by TI-84 calculator programs, this toolkit brings the same step-by-step educational approach to modern Python development, making statistics accessible and understandable for everyone.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built for statistics education and learning
- Inspired by the need for transparent statistical calculations
- Designed to complement traditional statistics textbooks and courses

---

**Made with ❤️ for statistics education**

[![GitHub stars](https://img.shields.io/github/stars/connorodea/statistics-toolkit-cli?style=social)](https://github.com/connorodea/statistics-toolkit-cli/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/connorodea/statistics-toolkit-cli?style=social)](https://github.com/connorodea/statistics-toolkit-cli/network/members)
EOF

# Initialize git repository
echo "🔧 Initializing Git repository..."
git init

# Add all files
echo "📁 Adding files to Git..."
git add .

# Initial commit
echo "💾 Making initial commit..."
git commit -m "🎉 Initial commit: Statistics Toolkit CLI

✨ Features:
- Complete educational statistics toolkit
- Step-by-step explanations for all calculations
- Interactive CLI with menu navigation
- Descriptive statistics with detailed breakdowns
- Hypothesis testing with full procedure
- CSV data import/export capabilities
- Sample datasets for practice
- Comprehensive test suite

🎓 Educational focus: Shows mathematical reasoning behind every calculation
📊 Perfect for students, educators, and statistics learners"

echo "✅ Local repository setup complete!"

# =============================================================================
# STEP 2: Create GitHub Repository and Push
# =============================================================================

echo ""
echo "🚀 Setting up GitHub repository..."

# Check if GitHub CLI is installed
if command -v gh &> /dev/null; then
    echo "📱 GitHub CLI detected! Creating repository..."
    
    # Create repository using GitHub CLI
    gh repo create statistics-toolkit-cli \
        --public \
        --description "📊 A comprehensive command-line statistics learning tool with step-by-step explanations" \
        --homepage "https://github.com/connorodea/statistics-toolkit-cli" \
        --add-readme=false
    
    # Add remote origin
    git remote add origin https://github.com/connorodea/statistics-toolkit-cli.git
    
    # Push to GitHub
    git branch -M main
    git push -u origin main
    
    echo ""
    echo "🎉 Repository created and pushed successfully!"
    echo "🔗 Repository URL: https://github.com/connorodea/statistics-toolkit-cli"
    
else
    echo ""
    echo "⚠️  GitHub CLI not found. Please create repository manually:"
    echo ""
    echo "MANUAL SETUP STEPS:"
    echo "==================="
    echo ""
    echo "1. 🌐 Go to: https://github.com/new"
    echo ""
    echo "2. 📝 Fill in repository details:"
    echo "   - Repository name: statistics-toolkit-cli"
    echo "   - Description: 📊 A comprehensive command-line statistics learning tool with step-by-step explanations"
    echo "   - ✅ Public repository"
    echo "   - ❌ Do NOT initialize with README (we already have one)"
    echo "   - ❌ Do NOT add .gitignore (we already have one)"
    echo "   - ❌ Do NOT add license (we already have one)"
    echo ""
    echo "3. 🔘 Click 'Create repository'"
    echo ""
    echo "4. 💻 Run these commands in your terminal:"
    echo ""
    echo "   git remote add origin https://github.com/connorodea/statistics-toolkit-cli.git"
    echo "   git branch -M main"
    echo "   git push -u origin main"
    echo ""
fi

# =============================================================================
# STEP 3: Setup Additional GitHub Features
# =============================================================================

echo ""
echo "🔧 Additional GitHub setup recommendations..."

# Create issue templates directory
mkdir -p .github/ISSUE_TEMPLATE

# Bug report template
cat > .github/ISSUE_TEMPLATE/bug_report.md << 'EOF'
---
name: Bug report
about: Create a report to help us improve
title: '[BUG] '
labels: bug
assignees: ''

---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Run command '...'
2. Select option '....'
3. Enter data '....'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Error output**
If applicable, paste the error output here.

**Environment (please complete the following information):**
 - OS: [e.g. Ubuntu 20.04, Windows 10, macOS]
 - Python Version: [e.g. 3.9.5]
 - Package Versions: [run `pip list` for installed packages]

**Additional context**
Add any other context about the problem here.
EOF

# Feature request template
cat > .github/ISSUE_TEMPLATE/feature_request.md << 'EOF'
---
name: Feature request
about: Suggest an idea for this project
title: '[FEATURE] '
labels: enhancement
assignees: ''

---

**Is your feature request related to a problem? Please describe.**
A clear and concise description of what the problem is. Ex. I'm always frustrated when [...]

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
A clear and concise description of any alternative solutions or features you've considered.

**Educational value**
How would this feature help people learn statistics better?

**Additional context**
Add any other context or screenshots about the feature request here.
EOF

# Create pull request template
cat > .github/pull_request_template.md << 'EOF'
## Description
Brief description of changes made

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update
- [ ] Educational content improvement

## Testing
- [ ] Tests pass locally
- [ ] New tests added for new functionality
- [ ] Manual testing completed

## Educational Impact
How do these changes improve the learning experience?

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Documentation updated if needed
- [ ] Changes maintain step-by-step educational approach
EOF

# GitHub Actions workflow for testing
mkdir -p .github/workflows

cat > .github/workflows/test.yml << 'EOF'
name: Tests

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, '3.10', 3.11]

    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pytest pytest-cov
    
    - name: Run tests
      run: |
        python -m pytest tests/ -v --cov=stats_cli
    
    - name: Test CLI functionality
      run: |
        python stats_cli.py --demo
EOF

# Add the GitHub-specific files to git
git add .github/
git add .gitignore
git add LICENSE
git add README.md

git commit -m "📝 Add GitHub repository setup

🔧 Added:
- Issue templates for bugs and features
- Pull request template
- GitHub Actions workflow for testing
- Updated README with GitHub-specific content
- MIT License
- Comprehensive .gitignore

🎯 Repository is now ready for collaboration and contributions!"

echo ""
echo "📋 Repository setup summary:"
echo "=============================="
echo ""
echo "✅ Local Git repository initialized"
echo "✅ All files added and committed"
echo "✅ GitHub templates created"
echo "✅ GitHub Actions workflow added"
echo "✅ README.md with badges and documentation"
echo "✅ MIT License added"
echo "✅ .gitignore configured"
echo ""

if command -v gh &> /dev/null; then
    echo "✅ GitHub repository created automatically"
    echo "✅ Code pushed to GitHub"
    echo ""
    echo "🔗 Your repository: https://github.com/connorodea/statistics-toolkit-cli"
    
    # Push the additional commits
    git push origin main
    
else
    echo "⏳ Manual GitHub repository creation required"
    echo "   (Follow the manual steps above)"
    echo ""
fi

echo ""
echo "🎉 SETUP COMPLETE!"
echo ""
echo "🚀 Next steps:"
echo "  1. Visit your repository: https://github.com/connorodea/statistics-toolkit-cli"
echo "  2. Add repository topics: statistics, education, cli, python, mathematics"
echo "  3. Enable GitHub Pages if you want documentation hosting"
echo "  4. Star your own repo to show it's ready! ⭐"
echo ""
echo "📢 Share your project:"
echo "  - Tweet about it with #StatisticsEducation #Python #OpenSource"
echo "  - Post in r/Python and r/statistics"
echo "  - Share with your classmates and teachers!"
echo ""
echo "💡 Pro tips:"
echo "  - Add more sample datasets in examples/data/"
echo "  - Create tutorials in docs/ folder"
echo "  - Add more statistical tests and visualizations"
echo "  - Consider adding Jupyter notebook examples"
