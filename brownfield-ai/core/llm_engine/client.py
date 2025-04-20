# # core/llm_engine/client.py

# from langchain.chat_models import ChatOpenAI
# from langchain.chat_models import AzureChatOpenAI
# import os

# def get_llm_client():
#     provider = os.getenv("LLM_PROVIDER", "openai")  # openai or azure

#     if provider == "azure":
#         return AzureChatOpenAI(
#             deployment_name=os.getenv("AZURE_DEPLOYMENT_NAME"),
#             openai_api_base=os.getenv("AZURE_API_BASE"),
#             openai_api_key=os.getenv("AZURE_API_KEY"),
#             openai_api_version=os.getenv("AZURE_API_VERSION"),
#             temperature=0
#         )
#     else:
#         return ChatOpenAI(
#             model=os.getenv("OPENAI_MODEL", "gpt-4"),
#             openai_api_key=os.getenv("OPENAI_API_KEY"),
#             temperature=0
#         )


# core/llm_engine/client.py

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def get_openai_client():
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
