# https://serper.dev/playground
from dotenv import load_dotenv
load_dotenv()
import os

os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

from crewai_tools import SerperDevTool

# Initializing the SerperDevTool for internet searching capabilities
serper_tool = SerperDevTool(
    api_key=os.getenv("SERPER_API_KEY"),
    verbose=True
)

