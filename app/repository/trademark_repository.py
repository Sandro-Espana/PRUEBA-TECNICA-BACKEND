from sqlalchemy.orm import Session
from datetime import datetime
from app.models.trademark_model import BrandRegistry


def get_by_registration_number(db: Session, registration_number: str):
    return db.query(BrandRegistry).filter(BrandRegistry.registration_number ==      registration_number).first()

def get_all(db: Session):
    return db.query(BrandRegistry).filter(BrandRegistry.active == True).all()

def get_by_id(db: Session, trademark_id: int):
    return db.query(BrandRegistry).filter(BrandRegistry.id == trademark_id,
        BrandRegistry.active == True).first()

def create(db: Session, brand_data: dict):
    new_brand = BrandRegistry(**brand_data)
    db.add(new_brand)
    db.commit()
    db.refresh(new_brand)
    return new_brand

def update(db: Session, trademark_id: int, brand_data: dict):
    db_brand = db.query(BrandRegistry).filter(BrandRegistry.id == trademark_id).first()
    if not db_brand:
        return None
    for key, value in brand_data.items():
        setattr(db_brand, key, value)
    db.commit()
    db.refresh(db_brand)
    return db_brand

def delete(db: Session, trademark_id: int):
    db_brand = db.query(BrandRegistry).filter(BrandRegistry.id == trademark_id).first()
    if not db_brand:
        return None
    db_brand.active = False
    db_brand.deleted_at = datetime.utcnow()
    db.commit()
    db.refresh(db_brand)
    return db_brand