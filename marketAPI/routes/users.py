"""
Capture User information
"""

from flask import Blueprint, jsonify, current_app, request, abort
# from bson import json_util as bson
from flask_api import FlaskAPI, status, exceptions

from marketAPI import utilities


users = Blueprint("users", __name__, template_folder="templates")

@users.route("/user", methods=["POST"])
def create_user():
    req = request.get_json()

    # Register a user in our database.
    username = req.get("username")
    if username is None:
        raise exceptions.NotFound(f"`username` was not specified in body!")

    current_app.mongo.db.users.insert_one({"username": username})

    return jsonify(), 201

@users.route("/user/<username>", methods=["GET"])
def get_user(username):
    if username is None:
        raise exceptions.ParseError("`username` not provided!")
    user_data = current_app.mongo.db.users.find_one({"username": username})

    if user_data is None:
        raise exceptions.NotFound(f"User {username} not found in users table")
    return jsonify(user_data)

@users.route("/user/<username>/watchlists", methods=["GET"])
def get_watchlists(username):
    """
    Get all watchlists for a user
    """
    if not current_app.mongo.db.users.find_one({ "username": username }):
        raise exceptions.NotFound(f"User {username} does not exist")

    user = current_app.mongo.db.users.find_one({"username": username})
    # .get("watchlists")
    return jsonify({"watchlists": user.get("watchlists")})

@users.route("/user/<username>/watchlists/<watchlist_name>", methods=["GET"])
def get_watchlist(username, watchlist_name):
    """
    Get a specific watchlist for a user
    """

    # TODO: Fill in Watchlist data?
    return jsonify({"watchlist": _get_watchlist(username, watchlist_name)})


def _get_watchlist(username, watchlist_name):
    """
    Attempt to fetch a specific watchlist from a user
    """
    if not current_app.mongo.db.users.find_one({ "username": username }):
        raise exceptions.NotFound(f"User {username} does not exist")

    record = current_app.mongo.db.users.find_one({"username": username, "watchlists.watchlist_name": watchlist_name})
    if not record:
        raise exceptions.NotFound(f"Watchlist {watchlist_name} not found")

    return record["watchlists"][0]

@users.route("/user/<username>/watchlists", methods=["POST"])
def create_watchlist(username):
    req = request.get_json()

    watchlist_name = utilities.get_from_req(req, "watchlist_name")
    ticker_list = req.get("tickers", [])

    try:
        _get_watchlist(username, watchlist_name)

        raise exceptions.ParseError(f"`{watchlist_name}` already exists!`")
    except exceptions.NotFound:
        print("Creating watchlist for user")

    watchlist = {
        "watchlist_name": watchlist_name,
        "ticker_list": ticker_list
    }

    current_app.mongo.db.users.update(
        {"username": username },
        {
            "$set": {
                "watchlists": [watchlist]
            }
        }
    )

    return jsonify(), 201
