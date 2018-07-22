from flask import Flask
from MarketAPI.routes.healthcheck import healthcheck

app = Flask(__name__)

app.register_blueprint(healthcheck)


