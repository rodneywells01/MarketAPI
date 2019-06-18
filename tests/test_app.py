"""
Testing App Creation
"""
import pytest
from mock import MagicMock

import marketAPI

def test_configuration():
    fake_app = MagicMock()
    for env in ["local", "dev", "prod"]:
        marketAPI.set_configuration(fake_app, env)
        assert fake_app.config.update.called

def test_configuration_bad_env():
    fake_app = MagicMock()
    with pytest.raises(ValueError):
        marketAPI.set_configuration(fake_app, "nonexistent_env")