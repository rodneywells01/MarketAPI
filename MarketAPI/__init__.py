"""
Configure API and routes.
"""
from flask import Flask
from MarketAPI.routes.healthcheck import healthcheck

APP = Flask(__name__)

APP.register_blueprint(healthcheck)
