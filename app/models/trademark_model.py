from sqlalchemy import Column, Integer, String, Date, Boolean, Text
from app.database import Base

class BrandRegistry(Base):
    __tablename__ = "tb_brand_registry"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    registration_number = Column(String, unique=True, nullable=False, index=True)
    country = Column(String(100), nullable=False)
    registration_date = Column(Date, nullable=False)
    status = Column(String(50), nullable=False, default="active")
    monitored_platforms = Column(String, nullable=True)
    can_enforce = Column(Boolean, default=True)
    authority_collaboration = Column(String, nullable=True)
    last_monitoring_date = Column(Date, nullable=True)
    evidence_link = Column(Text, nullable=True)
    active = Column(Boolean, default=True)
