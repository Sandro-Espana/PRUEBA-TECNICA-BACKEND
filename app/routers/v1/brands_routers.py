from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.trademark_schema import BrandRegistryCreate, BrandRegistryOut, BrandRegistryUpdate
from app.services.trademark_service import create_brand_service, get_brand_by_id_service, get_all_brands_service, update_brand_service, delete_brand_service
from app.database import get_db

# Router para rutas /brands (compatibilidad con frontend)
brands_router = APIRouter(
    prefix="/brands",
    tags=["Brands (Compatibilidad)"]
)

@brands_router.post("", response_model=BrandRegistryOut, status_code=status.HTTP_201_CREATED)
def create_brand(payload: BrandRegistryCreate, db: Session = Depends(get_db)):
    return create_brand_service(db, payload)

@brands_router.get("", response_model=list[BrandRegistryOut])
def list_brands(db: Session = Depends(get_db)):
    return get_all_brands_service(db)

@brands_router.get("/{trademark_id}", response_model=BrandRegistryOut)
def get_brand(trademark_id: int, db: Session = Depends(get_db)):
    return get_brand_by_id_service(db, trademark_id)

@brands_router.put("/{trademark_id}", response_model=BrandRegistryOut)
def update_brand(trademark_id: int, payload: BrandRegistryUpdate, db: Session = Depends(get_db)):
    return update_brand_service(db, trademark_id, payload)

@brands_router.delete("/{trademark_id}", response_model=BrandRegistryOut)
def delete_brand(trademark_id: int, db: Session = Depends(get_db)):
    return delete_brand_service(db, trademark_id)
