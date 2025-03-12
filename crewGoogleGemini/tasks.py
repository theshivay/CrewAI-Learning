from crewai import Task
from tools import serper_tool
from agents import news_researcher,news_writer
# from crew import topic
import re
from datetime import datetime

def sanitize_filename(topic):
    """Removes invalid characters and formats the topic for a filename."""
    topic = topic.lower().strip()
    topic = re.sub(r'[^\w\s-]', '', topic)  # Remove special characters
    topic = re.sub(r'\s+', '_', topic)  # Replace spaces with underscores
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"./Blog/{topic}_{timestamp}.md"
    return output_filename

# Research task
research_task = Task(
  description=(
    "Identify the next big trend in {topic}."
    "Focus on identifying pros and cons and the overall narrative."
    "Your final report should clearly articulate the key points,"
    "its market opportunities, and potential risks."
  ),
  expected_output='A comprehensive 3 paragraphs long report on the latest AI trends.',
  tools=[serper_tool],
  agent=news_researcher,
)

# Writing task with language model configuration
write_task = Task(
  description=(
    "Compose an insightful article on {topic}."
    "Focus on the latest trends and how it's impacting the industry."
    "This article should be easy to understand, engaging, and positive."
  ),
  expected_output='A 4 paragraph article on {topic} advancements formatted as markdown.',
  tools=[serper_tool],
  agent=news_writer,
  async_execution=False,
  output_file="./Blog/tech-blog.md"  # Example of output customization
)