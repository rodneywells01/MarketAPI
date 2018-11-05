import os
import tempfile
import pytest
from mock import Mock

from MarketAPI import create_app, connect_db

# https://github.com/pallets/flask/blob/1.0.2/examples/tutorial/tests/conftest.py
@pytest.fixture
def client():
	"""
	Create and configure a new app instance for each test.
	"""
	
	# create a temporary file to isolate the database for each test
	db_fd, db_path = tempfile.mkstemp()

	connect_db = Mock(return_value=None)

	# create the app with common test config
	app = create_app({
		'TESTING': True,
		'DATABASE': db_path,
	})

	yield app.test_client()

	# close and remove the temporary database
	os.close(db_fd)
	os.unlink(db_path)

def test_healthcheck(client): 
	response = client.get("/health")
	print("Hello")
	assert response.status_code == 200
	