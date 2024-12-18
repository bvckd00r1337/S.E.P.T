import os
import shutil
from pathlib import Path
from datetime import datetime

def get_user_info():
    """
    Prompt the user for information to personalize the README.md.
    """
    print("\nPlease enter the following information to personalize your README.md:")
    name = input("Your Full Name: ").strip()
    email = input("Your Email Address: ").strip()
    github_username = input("Your GitHub Username: ").strip()
    linkedin_username = input("Your LinkedIn Username: ").strip()
    
    return {
        'name': name,
        'email': email,
        'github_username': github_username,
        'linkedin': linkedin_username
    }

def get_project_path():
    """
    Prompt the user to input the existing project path.
    """
    path = input("\nEnter the path to your existing SEP_Project directory (e.g., /path/to/SEP_Project): ").strip()
    return Path(path)

def create_directories(base_path):
    """
    Create the recommended project directory structure.
    """
    directories = [
        "src",
        "data",
        "docs",
        "tests",
        "scripts"
    ]
    for directory in directories:
        dir_path = base_path / directory
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {dir_path}")

def move_file(source, destination):
    """
    Move a file from source to destination.
    """
    if not source.exists():
        print(f"Source file {source} does not exist. Skipping.")
        return
    try:
        shutil.move(str(source), str(destination))
        print(f"Moved {source.name} to {destination}")
    except Exception as e:
        print(f"Error moving {source} to {destination}: {e}")

def delete_file(file_path):
    """
    Delete a specified file or directory.
    """
    try:
        if file_path.exists():
            if file_path.is_file():
                file_path.unlink()
                print(f"Deleted file: {file_path}")
            elif file_path.is_dir() and file_path.name not in ["src", "data", "docs", "tests", "scripts"]:
                shutil.rmtree(file_path)
                print(f"Deleted directory: {file_path}")
    except Exception as e:
        print(f"Error deleting {file_path}: {e}")

def create_gitignore(base_path):
    """
    Create a .gitignore file with predefined patterns.
    """
    gitignore_content = """
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Virtual environments
venv/
ENV/
env/

# Distribution / packaging
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
*.egg-info/
.installed.cfg
*.egg

# IDEs
.vscode/
.idea/

# Jupyter Notebooks
.ipynb_checkpoints/

# Generated files
SEP_Tool_Financials.xlsx

# Logs and temporary files
*.log
*.tmp
"""
    gitignore_path = base_path / ".gitignore"
    with open(gitignore_path, "w", encoding="utf-8") as f:
        f.write(gitignore_content.strip())
    print(f"Created .gitignore at {gitignore_path}")

def create_license(base_path, user_info):
    """
    Create a LICENSE file with MIT License.
    """
    current_year = datetime.now().year
    mit_license = f"""MIT License

Copyright (c) {current_year} {user_info['name']}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
    license_path = base_path / "LICENSE"
    with open(license_path, "w", encoding="utf-8") as f:
        f.write(mit_license.strip())
    print(f"Created LICENSE at {license_path}")

def create_readme(base_path, user_info):
    """
    Create a README.md file based on a template.
    """
    readme_content = f"""# S.E.P.T (Stock Exchange Prediction Tool)

![Project Logo](path/to/logo.png) <!-- Optional: Add your project logo -->

## Table of Contents

- [📖 Introduction](#-introduction)
- [🚀 Features](#-features)
- [🔧 Technologies Used](#-technologies-used)
- [📈 Financial Model](#-financial-model)
- [📂 Project Structure](#-project-structure)
- [⚙️ Installation](#️-installation)
- [💻 Usage](#-usage)
- [🧪 Testing](#-testing)
- [📝 Documentation](#-documentation)
- [🤝 Contribution](#-contribution)
- [📜 License](#-license)
- [📧 Contact](#-contact)

## 📖 Introduction

**S.E.P.T (Stock Exchange Prediction Tool)** is a SaaS platform designed to assist investors, brokers, and finance professionals in making informed investment decisions using advanced AI technologies. By leveraging Fine-tuned NLP for sentiment and news analysis and Complex GNN for risk assessment and stock price predictions, S.E.P.T offers unparalleled insights into the stock market.

## 🚀 Features

- **AI-Driven Portfolio Analysis:**
  - Interactive AI communication connected to user portfolios.
  - Customized feedback on trading choices based on analyzed movements, trends, and metrics.
  
- **Advanced Stock Insights:**
  - In-depth analysis of stock indices with superior calculation capabilities.
  - Scenario-based outcome predictions using company-specific data.
  
- **Unified Sentiment Analysis:**
  - Consolidates public sentiment data from various sources into a single dashboard.
  - Streamlines information consumption by eliminating the need to check multiple platforms.
  
- **Enterprise Integration:**
  - Seamless API integration into internal enterprise systems.
  - Enhances stock exchange analysis and decision-making processes.
  
- **Lower Barrier to Entry:**
  - Accessible to beginners and those with minimal financial education.
  - Promotes financial literacy and market participation.
  
- **Scalability:**
  - Designed for significant scalability through enterprise partnerships.
  - Potential collaborations with major entities like NYSE, Microsoft, OpenAI, and Google within five years post-launch.

## 🔧 Technologies Used

- **Backend:**
  - Python: Robust AI and data processing capabilities.
  
- **Frontend:**
  - NodeJS & ReactJS: High responsiveness and user-friendly design.
  
- **AI Technologies:**
  - Natural Language Processing (NLP): For sentiment and news analysis.
  - Graph Neural Networks (GNN): For relationship mapping and stock price predictions.
  
- **Graphical User Interface (GUI):**
  - Intuitive and interactive user interfaces for enhanced user experience.

## 📈 Financial Model

A comprehensive financial model can be found in the `SEP_Tool_Financials.xlsx` file. This model includes:

- **Revenue Estimates:** Short-term (6 months) and Long-term (5 years) projections.
- **Cost Estimates:** Development, marketing, and operational costs.
- **Profit Calculations:** Net profit and profit margins.
- **Time Estimates:** Project timeline with key milestones.
- **Graphs:** Visual representations of revenue vs. costs and profit margins.

## 📂 Project Structure

```
SEP_Project/
├── README.md
├── WHITEPAPER.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── src/
│   └── create_sep_financials.py
├── data/
│   └── (Any raw or processed data files, if applicable)
├── docs/
│   └── (Additional documentation)
├── tests/
│   └── test_create_sep_financials.py
└── scripts/
    └── (Any additional utility scripts)
```

## ⚙️ Installation

### 1. Clone the Repository

```
git clone https://github.com/{user_info['github_username']}/SEP_Project.git
cd SEP_Project
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```
python3 -m venv venv
```

### 3. Activate the Virtual Environment

- **On macOS/Linux:**

  ```bash
  source venv/bin/activate
  ```

- **On Windows:**

  ```bash
  venv\Scripts\activate
  ```

### 4. Install Dependencies

```
pip install --upgrade pip
pip install -r requirements.txt
```

## 💻 Usage

### Generating the Financial Model

To generate the `SEP_Tool_Financials.xlsx` file, navigate to the `src/` directory and run the script:

```
cd src
python create_sep_financials.py
```

Upon successful execution, the `SEP_Tool_Financials.xlsx` file will be created in the current directory.

### Scripts Overview

- **create_sep_financials.py:**
  - Generates the financial model Excel file with structured data and basic charts.

### Running Tests

Ensure you're in the project's root directory and that the virtual environment is activated.

```
cd tests
python -m unittest test_create_sep_financials.py
```

*(Ensure that `test_create_sep_financials.py` contains appropriate test cases.)*

## 🧪 Testing

A `tests/` directory is included to house all test scripts. Utilize Python's `unittest` framework or other testing libraries like `pytest` to write and execute tests, ensuring code reliability and functionality.

## 📝 Documentation

Additional documentation is available in the `docs/` directory, including:

- **WHITEPAPER.md:** Detailed overview of the project, technical stack, and future roadmap.
- **User Guides:** Instructions on using various features of S.E.P.T.
- **API Documentation:** (If applicable) Endpoints, request/response formats, and authentication details.
  
For comprehensive insights, refer to the [WHITEPAPER.md](docs/WHITEPAPER.md).

## 🤝 Contribution

Contributions are welcome! Whether you're fixing bugs, improving documentation, or adding new features, your input is valuable.

### Steps to Contribute:

1. **Fork the Repository**
2. **Create a New Branch**

   ```bash
   git checkout -b feature/YourFeatureName
   ```

3. **Make Your Changes**
4. **Commit Your Changes**

   ```bash
   git commit -m "Add Your Feature"
   ```

5. **Push to Your Fork**

   ```bash
   git push origin feature/YourFeatureName
   ```

6. **Create a Pull Request**

Please ensure your contributions adhere to the project's coding standards and include appropriate tests.

## 📜 License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute it as per the license terms.

## 📧 Contact

For any inquiries, suggestions, or support, please reach out to:

- **Name:** {user_info['name']}
- **Email:** {user_info['email']}
- **LinkedIn:** [{user_info['linkedin']}](https://www.linkedin.com/in/{user_info['linkedin']}/)
- **GitHub:** [{user_info['github_username']}](https://github.com/{user_info['github_username']})

---
"""

    readme_path = base_path / "README.md"
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"Created README.md at {readme_path}")

def main():
    print("=== SEP_Project Reorganization Script ===")
    
    # Get user information
    user_info = get_user_info()
    
    # Get existing project path
    existing_project_path = get_project_path()
    
    if not existing_project_path.exists() or not existing_project_path.is_dir():
        print(f"The path {existing_project_path} does not exist or is not a directory.")
        return
    
    # Define new project path
    parent_dir = existing_project_path.parent
    new_project_path = parent_dir / "SEP_Project"
    
    if new_project_path.exists():
        print(f"Directory {new_project_path} already exists. Please remove it or choose a different location.")
        return
    
    # Create new project directory
    new_project_path.mkdir(parents=True, exist_ok=True)
    print(f"Created new project directory: {new_project_path}")
    
    # Create subdirectories
    create_directories(new_project_path)
    
    # Move essential files
    essential_files = {
        "create_sep_financials.py": "src",
        "WHITEPAPER.md": "docs",
        "README.md": new_project_path,
        "LICENSE": new_project_path,
        "requirements.txt": new_project_path
    }
    
    for file_name, destination in essential_files.items():
        source = existing_project_path / file_name
        if destination == new_project_path:
            dest = new_project_path / file_name
        else:
            dest = new_project_path / destination / file_name
        move_file(source, dest)
    
    # Delete non-essential files
    non_essential_files = [
        "SEP_Tool_Financials.xlsx",
        "venv",
        "env",
        "__pycache__",
        "*.tmp",
        "*.log",
        ".vscode",
        ".idea"
    ]
    
    for item in non_essential_files:
        path = existing_project_path / item
        delete_file(path)
    
    # Create .gitignore
    create_gitignore(new_project_path)
    
    # Create LICENSE
    create_license(new_project_path, user_info)
    
    # Create README.md
    create_readme(new_project_path, user_info)
    
    print("\n=== Reorganization Complete ===")
    print(f"Your reorganized project is located at: {new_project_path}")

if __name__ == "__main__":
    main()