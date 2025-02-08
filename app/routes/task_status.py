from fastapi import APIRouter
from app.tasks import process_urls_task

router = APIRouter()

@router.get("/task_status/{task_id}")
async def get_task_status(task_id: str):
    """Check task status."""
    task = process_urls_task.AsyncResult(task_id)
    return {"status": task.state, "task_id": task_id}
