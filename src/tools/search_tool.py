import os
from crewai_tools import SerperDevTool

# Instanciamos la herramienta oficial nativa de CrewAI.
# El componente buscará de forma automatizada la variable "SERPER_API_KEY" en tu archivo .env
buscar_en_internet = SerperDevTool(
    name="Herramienta de Búsqueda Web para Agencias",
    description=(
        "Busca información en tiempo real en Google sobre un nicho o empresas específicas. "
        "Úsala cuando necesites encontrar datos reales sobre la presencia digital de un negocio."
    )
)
