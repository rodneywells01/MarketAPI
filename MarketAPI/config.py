import os

class BaseConfig: 
	iex_token = os.getenv("IEX_TOKEN")

class DevConfig(BaseConfig): 
	iex_base = "https://sandbox.iexapis.com/v1"

class ProdConfig(BaseConfig):
	iex_base = "https://cloud.iexapis.com/v1"