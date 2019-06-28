"""
Configure API and routes.
"""
import json
import os
from pymongo import MongoClient

from flask_api import FlaskAPI
from flask_cors import CORS
from flask_pymongo import PyMongo
from urllib.parse import quote_plus

from bson import ObjectId

from marketAPI.config import *

from marketAPI.routes.healthcheck import healthcheck
from marketAPI.routes.users import users
from marketAPI.routes.market import market

from marketAPI.services.MarketData import MarketData


class JSONEncoder(json.JSONEncoder):
    """
    Custom JSON Encoder.
    """

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


def connect_db(app):
    """
    Given an App, connect to a mongo db.
    """

    db_conn_str = app.config["db_conn_str"]

    if db_conn_str is None:
        raise Exception("DB Conn String is undefined in Configuration!")

    # Configure DB
    app.config["MONGO_URI"] = db_conn_str + "/marketdb"

    return PyMongo(app)


def generate_config(environment):
    """
    Based on the environment, select a config class from config.py
    Config is stored in app.config
    """
    if environment is None:
        raise ValueError("Environment is None. Is `DEPLOYMENT_ENV` env var set?")

    print(f"Deploying to {environment}")
    environment = environment.lower()
    if environment == "local":
        return LocalConfig().build_config_dictionary()
    elif environment == "dev":
        return DevConfig().build_config_dictionary()
    elif environment == "prod":
        return ProdConfig().build_config_dictionary()
    else:
        raise ValueError(f"INVALID CONFIGURATION PROVIDED: {environment}")


def create_app(config):
    """
    Given a configuration, create a MarketAPI Application
    """

    # Configure the application
    app = FlaskAPI(__name__)
    target_env = os.getenv("DEPLOYMENT_ENV")
    app.config.update(generate_config(app, target_env))
    CORS(app)

    # Configure app routing
    app.register_blueprint(healthcheck)
    app.register_blueprint(users)
    app.register_blueprint(market)

    app.json_encoder = JSONEncoder

    # Configure the Database
    app.mongo = connect_db(app)

    # Configure Services
    app.market_data = MarketData(app.config)

    return app
