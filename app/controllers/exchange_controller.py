from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.services.exchange_service import process_exchange
from app.schemas.exchange_schema import ExchangeRequest
from app.database import get_db

router = APIRouter()

@router.post("/exchange/")
def exchange_currency(request: ExchangeRequest, db: Session = Depends(get_db)):
    """
    Exchange currency per user
    """
    try:
        return process_exchange(
            user_id=request.user_id,
            currency_from=request.currency_from,
            currency_to=request.currency_to,
            amount=request.amount,
            db=db
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

