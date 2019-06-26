"""
Capture User information
"""

from flask import Blueprint, jsonify, current_app, request, abort
from marketAPI.errors import *
# from bson import json_util as bson
from flask_api import FlaskAPI, status, exceptions


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







@users.route("/test")
def db_test():
    """
	Testing Database connectivity. Try to grab one user.
	"""
    result = current_app.mongo.db.users.find_one()
    return jsonify(result)
