from sqlalchemy.orm import Session
from app.models.transaction import Transaction
from app.models.user_model import User
import requests

def process_exchange(db: Session, user_id: int, currency_from: str, currency_to: str, amount: float):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise ValueError("User not found")
    if amount > user.daily_limit:
        raise ValueError("Amount exceeds daily limit")
    
    api_url = f"https://v6.exchangerate-api.com/v6/cbb56a87b9a2c0ad47eb558c/latest/{currency_from}"
    response = requests.get(api_url)

    if response.status_code != 200:
        raise Exception("Error getting exchange rate")
    
    data = response.json()
    print (data)

    if currency_to not in data["conversion_rates"]:
        raise ValueError(f"Conversion rate for {currency_to} not found")
    
    rate = data["conversion_rates"][currency_to]
    result = amount * rate

    transaction = Transaction(
        user_id=user_id,
        currency_from=currency_from,
        currency_to=currency_to,
        amount=amount,
        result=result,
    )
    db.add(transaction)
    db.commit()
    return {"success": True, 
            "result": result
            }