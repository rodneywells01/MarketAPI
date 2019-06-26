from flask import Blueprint, jsonify, current_app, request, abort
from marketAPI.errors import *

@current_app.errorhandler(APIError)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response