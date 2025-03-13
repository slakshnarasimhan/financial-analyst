from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SeleniumScrapingTool
from crewai_tools import ScrapeElementFromWebsiteTool
from crewai_tools import ScrapeWebsiteTool

@CrewBase
class FinancialAgentInvestmentRecommendationChatCrew():
    """FinancialAgentInvestmentRecommendationChat crew"""

    @agent
    def data_crawler(self) -> Agent:
        return Agent(
            config=self.agents_config['data_crawler'],
            tools=[SeleniumScrapingTool(), ScrapeElementFromWebsiteTool()],
        )

    @agent
    def data_processor(self) -> Agent:
        return Agent(
            config=self.agents_config['data_processor'],
            tools=[],
        )

    @agent
    def peer_comparator(self) -> Agent:
        return Agent(
            config=self.agents_config['peer_comparator'],
            tools=[ScrapeWebsiteTool()],
        )

    @agent
    def recommendation_maker(self) -> Agent:
        return Agent(
            config=self.agents_config['recommendation_maker'],
            tools=[],
        )

    @agent
    def process_logger(self) -> Agent:
        return Agent(
            config=self.agents_config['process_logger'],
            tools=[],
        )


    @task
    def crawl_company_financials(self) -> Task:
        return Task(
            config=self.tasks_config['crawl_company_financials'],
            tools=[SeleniumScrapingTool(), ScrapeElementFromWebsiteTool()],
        )

    @task
    def process_financial_data(self) -> Task:
        return Task(
            config=self.tasks_config['process_financial_data'],
            tools=[],
        )

    @task
    def crawl_peer_financial_data(self) -> Task:
        return Task(
            config=self.tasks_config['crawl_peer_financial_data'],
            tools=[ScrapeWebsiteTool()],
        )

    @task
    def generate_investment_recommendation(self) -> Task:
        return Task(
            config=self.tasks_config['generate_investment_recommendation'],
            tools=[],
        )

    @task
    def log_process_details(self) -> Task:
        return Task(
            config=self.tasks_config['log_process_details'],
            tools=[],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the FinancialAgentInvestmentRecommendationChat crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
