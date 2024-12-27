from fastapi import APIRouter, Query, HTTPException
from app.services.quote_service import get_quote

router = APIRouter()

@router.post("/quote/")
def quote_currency(
    currency_from: str = Query(..., description="Base currency (ex: USD)"),
    currency_to: str = Query(..., description="Target currency (ex:) MXN)"),
    amount: float = Query(..., description="Amount to convert")
):
    """
    Quote Exchange
    converting one currency to another.
    """
    try:
        return get_quote(currency_from, currency_to, amount)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
