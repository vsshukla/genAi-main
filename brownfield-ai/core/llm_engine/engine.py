# core/llm_engine/engine.py
import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_llm(prompt: str):
    try:
        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4"),
            messages=[
                {"role": "system", "content": "You are a helpful code reviewer and migration expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )
        # Ensure response parsing is correct
        output = response['choices'][0]['message']['content'].strip()
        return json.loads(output)  # Expecting structured JSON list of tasks
    except Exception as e:
        print(f"❌ Error communicating with LLM: {e}")
        return []
