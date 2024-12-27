from pydantic import BaseModel

class ExchangeRequest(BaseModel):
    user_id: str
    currency_from: str
    currency_to: str
    amount: float

    class Config:
        schema_extra = {
            "example": {
                "user_id": "123e4567-e89b-12d3-a456-426614174000",
                "currency_from": "USD",
                "currency_to": "MXN",
                "amount": 250
            }
        }
