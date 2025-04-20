import os
from collections import Counter, defaultdict  # ✅ fixed

EXTENSION_LANGUAGE_MAP = {
    '.py': 'Python',
    '.js': 'JavaScript',
    '.ts': 'TypeScript',
    '.java': 'Java',
    '.cs': 'C#',
    '.cpp': 'C++',
    '.c': 'C',
    '.rb': 'Ruby',
    '.go': 'Go',
    '.php': 'PHP',
    '.rs': 'Rust',
    '.swift': 'Swift',
    '.kt': 'Kotlin'
}

def detect_languages(repo_path: str):
    language_count = defaultdict(int)

    for root, _, files in os.walk(repo_path):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            language = EXTENSION_LANGUAGE_MAP.get(ext)
            if language:
                language_count[language] += 1

    if not language_count:
        return "Unknown"

    sorted_langs = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    return [lang for lang, _ in sorted_langs]
