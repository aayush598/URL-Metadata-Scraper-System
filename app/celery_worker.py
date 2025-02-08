from celery import Celery
from app.config import CELERY_BROKER_URL, CELERY_BACKEND

celery = Celery("tasks", broker=CELERY_BROKER_URL, backend=CELERY_BACKEND)

celery.autodiscover_tasks(["app.tasks"])