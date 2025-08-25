from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from app.routers.v1 import trademark_routers, brands_routers
from app.database import engine, Base

app = FastAPI(title="API de Control de Marcas")

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
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

# Incluir ambos routers
app.include_router(trademark_routers.router)
app.include_router(brands_routers.brands_router)

@app.get("/")
def read_root():
    return {"message": "Brand Registry API is running"}

# Alias para mantener compatibilidad con el frontend
@app.get("/brands")
def redirect_brands():
    """Redirige /brands a /api/v1/trademark para compatibilidad"""
    return RedirectResponse(url="/api/v1/trademark")

@app.post("/brands")
def redirect_create_brand():
    """Redirige POST /brands a POST /api/v1/trademark para compatibilidad"""
    return RedirectResponse(url="/api/v1/trademark", status_code=307)

@app.get("/brands/{trademark_id}")
def redirect_get_brand(trademark_id: int):
    """Redirige GET /brands/{id} a GET /api/v1/trademark/{id} para compatibilidad"""
    return RedirectResponse(url=f"/api/v1/trademark/{trademark_id}")

@app.put("/brands/{trademark_id}")
def redirect_update_brand(trademark_id: int):
    """Redirige PUT /brands/{id} a PUT /api/v1/trademark/{id} para compatibilidad"""
    return RedirectResponse(url=f"/api/v1/trademark/{trademark_id}", status_code=307)

@app.delete("/brands/{trademark_id}")
def redirect_delete_brand(trademark_id: int):
    """Redirige DELETE /brands/{id} a DELETE /api/v1/trademark/{id} para compatibilidad"""
    return RedirectResponse(url=f"/api/v1/trademark/{trademark_id}", status_code=307)