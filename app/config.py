import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:newpassword@localhost:5432/metadata_scraper")

CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://default:password@redis-url:18479")
CELERY_BACKEND = os.getenv("CELERY_BACKEND", "redis://default:password@redis-url:18479")

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_DB = int(os.getenv("REDIS_DB", 0))
SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
