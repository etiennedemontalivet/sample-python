""" Test exampe using version
"""
from app_example import __version__


def test_version():
    """Test version"""
    assert __version__ == "0.1.0"
