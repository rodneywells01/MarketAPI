"""
Testing App Creation
"""
import pytest
from mock import MagicMock

import marketAPI

def test_configuration():
    fake_app = MagicMock()
    for env in ["local", "dev", "prod"]:
        marketAPI.generate_config(env)

def test_configuration_bad_env():
    fake_app = MagicMock()
    with pytest.raises(ValueError):
        marketAPI.generate_config("nonexistent_env")