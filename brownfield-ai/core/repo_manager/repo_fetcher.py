# core/repo-manager/repo_fetcher.py
import os
from git import Repo

def clone_or_pull_repo(repo_url: str, branch: str = "main", dest_dir: str = "./repos") -> str:
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    local_path = os.path.join(dest_dir, repo_name)

    if os.path.exists(local_path):
        repo = Repo(local_path)
        origin = repo.remotes.origin
        origin.pull(branch)
    else:
        repo = Repo.clone_from(repo_url, local_path, branch=branch)
    
    return local_path
