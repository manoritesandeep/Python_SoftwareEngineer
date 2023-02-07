import requests

APP_ID = "d75c474df75743c4982446e9a7bb7f8a"
ENDPOINT = "https://openexchangerates.org/api/latest.json"

response = requests.get(f"{ENDPOINT}?app_id={APP_ID}")
exchange_rates = response.json()['rates']
#print(exchange_rates)

usd_amount = 1000
gbd_amount = usd_amount * exchange_rates["GBP"]
print(f"USD {usd_amount} is GBP {gbd_amount}")