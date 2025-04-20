# core/llm_engine/prompts.py

def generate_task_prompt(code_info, language):
    prompt = f"""
You are an expert {language} code reviewer and maintainer AI. Analyze the following codebase
and identify any of the following tasks that should be performed:

- 🐞 Bug fixes
- ⚙️ Code enhancements
- 🔒 Security improvements
- 🔁 Migrations (e.g., outdated libraries or patterns)
- 🎨 Stylistic inconsistencies

For each task, return a JSON object with:
- `type`: "bug", "enhancement", "migration", "security_fix", or "style"
- `description`: Short description of the issue
- `file`: Filename where it occurs (if applicable)
- `line`: Line number or function name (if known)

Now here’s the code context:
{code_info}

Respond only with the JSON array of tasks.
    """
    return prompt
