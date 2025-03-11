from crewai import Agent
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

import os

llm = ChatGoogleGenerativeAI(
    model_name="gpt-3.5-turbo",
    api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.5,
    verbose=True
)