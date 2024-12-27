from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.models.base import Base

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    currency_from = Column(String, nullable=False)
    currency_to = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    result = Column(Float, nullable=False)