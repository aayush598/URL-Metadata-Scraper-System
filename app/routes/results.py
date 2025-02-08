from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Metadata

router = APIRouter()

@router.get("/results/{task_id}")
async def get_results(task_id: str):
    """Retrieve extracted metadata from PostgreSQL."""
    session: Session = SessionLocal()
    try:
        results = session.query(Metadata).all()

        if not results:
            raise HTTPException(status_code=404, detail="No metadata found.")

        return [{"url": record.url, "title": record.title, "description": record.description, "keywords": record.keywords} for record in results]

    finally:
        session.close()
