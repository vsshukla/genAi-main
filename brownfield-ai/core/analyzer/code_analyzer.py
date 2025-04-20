import os

SUPPORTED_EXTENSIONS = ['.py', '.js', '.ts', '.java', '.cs', '.cpp', '.c']

def get_source_files(repo_path):
    code_files = []
    for root, _, files in os.walk(repo_path):
        for file in files:
            if any(file.endswith(ext) for ext in SUPPORTED_EXTENSIONS):
                full_path = os.path.join(root, file)
                code_files.append(full_path)
    return code_files

def analyze_codebase(repo_path):
    files = get_source_files(repo_path)
    code_data = []

    for file in files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            code_data.append({
                'file_path': file,
                'content': content,
                'lines': len(content.splitlines()),
                'size': os.path.getsize(file)
            })
        except Exception as e:
            print(f"Error reading {file}: {e}")

    return code_data
