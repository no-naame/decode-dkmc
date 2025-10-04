from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.core.database import get_db
from app.tools.milestones.schemas import MilestoneCreate, MilestoneUpdate, MilestoneResponse
from app.tools.milestones.services import MilestoneService
from app.tools.milestones.utils import format_response, format_error_response

router = APIRouter()


@router.get("/", response_model=dict)
async def hello_milestones():
    """Simple hello endpoint for milestones"""
    return format_response({"message": "Hello from Milestones API!"})


@router.post("/", response_model=dict)
async def create_milestone(
    milestone_data: MilestoneCreate,
    db: AsyncSession = Depends(get_db)
):
    """Create a new milestone"""
    try:
        service = MilestoneService(db)
        milestone = await service.create_milestone(milestone_data)
        return format_response(
            MilestoneResponse.model_validate(milestone),
            "Milestone created successfully"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=format_error_response(f"Failed to create milestone: {str(e)}")
        )


@router.get("/{milestone_id}", response_model=dict)
async def get_milestone(
    milestone_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Get a milestone by ID"""
    service = MilestoneService(db)
    milestone = await service.get_milestone(milestone_id)
    
    if not milestone:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=format_error_response("Milestone not found")
        )
    
    return format_response(
        MilestoneResponse.model_validate(milestone),
        "Milestone retrieved successfully"
    )


@router.get("/", response_model=dict)
async def get_milestones(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    """Get all milestones with pagination"""
    service = MilestoneService(db)
    milestones = await service.get_milestones(skip=skip, limit=limit)
    
    return format_response(
        [MilestoneResponse.model_validate(milestone) for milestone in milestones],
        "Milestones retrieved successfully"
    )


@router.put("/{milestone_id}", response_model=dict)
async def update_milestone(
    milestone_id: int,
    milestone_data: MilestoneUpdate,
    db: AsyncSession = Depends(get_db)
):
    """Update a milestone"""
    service = MilestoneService(db)
    milestone = await service.update_milestone(milestone_id, milestone_data)
    
    if not milestone:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=format_error_response("Milestone not found")
        )
    
    return format_response(
        MilestoneResponse.model_validate(milestone),
        "Milestone updated successfully"
    )


@router.delete("/{milestone_id}", response_model=dict)
async def delete_milestone(
    milestone_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Delete a milestone"""
    service = MilestoneService(db)
    success = await service.delete_milestone(milestone_id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=format_error_response("Milestone not found")
        )
    
    return format_response(
        {"id": milestone_id},
        "Milestone deleted successfully"
    )
