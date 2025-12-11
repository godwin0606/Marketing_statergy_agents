from typing import List
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task

# from crewai_tools import FileReadTool
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os

_ = load_dotenv()


llm = LLM(
     
    model="perplexity/sonar-pro",
    openai_api_key=os.getenv("PERPLEXITY_API_KEY"),
    temperature=0.7,
)


class Content(BaseModel):
    content_type: str = Field(...,
                              description="The type of content to be created (e.g., blog post, social media post, video)")
    topic: str = Field(..., description="The topic of the content")
    target_audience: str = Field(..., description="The target audience for the content")
    tags: List[str] = Field(..., description="Tags to be used for the content")
    content: str = Field(..., description="The content itself")


@CrewBase
class TheMarketingCrew():
    "The marketing crew is responsible for creating and executing marketing strategies, content creation, and managing marketing campaigns."
    agents_config = "C:/Users/vigne/OneDrive/Desktop/Marketing_crew/Marketing_Crew/Marketing_crew/config/agents.yaml"
    tasks_config = "C:/Users/vigne/OneDrive/Desktop/Marketing_crew/Marketing_Crew/Marketing_crew/config/tasks.yaml"

    @agent
    def head_of_marketing(self) -> Agent:
        return Agent(
            # config=self.agents_config.get('head_of_marketing'),#type : ignore[index]


            role=self.agents_config.get('head_of_marketing').get('role'),
            goal=self.agents_config.get('head_of_marketing').get('goal'),
            backstory=self.agents_config.get('head_of_marketing').get('backstory'),

            tools=[
                # ScrapeWebsiteTool(),
                # DirectoryReadTool('resources/drafts'),
                # FileWriterTool(),
                # FileReadTool()
            ],
            reasoning=True,
            inject_date=True,
            llm=llm,
            allow_delegation=True,
            max_rpm=3
        )

    @agent
    def content_creator_social_media(self) -> Agent:
        return Agent(
            # config=self.agents_config.get('content_creator_social_media'),#type : ignore[index]

            role=self.agents_config.get('content_creator_social_media').get('role'),
            goal=self.agents_config.get('content_creator_social_media').get('goal'),
            backstory=self.agents_config.get('content_creator_social_media').get('backstory'),

            tools=[
                
                # ScrapeWebsiteTool(),
                # DirectoryReadTool('resources/drafts'),
                # FileWriterTool(),
                # FileReadTool()
            ],
            inject_date=True,
            llm=llm,
            allow_delegation=True,
            max_iter=30,
            max_rpm=3
        )

    @agent
    def content_writer_blogs(self) -> Agent:
        return Agent(
            # config=self.agents_config.get('content_writer_blogs'),#type : ignore[index]

            role=self.agents_config.get('content_writer_blogs').get('role'),
            goal=self.agents_config.get('content_writer_blogs').get('goal'),
            backstory=self.agents_config.get('content_writer_blogs').get('backstory'),

            tools=[
                
                # ScrapeWebsiteTool(),
                # DirectoryReadTool('resources/drafts/blogs'),
                # FileWriterTool(),
                # FileReadTool()
            ],
            inject_date=True,
            llm=llm,
            allow_delegation=True,
            max_iter=5,
            max_rpm=3
        )

    @agent
    def seo_specialist(self) -> Agent:
        return Agent(
            # config=self.agents_config.get('seo_specialist'),#type : ignore[index]

            role=self.agents_config.get('seo_specialist').get('role'),
            goal=self.agents_config.get('seo_specialist').get('goal'),
            backstory=self.agents_config.get('seo_specialist').get('backstory'),

            tools=[
               
                # ScrapeWebsiteTool(),
                # DirectoryReadTool('resources/drafts'),
                # FileWriterTool(),
                # FileReadTool()
            ],
            inject_date=True,
            llm=llm,
            allow_delegation=True,
            max_iter=3,
            max_rpm=3
        )

    @task
    def market_research(self) -> Task:
        return Task(
            # config=self.tasks_config['market_research'],#type : ignore[index]
            config = self.tasks_config.get('market_research'),
            agent=self.head_of_marketing()
        )

    @task
    def prepare_marketing_strategy(self) -> Task:
        return Task(
            config=self.tasks_config.get('prepare_marketing_strategy'),#type : ignore[index]
            agent=self.head_of_marketing()
        )

    @task
    def create_content_calendar(self) -> Task:
        return Task(
            config=self.tasks_config.get('create_content_calendar'),#type : ignore[index]
            agent=self.content_creator_social_media()
        )

    # @task
    # def prepare_post_drafts(self) -> Task:
    #     return Task(
    #         config=self.tasks_config.get('prepare_post_drafts'),#type : ignore[index]
    #         agent=self.content_creator_social_media(),
    #         output_json=Content
    #     )

    # @task
    # def prepare_scripts_for_reels(self) -> Task:
    #     return Task(
    #         config=self.tasks_config.get('prepare_scripts_for_reels'),#type : ignore[index]
    #             agent=self.content_creator_social_media(),
    #         output_json=Content
    #     )

    @task
    def content_research_for_blogs(self) -> Task:
        return Task(
            config=self.tasks_config.get('content_research_for_blogs'),#type : ignore[index]
            agent=self.content_writer_blogs()
        )

    @task
    def draft_blogs(self) -> Task:
        return Task(
            config=self.tasks_config.get('draft_blogs'),#type : ignore[index]
            agent=self.content_writer_blogs(),
            output_json=Content
        )

    @task
    def seo_optimization(self) -> Task:
        return Task(
            config=self.tasks_config.get('seo_optimization'),#type : ignore[index]
            agent=self.seo_specialist(),
            output_json=Content
        )

    @crew
    def marketingcrew(self) -> Crew:
        """Creates the Marketing crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            planning=True,
            planning_llm=llm,
            max_rpm=3
        )


if __name__ == "__main__":
    from datetime import datetime

    inputs = {
        "product_name": "AI Powered Excel Automation Tool",
        "target_audience": "Small and Medium Enterprises (SMEs)",
        "product_description": "A tool that automates repetitive tasks in Excel using AI, saving time and reducing errors.",
        "budget": "Rs. 50,000",
        "current_date": datetime.now().strftime("%Y-%m-%d"),
    }
    crew = TheMarketingCrew()
    crew.marketingcrew().kickoff(inputs=inputs)
    print("Marketing crew has been successfully created and run.")