"""
Generic, reusable app fixture.
"""

import tempfile
import os
import pytest

from mock import MagicMock

import marketAPI

@pytest.fixture
def client():
    """
	Create and configure a new client instance for each test.
	"""

    # create a temporary file to isolate the database for each test
    db_fd, db_path = tempfile.mkstemp()

    marketAPI.connect_db = MagicMock(return_value=None)
    marketAPI.set_configuration = MagicMock()

    # create the app with common test config
    app = marketAPI.create_app({"TESTING": True, "DATABASE": db_path})

    # Mocked DB Responses
    app.mongo = MagicMock(
        db=MagicMock(
            users=MagicMock(
                find_one=MagicMock(
                    return_value={"_id": "123", "age": 23, "name": "Rodney Wells"}
                )
            )
        )
    )

    yield app.test_client()

    # close and remove the temporary database
    os.close(db_fd)
    os.unlink(db_path)