from pydantic import BaseModel

class ExchangeRequest(BaseModel):
    user_id: str
    currency_from: str
    currency_to: str
    amount: float

    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "1",
                "currency_from": "USD",
                "currency_to": "MXN",
                "amount": 250
            }
        }
