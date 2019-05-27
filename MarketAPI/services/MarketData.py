import requests

class MarketData:
	def __init__(self, config):
		self.url = config.iex_base
		self.token = config.iex_token

	def _request(route):
		target = self.url + route + f"?token={self.token}"
		res = requests.get(target)

		if res.status_code > 400: 
			raise Exception(f"ERROR CODE [{res.status_code}] hitting '{target}'")

		return res.json()

	def fetch_data(route): 
		return _request(route)

	def fetch_price(ticker): 
		pass
