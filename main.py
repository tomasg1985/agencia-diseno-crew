from src.crew import AgenciaDisenoCrew

def iniciar_agente_local():
    # Definimos el nicho que queremos analizar de manera dinámica
    inputs = {
        'nicho': 'Consultorios Dentales Locales',
        'presupuesto_base': '1200'
    }
    
    print("🤖 Iniciando el Agente Prospectador en tu máquina...")
    print("👀 Mira tu Administrador de Tareas / Monitor de Actividad ahora...\n")
    
    # Instanciamos la clase y ejecutamos la tarea
    resultado = AgenciaDisenoCrew().crew().kickoff(inputs=inputs)
    
    print("\n================ REPORTAJE FINAL DEL AGENTE ================\n")
    print(resultado)

if __name__ == "__main__":
    iniciar_agente_local()
