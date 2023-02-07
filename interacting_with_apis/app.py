import time
from libs.openexchange import OpenExchangeClient

APP_ID = "d75c474df75743c4982446e9a7bb7f8a"

client = OpenExchangeClient(APP_ID)

usd_amount = 1000

start = time.time()
gbd_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()

print(end - start)

print(f"USD {usd_amount} is GBP {gbd_amount:.2f}")
