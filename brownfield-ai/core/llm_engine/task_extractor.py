# # core/llm_engine/task_extractor.py
# from .client import get_llm_client
# from .prompt_builder import build_system_prompt, build_user_prompt
# from langchain.schema import SystemMessage, HumanMessage
# from core.llm_engine.client import get_llm_client
# from langchain.prompts import PromptTemplate

# import os
# import json

# def extract_tasks(language: str, file_snippet: str, repo_context: str = "") -> dict:
#     llm = get_llm_client()
#     messages = [
#         SystemMessage(content=build_system_prompt(language)),
#         HumanMessage(content=build_user_prompt(file_snippet, repo_context))
#     ]
#     result = llm(messages)
#     try:
#         return json.loads(result.content)
#     except json.JSONDecodeError:
#         return {"error": "LLM response is not valid JSON", "raw": result.content}


# # core/llm_engine/task_extractor.py
# def extract_tasks_from_code(code: str) -> list[dict]:
#     llm = get_llm_client()

#     with open("workflows/prompts/system_prompt.txt", "r") as f:
#         system_prompt = f.read()

#     prompt = PromptTemplate.from_template("{code}")

#     chain = prompt | llm

#     try:
#         result = chain.invoke({"code": code})
#         return eval(result.content) if isinstance(result.content, str) else result
#     except Exception as e:
#         print("Failed to analyze code:", e)
#         return []




# core/llm_engine/task_extractor.py

from core.llm_engine.engine import ask_llm
from core.llm_engine.prompts import generate_task_prompt

def extract_tasks(language: str, file_snippet: str, repo_context: str = "") -> dict:
    """
    Extracts tasks using language and file snippet with optional repo context.
    """
    prompt = f"""
You are a highly skilled {language} developer and AI assistant.
Analyze the following code snippet in the context of the repo and identify:
- Bugs
- Enhancements
- Code Smells
- Security Issues

Provide results as a JSON list with type, description, and file.

Context: {repo_context}

Code:
{file_snippet[:3000]}

python
Copy
Edit
"""
    return ask_llm(prompt)

def extract_tasks_from_code(code_snippets: list, language: str) -> list[dict]:
    """
    Extracts tasks from the full codebase using a structured prompt.
    """
    prompt = generate_task_prompt(code_snippets, language)
    return ask_llm(prompt)
