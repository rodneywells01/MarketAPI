"""
Market Data exposure
"""
from flask import Blueprint, jsonify

from marketAPI.services.MarketData import *

market = Blueprint("market", __name__, template_folder="templates")

@market.route("/market")
def health_check():
    """
	Verify API is alive
	"""
    return jsonify({"status": "Alive"})
