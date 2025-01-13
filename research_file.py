import os
from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task
from openai import OpenAI
from crewai_tools import SerperDevTool

# Load environment variables from .env file
load_dotenv()

search_tool = SerperDevTool()

llm = OpenAI()

# os.environ["OPENAI_MODEL_NAME"] = "gpt-4"

researcher = Agent(
    role="Senior Research Analyst",
    goal="Uncover cutting-edge developments in AI",
    backstory="You are an experienced research anyalyst with a keen eye for emerging trends in technology. Your",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    memory=True
)

writer = Agent(
    role="Content Writer",
    goal="Create engaging articles about AI developments",
    backstory="You are a skilled writer with a passion for explaining complex technological concepts in simple ...",
    verbose=True,
    allow_delegation=False,
)

research_task = Task(
    description="Research the latest advancements in AI and summarize your findings",
    agent=researcher,
    expected_output="A bullet-point list of the most 3 AI breakthroughs ...",
)

writing_task = Task(
    description="Write a blog post about the top 3 AI breakthroughs",
    agent=writer,
    expected_output="A 500-word blog post discussing the top 3 AI breakthroughs ...",
    context=[research_task],
)

crew = Crew(
    members=[researcher, writer],
    tasks=[research_task, writing_task],
    process=Process.sequential,
    verbose=True,
)

result = crew.kickoff()
print(result)
