from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.tools.milestones.routes.endpoints import router as milestones_router


# Create FastAPI app
app = FastAPI(
    title=settings.app_name,
    description="A FastAPI template with async SQLAlchemy",
    version="1.0.0",
    debug=settings.debug
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(
    milestones_router,
    prefix=f"{settings.api_v1_prefix}/milestones",
    tags=["milestones"]
)


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to DKMC Backend API",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "message": "API is running"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug
    )
