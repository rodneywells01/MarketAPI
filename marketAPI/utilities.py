from flask_api import exceptions

def get_from_req(request, value):
    """
    Get a value from a request
    """

    val = request.get(value)
    if val is None:
        raise exceptions.NotFound(f"`{value}` was not specified in body!")

    return val