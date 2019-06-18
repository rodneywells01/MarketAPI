"""
Configure API and routes.
"""
from pymongo import MongoClient
import json
from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo
from urllib.parse import quote_plus

from bson import ObjectId

from marketAPI.config import *

from marketAPI.routes.healthcheck import healthcheck
from marketAPI.routes.users import users

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


def set_configuration(app, environment):
    """
    Based on the environment, select a config class from config.py
    Config is stored in app.config
    """
    if environment is None:
        app.logger.info(environment)
        raise ValueError("Environment is None. Is `DEPLOYMENT_ENV` env var set?")

    app.logger.info(f"Deploying to {environment}")
    environment = environment.lower()
    if environment == 'local':
        app.config.update(LocalConfig().build_config_dictionary())
    elif environment == 'dev':
        app.config.update(DevConfig().build_config_dictionary())
    elif environment == 'prod':
        app.config.update(ProdConfig().build_config_dictionary())
    else:
        raise ValueError(f"INVALID CONFIGURATION PROVIDED: {environment}")
    app.logger.info(app.config)


def create_app(config):
    """
    Given a configuration, create a MarketAPI Application
    """

    # Configure the application
    app = Flask(__name__)
    target_env = os.getenv("DEPLOYMENT_ENV")
    set_configuration(app, target_env)
    CORS(app)

    # Configure app routing
    app.register_blueprint(healthcheck)
    app.register_blueprint(users)
    app.json_encoder = JSONEncoder

    # Configure the Database
    app.mongo = connect_db(app)

    return app
