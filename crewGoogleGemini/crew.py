from crewai import Process, Crew

from tasks import research_task, write_task
from agents import news_researcher, news_writer

## Forming the tech focused crew with some enhanced configuration
topic = 'AI in Tech'

crew = Crew(
    agents=[news_researcher, news_writer],
    tasks=[research_task, write_task],
    process=Process.sequential
)

## starting the task execution process wiht enhanced feedback
result = crew.kickoff(inputs={'topic':topic})
print(result)