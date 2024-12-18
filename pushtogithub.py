import os
import subprocess

def run_command(command, cwd=None):
    """Run a shell command."""
    result = subprocess.run(command, shell=True, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command: {command}")
        print(result.stderr)
        exit(1)
    return result.stdout.strip()

def initialize_git_repo(repo_path):
    """Initialize Git repository, add all files, and commit."""
    print("Initializing Git repository...")
    run_command("git init", cwd=repo_path)
    run_command("git add .", cwd=repo_path)
    run_command('git commit -m "Initial commit"', cwd=repo_path)
    print("Git repository initialized and files committed.")

def create_github_repo(repo_name, description, private, repo_path):
    """Create GitHub repository using GitHub CLI and push local commits."""
    print("Creating GitHub repository...")
    privacy_flag = "--private" if private else "--public"
    command = f'gh repo create "{repo_name}" {privacy_flag} --description "{description}" --source=. --remote=origin --push'
    run_command(command, cwd=repo_path)
    print(f"GitHub repository '{repo_name}' created and pushed.")

def main():
    # Configuration
    GITHUB_USERNAME = "bvckd00r1337"        # Replace with your GitHub username
    REPO_NAME = "S.E.P.T"                  # Desired repository name
    DESCRIPTION = "Stock Exchange Prediction Tool" # Repository description
    PRIVATE = True                           # Set to True for a private repo

    # Current working directory
    repo_path = os.getcwd()

    # Initialize Git repository
    initialize_git_repo(repo_path)

    # Create and push to GitHub repository
    full_repo_name = f"{GITHUB_USERNAME}/{REPO_NAME}"
    create_github_repo(full_repo_name, DESCRIPTION, PRIVATE, repo_path)

if __name__ == "__main__":
    main()