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


def connect_db(app): 
	# Configure DB
	app.config["MONGO_URI"] = "mongodb://localhost:27017/WatchList"
	return PyMongo(app)

	# Debug stuff 
	print(type(app.mongo))
	print(type(app.mongo.db))
	print(type(app.mongo.cx))


def create_app(config):
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
