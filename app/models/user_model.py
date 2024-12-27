from sqlalchemy import Column, Integer, String, Float
from app.models.base import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    daily_limit = Column(Float, default=1000.0)