import pyEX
from MarketAPI.config import DevConfig as Config
import requests

url = Config.iex_base
url = "https://sandbox.iexapis.com/v1"
endpoint = "/stock/TSLA/quote"
token = "Tsk_62259f60e6c94f40978849d06316efb3"
auth = f"?token={token}"
target = url + endpoint + auth
print(target)
req = requests.get(target)

print(req)
print(req.text)

