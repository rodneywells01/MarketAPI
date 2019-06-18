"""
Class based configuration values for various environments.
"""

import os
import inspect

class BaseConfig:
    """
    Base Configuration
    """
    iex_token = os.getenv("IEX_TOKEN")

    def build_config_dictionary(self):
        """
        Fetch all values in the Config to generate a dictionary
        of configuration values
        """

        members = inspect.getmembers(self, lambda a: not inspect.isroutine(a))
        return dict(
            [attribute for attribute in members if attribute[0][:2] != "__"]
        )

class LocalConfig(BaseConfig):
    """
    Local Configuration
    """
    iex_base = "https://sandbox.iexapis.com/v1"
    mongo_uri = "mongodb://mongodb:27017"
    db_conn_str = "mongodb://mongodb:27017"

class DevConfig(BaseConfig):
    """
    Dev Configuration
    """
    iex_base = "https://sandbox.iexapis.com/v1"
    mongo_uri = ""
    db_conn_str = ""

class ProdConfig(BaseConfig):
    """
    Prod Configuration
    """
    iex_base = "https://cloud.iexapis.com/v1"
    mongo_uri = ""
    db_conn_str = ""
