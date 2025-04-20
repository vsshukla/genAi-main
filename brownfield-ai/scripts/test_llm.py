# scripts/test_llm.py
from core.llm_engine.task_extractor import extract_tasks

if __name__ == "__main__":
    code = """public class Test { void badCode() { String s = null; s.length(); } }"""
    lang = "Java"
    result = extract_tasks(lang, code)
    print(result)
