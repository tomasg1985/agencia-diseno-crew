from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.llm import LLM

@CrewBase
class AgenciaDisenoCrew():
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # 1. REMOVE the entire def __init__(self): block completely.
    # 2. Instead, define the LLM properties directly on the class level:
    
    llm_comercial = LLM(
        model="ollama/llama3.2",
        base_url="http://localhost:11434",
        temperature=0.1,
    )
    
    llm_tecnico = LLM(
        model="ollama/qwen3.5:4b",
        base_url="http://localhost:11434",
        temperature=0.1,
    )

    # === REGISTRO DE AGENTES ===
    @agent
    def prospectador_agente(self) -> Agent:
        return Agent(
            config=self.agents_config['prospectador_agente'], 
            llm=self.llm_comercial, # Reference it as self.llm_comercial
            verbose=True, 
            max_iter=2
        )

    @agent
    def estratega_contenido_agente(self) -> Agent:
        return Agent(
            config=self.agents_config['estratega_contenido_agente'], 
            llm=self.llm_tecnico, # Reference it as self.llm_tecnico
            verbose=True, 
            max_iter=2
        )

    @agent
    def director_motion_agente(self) -> Agent:
        return Agent(
            config=self.agents_config['director_motion_agente'], 
            llm=self.llm_tecnico, 
            verbose=True, 
            max_iter=2
        )

    @agent
    def ejecutivo_cuentas_agente(self) -> Agent:
        return Agent(
            config=self.agents_config['ejecutivo_cuentas_agente'], 
            llm=self.llm_comercial, 
            verbose=True, 
            max_iter=2
        )

    # === REGISTRO DE TAREAS ===
    @task
    def buscar_clientes_tarea(self) -> Task:
        return Task(config=self.tasks_config['buscar_clientes_tarea'])

    @task
    def crear_estrategia_tarea(self) -> Task:
        return Task(config=self.tasks_config['crear_estrategia_tarea'])

    @task
    def generar_codigo_motion_tarea(self) -> Task:
        return Task(config=self.tasks_config['generar_codigo_motion_tarea'])

    @task
    def preparar_presupuesto_tarea(self) -> Task:
        return Task(config=self.tasks_config['preparar_presupuesto_tarea'])

    # === ORQUESTADOR ÚNICO ===
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
