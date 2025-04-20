# core/llm_engine/prompt_builder.py

def build_system_prompt(language: str) -> str:
    return f"""
You are a senior software engineer. Analyze the following {language} codebase for:
- Bugs or anti-patterns
- Enhancement opportunities
- Security issues
- Migration suggestions
- Stylistic inconsistencies

Respond in JSON with categorized tasks.
"""

def build_user_prompt(file_snippet: str, repo_context: str) -> str:
    return f"""
Repository Context:
{repo_context}

Code Snippet:
{file_snippet}

Please analyze and suggest actions.
"""
