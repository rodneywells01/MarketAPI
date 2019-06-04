"""
Class based configuration values for various environments.
"""

import os

class BaseConfig:
    """
    Base Configuration
    """
    iex_token = os.getenv("IEX_TOKEN")

class DevConfig(BaseConfig):
    """
    Dev Configuration
    """
    iex_base = "https://sandbox.iexapis.com/v1"

class ProdConfig(BaseConfig):
    """
    Prod Configuration
    """
    iex_base = "https://cloud.iexapis.com/v1"
