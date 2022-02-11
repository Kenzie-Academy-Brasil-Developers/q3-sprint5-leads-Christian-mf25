from sqlalchemy import Column, Integer, DateTime, String
from app.configs.database import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class LeadModel(db.Model):
    keys = ["name", "email", "phone"]
    default_keys = ["id", "creation_date", "last_visit", "visits"]
    __tablename__ = "leads"
    time_now = datetime.now()
    
    id = Column(Integer, primary_key=True)
    name: str = Column(String, nullable=False)
    email: str = Column(String, unique=True, nullable=False)
    phone: str = Column(String, unique=True, nullable=False)
    creation_date: str = Column(DateTime, default=time_now)
    last_visit: str = Column(DateTime, default=time_now)
    visits: int = Column(Integer, default=1)
