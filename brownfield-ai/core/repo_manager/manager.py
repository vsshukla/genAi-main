# core/repo-manager/manager.py

import os
import git
from pathlib import Path

EXTENSIONS = {
    "python": [".py"],
    "javascript": [".js", ".jsx"],
    "typescript": [".ts", ".tsx"],
    "java": [".java"],
    "csharp": [".cs"],
    "dotnet": [".cs", ".csproj"],
}

def clone_repo(repo_url: str, branch: str = "main", dest: str = "cloned_repo") -> str:
    if os.path.exists(dest):
        return dest  # Repo already cloned
    git.Repo.clone_from(repo_url, dest, branch=branch)
    return dest

def detect_language(file_path: str) -> str:
    ext = Path(file_path).suffix
    for lang, extensions in EXTENSIONS.items():
        if ext in extensions:
            return lang
    return "unknown"

def load_code_files(base_path: str) -> list[dict]:
    code_files = []
    for root, _, files in os.walk(base_path):
        for file in files:
            file_path = os.path.join(root, file)
            lang = detect_language(file_path)
            if lang != "unknown":
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    try:
                        code = f.read()
                        code_files.append({
                            "path": file_path,
                            "language": lang,
                            "code": code
                        })
                    except Exception as e:
                        print(f"Could not read file {file_path}: {e}")
    return code_files
