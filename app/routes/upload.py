from fastapi import APIRouter, UploadFile, File, HTTPException
import csv
import io
from app.tasks import process_urls_task

router = APIRouter()

@router.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    """Process a CSV file with URLs and start Celery task."""
    try:
        contents = await file.read()
        csv_data = io.StringIO(contents.decode("utf-8"))
        reader = csv.reader(csv_data)

        next(reader, None)  # Skip header if exists
        urls = [row[0] for row in reader if row]

        if not urls:
            raise HTTPException(status_code=400, detail="Invalid or empty CSV file.")

        task = process_urls_task.delay(urls)
        return {"status": "processing", "task_id": task.id}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
