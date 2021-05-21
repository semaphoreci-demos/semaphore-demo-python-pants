"""Tests main.py."""

from hello_world.main import message


def test_message() -> None:
    """Tests hello message."""
    assert message() == "Hi world"
