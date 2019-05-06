"""
Configure API and routes.
"""

import json
from flask import Flask
from flask_pymongo import PyMongo

from bson import ObjectId

from MarketAPI.routes.healthcheck import healthcheck
from MarketAPI.routes.users import users


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

    # Configure DB
    app.config["MONGO_URI"] = "mongodb://localhost:27017/marketdb"
    return PyMongo(app)


def create_app(config):
    """
	Given a configuration, create a MarketAPI Application
	"""

    # TESTing = True, Database = DB PAth
    app = Flask(__name__)

    if app.config["TESTING"]:
        # Spin up a DB
        pass

    app.register_blueprint(healthcheck)
    app.register_blueprint(users)
    app.json_encoder = JSONEncoder

    app.mongo = connect_db(app)

    return app
