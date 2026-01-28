from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class BankingFinancialServicesIntelligentCustomerResolution():
    """BankingFinancialServicesIntelligentCustomerResolution crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    # @agent
    # def researcher(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['researcher'], # type: ignore[index]
    #         verbose=True
    #     )
    #
    # @agent
    # def reporting_analyst(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['reporting_analyst'], # type: ignore[index]
    #         verbose=True
    #     )

    @agent
    def intent_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['intent_agent'],
            verbose=True
        )

    @agent
    def risk_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['risk_agent'],
            verbose=True
        )

    @agent
    def knowledge_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['knowledge_agent'],
            verbose=True
        )

    @agent
    def resolution_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['resolution_agent'],
            verbose=True
        )

    @agent
    def communication_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['communication_agent'],
            verbose=True
        )

    @agent
    def escalation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['escalation_agent'],
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    # @task
    # def research_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['research_task'], # type: ignore[index]
    #     )
    #
    # @task
    # def reporting_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['reporting_task'], # type: ignore[index]
    #         output_file='report.md'
    #     )

    @task
    def intent_task(self) -> Task:
        return Task(
            config=self.tasks_config['intent_task'],
        )

    @task
    def risk_task(self) -> Task:
        return Task(
            config=self.tasks_config['risk_task'],
        )

    @task
    def knowledge_task(self) -> Task:
        return Task(
            config=self.tasks_config['knowledge_task'],
        )

    @task
    def resolution_task(self) -> Task:
        return Task(
            config=self.tasks_config['resolution_task'],
        )

    @task
    def communication_task(self) -> Task:
        return Task(
            config=self.tasks_config['communication_task'],
        )

    @task
    def escalation_task(self) -> Task:
        return Task(
            config=self.tasks_config['escalation_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the BankingFinancialServicesIntelligentCustomerResolution crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
