"""
Exceptions for invalid requests.
http://flask.pocoo.org/docs/1.0/patterns/apierrors/
"""
from flask import jsonify

class APIError(Exception):
    """
    Basic API Error Class
    """
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


class NotFoundError(APIError):
    status_code = 404

class BadRequestError(APIError):
    status_code = 400

