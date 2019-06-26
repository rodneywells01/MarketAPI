import os
import tempfile
import pytest
from mock import Mock

import marketAPI


@pytest.fixture
def client():
    """
	Create and configure a new app instance for each test.
	"""

    # create a temporary file to isolate the database for each test
    db_fd, db_path = tempfile.mkstemp()

    marketAPI.connect_db = Mock(return_value=None)

    # create the app with common test config
    app = marketAPI.create_app({"TESTING": True, "DATABASE": db_path})

    # Mocked DB Responses
    app.mongo = Mock(
        db=Mock(
            users=Mock(
                find_one=Mock(
                    return_value={"_id": "123", "age": 23, "name": "Rodney Wells"}
                )
            )
        )
    )

    yield app.test_client()

    # close and remove the temporary database
    os.close(db_fd)
    os.unlink(db_path)


def test_get_user(client):
    result = client.get("/test")
    print(result.data)
