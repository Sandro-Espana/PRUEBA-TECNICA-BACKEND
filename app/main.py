from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.v1 import trademark_routers
from app.database import engine, Base

app = FastAPI(title="API de Control de Marcas")

# Configuración de CORS para permitir conexiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Frontend en desarrollo
        "https://localhost:3000",  # Frontend en desarrollo con HTTPS
        "http://127.0.0.1:3000",  # Frontend en desarrollo (alternativo)
        "https://127.0.0.1:3000",  # Frontend en desarrollo con HTTPS (alternativo)
        # Agrega aquí tu dominio de producción cuando lo tengas
        # "https://tu-dominio-produccion.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP
    allow_headers=["*"],  # Permite todos los headers
)

Base.metadata.create_all(bind=engine)

app.include_router(trademark_routers.router)

@app.get("/")
def read_root():
    return {"message": "Brand Registry API is running"}