import asyncio
import json
from sqlalchemy.orm import Session
from app.celery_worker import celery
from app.services import fetch_html, extract_metadata
from app.database import SessionLocal
from app.models import Metadata
from app.redis_client import redis_client

@celery.task(name="app.tasks.process_urls_task")
def process_urls_task(urls):
    """Celery task to scrape multiple URLs asynchronously."""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    async def process_url(url):
        """Fetch metadata for a single URL."""
        session: Session = SessionLocal()
        try:
            html = await fetch_html(url)
            metadata = extract_metadata(html)

            # Store in PostgreSQL
            record = Metadata(url=url, title=metadata.get("title"),
                              description=metadata.get("description"),
                              keywords=metadata.get("keywords"))
            session.add(record)
            session.commit()

            return {"url": url, **metadata}
        except Exception as e:
            session.rollback()
            return {"url": url, "error": str(e)}
        finally:
            session.close()

    tasks = [process_url(url) for url in urls]
    results = loop.run_until_complete(asyncio.gather(*tasks))

    # Store results in Redis
    task_id = process_urls_task.request.id
    redis_client.set(task_id, json.dumps(results), ex=3600)

    return results
