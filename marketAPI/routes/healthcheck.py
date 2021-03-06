"""
Health check information to verify the API is functioning properly.
"""
from flask import Blueprint, jsonify

healthcheck = Blueprint("health_check", __name__, template_folder="templates")


@healthcheck.route("/health")
def health_check():
    """
	Verify API is alive
	"""
    return jsonify({"status": "Alive"})
