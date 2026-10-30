from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from src.tools.search_tool import buscar_en_internet

@CrewBase
class AgenciaDisenoCrew():
    """Tripulación AgenciaDisenoCrew para prospección y estrategia creativa"""

    # Definición limpia y ultra-compatible de Modelos Locales (Ollama)
    llm_comercial = LLM(
        model="ollama/llama3.2",
        base_url="http://localhost:11434",
        temperature=0.2
    )
    
    llm_tecnico = LLM(
        model="ollama/qwen3.5:4b",
        base_url="http://localhost:11434",
        temperature=0.1
    )

    @agent
    def prospectador_agente(self) -> Agent:
        return Agent(
            config=self.agents_config['prospectador_agente'],
            llm=self.llm_comercial,
            tools=[buscar_en_internet],  # Asignación limpia de la herramienta en el cinturón del agente
            verbose=True,
            max_iter=2
        )

    @agent
    def estratega_contenido_agente(self) -> Agent:
        return Agent(
            config=self.agents_config['estratega_contenido_agente'],
            llm=self.llm_tecnico,
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

    @task
    def buscar_clientes_tarea(self) -> Task:
        return Task(
            config=self.tasks_config['buscar_clientes_tarea'],
        )

    @task
    def crear_estrategia_tarea(self) -> Task:
        return Task(
            config=self.tasks_config['crear_estrategia_tarea'],
        )

    @task
    def generar_codigo_motion_tarea(self) -> Task:
        return Task(
            config=self.tasks_config['generar_codigo_motion_tarea'],
        )

    @task
    def preparar_presupuesto_tarea(self) -> Task:
        return Task(
            config=self.tasks_config['preparar_presupuesto_tarea'],
        )

    @crew
    def crew(self) -> Crew:
        """Crea la tripulación de la Agencia de Diseño"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
