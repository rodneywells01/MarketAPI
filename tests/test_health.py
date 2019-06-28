import os
import tempfile
import pytest
from mock import Mock

from marketAPI import create_app, connect_db
from tests.general_fixtures.app import client

# https://github.com/pallets/flask/blob/1.0.2/examples/tutorial/tests/conftest.py


def test_healthcheck(client):
    response = client.get("/health")
    assert response.status_code == 200
