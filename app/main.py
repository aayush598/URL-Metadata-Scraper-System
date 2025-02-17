from fastapi import FastAPI
from app.routes import upload, task_status, results, auth
from app.database import Base, engine
from app.celery_worker import celery  # Celery instance

# Initialize FastAPI
app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Include Routers
app.include_router(upload.router)
app.include_router(task_status.router)
app.include_router(results.router)
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
# Run Celery worker in another terminal before starting FastAPI
