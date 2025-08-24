from sqlalchemy.orm import Session
from app.utils.converters import normalize_evidence_link
from app.repository.trademark_repository import get_by_registration_number, create, get_by_id, get_all, update, delete
from app.schemas.trademark_schema import BrandRegistryCreate, BrandRegistryUpdate
from fastapi import HTTPException, status

def create_brand_service(db: Session, payload: BrandRegistryCreate):
    data_dict = normalize_evidence_link(payload.model_dump())
    db_brand = get_by_registration_number(db, registration_number=payload.registration_number)
    if db_brand:
        raise HTTPException(status_code=400, detail="Registration number already exists")
    return create(db, data_dict)

def get_all_brands_service(db: Session):
    return get_all(db)

def get_brand_by_id_service(db: Session, trademark_id: int):
    db_brand = get_by_id(db, trademark_id)
    if not db_brand:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Trademark not found")
    return db_brand

def update_brand_service(db: Session, trademark_id: int, brand_data: BrandRegistryUpdate):
    data_dict = normalize_evidence_link(brand_data.model_dump())
    db_brand = update(db, trademark_id, data_dict)
    if not db_brand:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Trademark not found")
    return db_brand

def delete_brand_service(db: Session, trademark_id: int):
    db_brand = delete(db, trademark_id)
    if not db_brand:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Trademark not found")
    return db_brand