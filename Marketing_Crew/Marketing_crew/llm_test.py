from typing import List
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task

# from crewai_tools import FileReadTool
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os

_ = load_dotenv()


os.environ["OPENROUTER_API_KEY"] = os.getenv("OPENROUTER_API_KEY")

llm = LLM(

    model="openrouter/gpt-4o-mini",
    openai_api_key=os.environ["OPENROUTER_API_KEY"],
    temperature=0.7,
)



result = llm.invoke("tell me about Agentic AI")

print(result)