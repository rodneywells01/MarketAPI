import os
import tempfile
import pytest
from mock import Mock, MagicMock

import marketAPI

from tests.general_fixtures.app import client

def test_get_user(client):
    result = client.get("/test")
    print(result.data)
