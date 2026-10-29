from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.llm import LLM

@CrewBase
class AgenciaDisenoCrew():
    """Tripulación mínima para arrancar el desarrollo local"""
    
    # Indicamos las rutas relativas de nuestras configuraciones en texto
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self):
        # Configuramos Llama 3.2 apuntando a tu Ollama local
        self.llm_local = LLM(
            model="ollama/llama3.2",
            base_url="http://localhost:11434"
        )

    @agent
    def prospectador_agente(self) -> Agent:
        return Agent(
            config=self.agents_config['prospectador_agente'],
            llm=self.llm_local,
            verbose=True,
            max_iter=2  # Solo permitimos 2 intentos para cuidar tu procesador hoy
        )

    @task
    def buscar_clientes_tarea(self) -> Task:
        return Task(
            config=self.tasks_config['buscar_clientes_tarea']
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
