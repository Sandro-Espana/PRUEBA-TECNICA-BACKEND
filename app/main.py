from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.v1 import trademark_routers, brands_routers
from app.database import engine, Base
from app.middleware.cors_middleware import CORSDebugMiddleware
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="API de Control de Marcas")

# Agregar middleware de debugging CORS
app.add_middleware(CORSDebugMiddleware)

# Configuración de CORS para permitir conexiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001", 
        "https://prueba-tecnica-frontend-gamma.vercel.app",
        "https://prueba-tecnica-frontend-git-master-sandro-espanas-projects.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
    expose_headers=["*"],
    max_age=86400,  # Cache preflight por 24 horas
)

Base.metadata.create_all(bind=engine)

# Incluir ambos routers
app.include_router(trademark_routers.router)
app.include_router(brands_routers.brands_router)

@app.get("/")
def read_root():
    return {"message": "Brand Registry API is running"}

@app.get("/health")
def health_check():
    """Endpoint de verificación de salud de la API"""
    return {"status": "healthy", "cors_enabled": True}

@app.options("/brands")
async def options_brands():
    """Endpoint OPTIONS para /brands para manejar preflight CORS"""
    return {"message": "CORS preflight handled"}

@app.options("/brands/{trademark_id}")
async def options_brand_by_id(trademark_id: int):
    """Endpoint OPTIONS para /brands/{id} para manejar preflight CORS"""
    return {"message": "CORS preflight handled"}