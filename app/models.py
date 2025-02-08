from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Metadata(Base):
    __tablename__ = "url_metadata"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True, nullable=False)
    title = Column(String)
    description = Column(Text)
    keywords = Column(Text)
