"""
Configure API and routes.
"""

from flask import Flask
from flask_pymongo import PyMongo

from MarketAPI.routes.healthcheck import healthcheck
from MarketAPI.routes.users import users

import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

def create_app(config):
	app = Flask(__name__)
	app.config["MONGO_URI"] = "mongodb://localhost:27017/WatchList"
	app.register_blueprint(healthcheck)
	app.register_blueprint(users)
	app.json_encoder = JSONEncoder

	# Configure DB
	app.mongo = PyMongo(app)

	return app


