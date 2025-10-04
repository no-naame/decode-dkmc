from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class MilestoneBase(BaseModel):
    title: str
    description: Optional[str] = None
    is_completed: bool = False


class MilestoneCreate(MilestoneBase):
    pass


class MilestoneUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None


class MilestoneResponse(MilestoneBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True
