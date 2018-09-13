"""
Configure API and routes.
"""

from flask import Flask
from flask_pymongo import PyMongo

from MarketAPI.routes.healthcheck import healthcheck
from MarketAPI.routes.users import users


APP = Flask(__name__)
APP.config["MONGO_URI"] = "mongodb://localhost:27017/WatchList"
APP.register_blueprint(healthcheck)
APP.register_blueprint(users)

# Configure DB
APP.mongo = PyMongo(APP)
