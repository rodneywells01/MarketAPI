"""
Capture User information
"""

from flask import Blueprint, jsonify, current_app, request, abort
from marketAPI.errors import *
# from bson import json_util as bson

users = Blueprint("users", __name__, template_folder="templates")

@users.route("/user", methods=["POST"])
def create_user():
    req = request.get_json()

    # Register a user in our database.
    username = req.get("username")
    if username is None:
        raise NotFoundError(f"`username` was not specified in body!")

    current_app.mongo.db.users.insert_one({"username": username})

@users.route("/user", methods=["GET"])
def get_user():
    req = request.get_json()

    # Find a user in our database.
    username = req.get("username")
    if username is None:
        raise NotFoundError(f"`username` was not specified in body!")
    user_data = current_app.mongo.db.users.find_one({"username": username})

    return jsonify(user_data)







@users.route("/test")
def db_test():
    """
	Testing Database connectivity. Try to grab one user.
	"""
    result = current_app.mongo.db.users.find_one()
    return jsonify(result)
