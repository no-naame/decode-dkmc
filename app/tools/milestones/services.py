from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List, Optional
from app.tools.milestones.models import Milestone
from app.tools.milestones.schemas import MilestoneCreate, MilestoneUpdate


class MilestoneService:
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def create_milestone(self, milestone_data: MilestoneCreate) -> Milestone:
        milestone = Milestone(**milestone_data.model_dump())
        self.db.add(milestone)
        await self.db.commit()
        await self.db.refresh(milestone)
        return milestone
    
    async def get_milestone(self, milestone_id: int) -> Optional[Milestone]:
        result = await self.db.execute(select(Milestone).where(Milestone.id == milestone_id))
        return result.scalar_one_or_none()
    
    async def get_milestones(self, skip: int = 0, limit: int = 100) -> List[Milestone]:
        result = await self.db.execute(select(Milestone).offset(skip).limit(limit))
        return result.scalars().all()
    
    async def update_milestone(self, milestone_id: int, milestone_data: MilestoneUpdate) -> Optional[Milestone]:
        milestone = await self.get_milestone(milestone_id)
        if not milestone:
            return None
        
        update_data = milestone_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(milestone, field, value)
        
        await self.db.commit()
        await self.db.refresh(milestone)
        return milestone
    
    async def delete_milestone(self, milestone_id: int) -> bool:
        milestone = await self.get_milestone(milestone_id)
        if not milestone:
            return False
        
        await self.db.delete(milestone)
        await self.db.commit()
        return True
