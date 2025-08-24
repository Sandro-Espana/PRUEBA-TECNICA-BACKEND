from fastapi import FastAPI
from app.routers.v1 import trademark_routers
from app.database import engine, Base

app = FastAPI(title="API de Control de Marcas")

Base.metadata.create_all(bind=engine)

app.include_router(trademark_routers.router)

@app.get("/")
def read_root():
    return {"message": "Brand Registry API is running"}