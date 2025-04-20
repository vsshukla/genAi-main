# scripts/setup_repo.py
from core.repo_manager.repo_fetcher import clone_or_pull_repo
from core.repo_manager.language_detector import detect_languages

if __name__ == "__main__":
    repo_url = input("Enter the repo URL: ")
    repo_path = clone_or_pull_repo(repo_url)
    language = detect_languages(repo_path)
    print(f"Repo language detected: {language}")
