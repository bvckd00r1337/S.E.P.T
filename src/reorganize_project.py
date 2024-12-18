import os
import shutil
from pathlib import Path

def create_directories(base_path):
    directories = ["src", "docs", "tests", "data", "scripts"]
    for directory in directories:
        dir_path = base_path / directory
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {dir_path}")

def move_files(base_path):
    file_mappings = {
        "create_sept_financials.py": "src",
        "WHITEPAPER.md": "docs",
        "README.md": base_path,
        "requirements.txt": base_path
    }
    for file, folder in file_mappings.items():
        source = base_path / file
        destination = base_path / folder / file if isinstance(folder, str) else folder / file
        if source.exists():
            shutil.move(str(source), str(destination))
            print(f"Moved {file} to {folder}/")
        else:
            print(f"File {file} does not exist. Skipping.")

def delete_unnecessary_files(base_path):
    unnecessary = ["SEPT_Tool_Financials.xlsx", "venv", "__pycache__", "*.tmp", "*.log", ".vscode", ".idea"]
    for item in unnecessary:
        target = base_path / item
        if target.exists():
            if target.is_dir():
                shutil.rmtree(target)
                print(f"Deleted directory: {item}")
            else:
                target.unlink()
                print(f"Deleted file: {item}")
        else:
            print(f"Unnecessary item {item} not found. Skipping.")

def create_gitignore(base_path):
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
dist/
*.egg-info/

# IDEs
.vscode/
.idea/

# Logs and temporary files
*.log
*.tmp

# Generated files
SEPT_Tool_Financials.xlsx
"""
    with open(base_path / ".gitignore", "w") as f:
        f.write(gitignore_content.strip())
    print("Created .gitignore")

def create_readme(base_path):
    readme_content = """# S.E.P.E.T (Stock Exchange Prediction Tool)
    
## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction
S.E.P.E.T is a tool designed to assist in stock exchange predictions using advanced algorithms and data analysis.

## Installation
1. Clone the repository.
2. Navigate to the project directory.
3. Create and activate a virtual environment.
4. Install dependencies using `pip install -r requirements.txt`.

## Usage
Run the main script located in the `src` directory: 
python src/create_sept_financials.py

## Project Structure

S.E.P.T/
├── README.md
├── WHITEPAPER.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── src/
│   └── create_sept_financials.py
├── docs/
├── tests/
├── data/
└── scripts/

## Contributing
Please submit pull requests for any improvements or bug fixes.

## License
This project is licensed under the MIT License.
"""
    with open(base_path / "README.md", "w") as f:
        f.write(readme_content)
    print("Created README.md")

def create_project_explained(base_path):
    explained_content = """# S.E.P.E.T (Stock Exchange Prediction Tool) Explained

S.E.P.E.T is a software tool designed to help investors make informed decisions in the stock market. It uses advanced data analysis and prediction algorithms to provide insights into stock performance.

## Key Features
- **Data Analysis:** Processes and analyzes large sets of financial data.
- **Predictive Modeling:** Uses algorithms to predict future stock trends.
- **User-Friendly Interface:** Easy to navigate and use for both beginners and experts.

## How It Helps
By leveraging data-driven insights, S.E.P.E.T reduces the guesswork in stock investments, allowing users to make decisions based on solid predictions and thorough analysis.

## Getting Started
1. Install the necessary software as outlined in the README.
2. Run the main script to generate financial models.
3. Use the generated data to inform your investment strategies.

S.E.P.E.T aims to empower individuals with the tools needed for successful investing in the stock market.
"""
    with open(base_path / "PROJECT_EXPLAINED.md", "w") as f:
        f.write(explained_content)
    print("Created PROJECT_EXPLAINED.md")

def main():
    base_path = Path.cwd()
    print(f"Reorganizing project in: {base_path}")
    create_directories(base_path)
    move_files(base_path)
    delete_unnecessary_files(base_path)
    create_gitignore(base_path)
    create_readme(base_path)
    create_project_explained(base_path)
    print("Project reorganization complete.")

if __name__ == "__main__":
    main()