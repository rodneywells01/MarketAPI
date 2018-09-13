"""
Capture User information
"""


from flask import Blueprint, jsonify, current_app
from bson import json_util as bson

users = Blueprint('users', __name__, template_folder='templates')


@users.route('/test')
def db_test():
    """
    Testing Database connectivity. Try to grab one user.
    """
    result = bson.dumps(current_app.mongo.db.users.find_one())
    print(result)

    return jsonify(result)


@users.route('/users')
def get_users():
    pass
