import requests

def get_quote(currency_from: str, currency_to: str, amount: float) -> dict:
    api_url = f"https://v6.exchangerate-api.com/v6/cbb56a87b9a2c0ad47eb558c/latest/{currency_from}"
    response = requests.get(api_url)
    data = response.json()

    if response.status_code != 200:
        raise Exception("Error getting exchange rate")
    
    rate = data["conversion_rates"].get(currency_to)
    if not rate:
        raise Exception("This currency is not valid")
    
    return {"rate": rate, "converted_amount": rate * amount}
