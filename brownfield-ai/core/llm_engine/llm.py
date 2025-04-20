# core/llm_engine/llm.py

from langchain_openai.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from langchain.prompts import ChatPromptTemplate
import os

from dotenv import load_dotenv
load_dotenv()

print('OPENAI_API_KEY ==> ',os.getenv("OPENAI_API_KEY"))
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")
print(f"API Key loaded: {api_key}")


# Initialize LLM model
llm = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL", "gpt-4"),
    temperature=0.2,
    openai_api_key=os.getenv("OPENAI_API_KEY"),
)


def process_with_llm(prompt: str) -> list:
    messages = [
        SystemMessage(content="You are an expert code reviewer. Identify bugs, enhancements, migrations, and security issues."),
        HumanMessage(content=prompt)
    ]

    response = llm.invoke(messages)  # ✅ Use invoke instead of direct call
    return parse_response(response.content)


def parse_response(response: str) -> list:
    """
    Expected format:
    - type: bug
      description: Null pointer in file X line 12
      file: path/to/file
    """
    import json
    try:
        return json.loads(response)
    except Exception as e:
        print(f"Error parsing response: {e}")
        return []


# azure openai

# from langchain_openai import ChatOpenAI
# from langchain.schema import SystemMessage, HumanMessage
# import os

# # Load environment variables (make sure you have them set)
# from dotenv import load_dotenv
# load_dotenv()

# azure_api_key = os.getenv("AZURE_API_KEY")
# azure_endpoint = os.getenv("AZURE_ENDPOINT")

# if not azure_api_key or not azure_endpoint:
#     raise ValueError("Azure API Key or Endpoint not set in environment variables.")

# print(f"Azure API Key loaded: {azure_api_key}")

# # Initialize LLM model with Azure's OpenAI API
# llm = ChatOpenAI(
#     model="gpt-4",  # You can specify your model here, such as "gpt-4" or another available model.
#     temperature=0.2,
#     openai_api_key=azure_api_key,  # Azure key
#     openai_api_base=azure_endpoint  # Azure endpoint
# )

# def process_with_llm(prompt: str) -> list:
#     messages = [
#         SystemMessage(content="You are an expert code reviewer. Identify bugs, enhancements, migrations, and security issues."),
#         HumanMessage(content=prompt)
#     ]

#     response = llm(messages)
#     return parse_response(response.content)

# def parse_response(response: str) -> list:
#     import json
#     try:
#         return json.loads(response)
#     except Exception as e:
#         print(f"Error parsing response: {e}")
#         return []
