from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from datetime import date

class BrandRegistryBase(BaseModel):
    name: str
    registration_number: str
    country: str
    registration_date: date
    status: str
    monitored_platforms: Optional[str] = None
    can_enforce: Optional[bool] = True
    authority_collaboration: Optional[str] = None
    last_monitoring_date: Optional[date] = None
    evidence_link: Optional[HttpUrl] = None

class BrandRegistryCreate(BrandRegistryBase):
    pass

class BrandRegistryUpdate(BaseModel):
    status: Optional[str] = None
    monitored_platforms: Optional[str] = None
    last_monitoring_date: Optional[date] = None
    evidence_link: Optional[HttpUrl] = None
    can_enforce: Optional[bool] = None
    authority_collaboration: Optional[str] = None

class BrandRegistryOut(BrandRegistryBase):
    id: int
    active: bool = True

    model_config = {"from_attributes": True}

class BrandRegistryList(BaseModel):
    items: List[BrandRegistryOut]
    total: int
