from collections import defaultdict

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import git
from core.repo_manager.manager import load_code_files  # Your existing function to load files
from core.llm_engine.prompts import generate_task_prompt
from core.llm_engine.llm import process_with_llm
from core.repo_manager.language_detector import detect_languages
from dotenv import load_dotenv


load_dotenv()


def clone_or_update_repo(git_url: str, local_path: str, branch: str = None):
    """
    Clone the repository if it doesn't exist or pull the latest changes.
    Checkout a specific branch if specified.
    """
    if not os.path.exists(local_path):
        print(f"Cloning the repository from {git_url} to {local_path}...")
        repo = git.Repo.clone_from(git_url, local_path)
    else:
        print(f"Repository already exists at {local_path}. Pulling the latest changes...")
        repo = git.Repo(local_path)
        repo.remotes.origin.pull()  # Pull the latest changes
    
    # Checkout the specified branch (if any)
    if branch:
        print(f"Checking out branch: {branch}")
        repo.git.checkout(branch)

    return local_path


def resolve_task(repo_input: str, branch: str = None):
    # Step 1: Check if input is a Git URL or local path
    if repo_input.startswith("http://") or repo_input.startswith("https://"):
        repo_path = clone_or_update_repo(repo_input, os.path.join(os.getcwd(), "temp_repo"), branch)
    else:
        if not os.path.exists(repo_input) or not os.path.isdir(os.path.join(repo_input, ".git")):
            print("Error: Provided local path is not a valid Git repository.")
            return
        repo_path = repo_input
        if branch:
            repo = git.Repo(repo_path)
            print(f"Checking out branch: {branch}")
            repo.git.checkout(branch)
    
    # Step 2: Load code from the repo
    code_files = load_code_files(repo_path)

    # Step 3: Detect language(s)
    language = detect_languages(repo_path)
    print(f"Detected language: {language}")

    # Step 4: Generate task prompts using LLM
    task_prompts = generate_task_prompt(code_files, language)
    tasks = process_with_llm(task_prompts)

    if not tasks:
        print("No tasks identified.")
        return

    # Step 5: Ask user what action to take for each task
    for task in tasks:
        print(f"Task: {task['description']}")
        action = input("Would you like to resolve this task? (yes/no): ")

        if action.lower() == 'yes':
            handle_task(task)

def handle_task(task: dict):
    if task['type'] == 'bug':
        fixer = BugFixer()
    elif task['type'] == 'enhancement':
        fixer = CodeEnhancer()
    elif task['type'] == 'migration':
        fixer = MigrationHandler()
    elif task['type'] == 'security_fix':
        fixer = SecurityFixer()
    else:
        print("Unknown task type.")
        return

    # Resolve the task
    fixer.resolve(task)
    print(f"Task {task['type']} resolved!")


if __name__ == "__main__":
    # Example of passing a Git repo URL or local path with an optional branch
    repo_input = "https://github.com/vsshukla/genAi_test_dotNet"  # Change this to your actual Git repo URL
    branch = "main"  # Optional: Specify the branch if needed
    resolve_task(repo_input, branch)
