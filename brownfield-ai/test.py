from core.repo-manager.manager import clone_repo, load_code_files # type: ignore

repo_path = clone_repo("https://github.com/vsshukla/genAi_test_dotNet", branch="main")
files = load_code_files(repo_path)