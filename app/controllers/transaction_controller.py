from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.transaction_service import get_transactions_by_user_id
from app.database import get_db

router = APIRouter()

@router.get("/transactions/{user_id}")
def get_transactions(user_id: int, db: Session = Depends(get_db)):
    """
    Get a user's transactions.
    """
    transactions = get_transactions_by_user_id(db, user_id)
    
    if not transactions:
        raise HTTPException(status_code=404, detail="This user has no transactions")
    
    return transactions
