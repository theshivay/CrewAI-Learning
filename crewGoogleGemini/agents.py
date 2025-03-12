from crewai import Agent
from dotenv import load_dotenv
import os
from tools import serper_tool
from crewai import LLM

# Load environment variables
load_dotenv()
google_api_key = os.getenv("GEMINI_API_KEY")

from crewai import LLM
llm = LLM(
    model="gemini/gemini-1.5-flash",
    verbose=True,
    temperature=0.5,
    google_api_key = google_api_key
)

# Creating a senior researcher agent with memory and verbose mode
news_researcher = Agent(
    role="Senior Researcher",
    goal="Uncover groundbreaking technologies in {topic}",
    verbose=True,
    memory=True,
    backstory="Driven by curiosity, you're at the forefront of innovation, eager to explore and share knowledge that could change the world.",
    tools=[serper_tool],  # Ensure serper_tool is correctly configured
    llm=llm,
    allow_delegation=True
)

# Creating a writer agent with custom tools responsible for writing new blogs
news_writer = Agent(
    role="Writer",
    goal="Narrate compelling tech stories about {topic}",
    verbose=True,
    memory=True,
    backstory="With a flair for simplifying complex topics, you craft engaging narratives that captivate and educate, bringing new discoveries to light in an accessible manner.",
    tools=[serper_tool],  # Ensure serper_tool is correctly configured
    llm=llm,
    allow_delegation=False,
)
