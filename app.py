from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.crew import AgenciaDisenoCrew

app = FastAPI(
    title="API de la Agencia de Diseño con IA",
    description="Backend para conectar nuestro sistema multiagente local con interfaces web."
)

class SolicitudProspeccion(BaseModel):
    nicho: str
    presupuesto_base: int

@app.get("/")
def inicio():
    return {"estado": "Servidor funcionando correctamente", "mensaje": "Bienvenido al backend de la agencia"}

@app.post("/prospectar")
def ejecutar_agencia(datos: SolicitudProspeccion):
    try:
        inputs = {
            'nicho': datos.nicho,
            'presupuesto_base': datos.presupuesto_base
        }
        
        agencia_crew = AgenciaDisenoCrew()
        
        resultado_final = agencia_crew.crew().kickoff(inputs=inputs)
        
        return {
            "exito": True,
            "nicho_analizado": datos.nicho,
            "correo_generado": str(resultado_final)
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Error interno en la ejecución de los agentes: {str(e)}"
        )
