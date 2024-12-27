from sqlalchemy.orm import Session
from app.models.transaction import Transaction

def get_transactions_by_user_id(db: Session, user_id: int):
    """
    Get all transactions for a user
    """
    return db.query(Transaction).filter(Transaction.user_id == user_id).all()
