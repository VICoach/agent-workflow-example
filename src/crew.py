from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Retrieve API key and model from environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL = os.getenv("CREW_MODEL")

@CrewBase
class Demo():
	"""Demo crew"""

	# Configuration files for agents and tasks
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def researcher(self) -> Agent:
		# Create and return a researcher agent
		return Agent(
			config=self.agents_config['researcher'],
			verbose=True
		)

	@agent
	def reporting_analyst(self) -> Agent:
		# Create and return a reporting analyst agent
		return Agent(
			config=self.agents_config['reporting_analyst'],
			verbose=True
		)

	@task
	def research_task(self) -> Task:
		# Create and return a research task
		return Task(
			config=self.tasks_config['research_task'],
		)

	@task
	def reporting_task(self) -> Task:
		# Create and return a reporting task
		return Task(
			config=self.tasks_config['reporting_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Demo crew"""

		# Create and return a crew with the defined agents and tasks
		return Crew(
			agents=self.agents,  # Automatically created by the @agent decorator
			tasks=self.tasks,  # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			api_key=GROQ_API_KEY,
			model=MODEL
		)
