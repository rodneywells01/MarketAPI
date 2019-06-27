"""
Market Data exposure
"""
from flask import Blueprint, jsonify, current_app

from marketAPI.services.MarketData import *

market = Blueprint("market", __name__, template_folder="templates")

@market.route("/market/<ticker>", methods=["GET"])
def get_stock_info(ticker):
    """
	Fetch basic information about a stock.
	"""
    return jsonify(
        {
            "ticker": ticker,
            "price": current_app.market_data.fetch_price(ticker)
        }
    )


    # return jsonify({"status": "Alive"})
