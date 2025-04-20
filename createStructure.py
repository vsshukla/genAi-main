import os

def create_project_structure(base_path="."):
    """
    Creates the specified project structure.

    Args:
        base_path (str): The root directory where the project structure will be created.
    """
    directories = [
        "brownfield-ai/apps/cli",
        "brownfield-ai/apps/web-ui",
        "brownfield-ai/apps/api-server",
        "brownfield-ai/core/analyzer",
        "brownfield-ai/core/llm_engine",
        "brownfield-ai/core/actions",
        "brownfield-ai/core/jira-integration",
        "brownfield-ai/core/repo-manager",
        "brownfield-ai/workflows/prompts",
        "brownfield-ai/scripts",
        "brownfield-ai/config",
        "brownfield-ai/tests",
    ]
    files = [
        "brownfield-ai/workflows/resolve_task.py",
        "brownfield-ai/config/settings.yaml",
        "brownfield-ai/requirements.txt",  # For Python
        "brownfield-ai/README.md",
        "brownfield-ai/package.json",      # For Node.js

    ]

    # Create the directories
    for directory in directories:
        dir_path = os.path.join(base_path, directory)
        os.makedirs(dir_path, exist_ok=True)

    # Create the files
    for file_name in files:
        file_path = os.path.join(base_path, file_name)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                pass

    print("Project structure created successfully!")

if __name__ == "__main__":
    create_project_structure()
import os

def create_app_structure(base_path="."):
    """Creates the 'brownfield-ai' application structure.

    Args:
        base_path (str, optional): The base directory where the structure
            will be created. Defaults to the current directory.
    """
    app_name = "brownfield-ai"
    full_path = os.path.join(base_path, app_name)

    # Directories to create
    directories = [
        "apps",
        "core",
        "workflows",
        "scripts",
        "config",
        "tests",
    ]

    # Create the main directory
    os.makedirs(full_path, exist_ok=True)

    # Create subdirectories
    for directory in directories:
        dir_path = os.path.join(full_path, directory)
        os.makedirs(dir_path, exist_ok=True)

    print(f"Application structure for '{app_name}' created successfully at '{full_path}'")


if __name__ == "__main__":
    create_app_structure()
