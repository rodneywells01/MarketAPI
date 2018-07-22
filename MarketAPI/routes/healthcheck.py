from flask import Blueprint, jsonify

healthcheck = Blueprint('health_check', __name__,
			template_folder='templates')

@healthcheck.route('/health')
def health_check():
	return ""
