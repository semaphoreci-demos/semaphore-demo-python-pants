"""Prints Hi world in green."""

from colors import green  # type: ignore
from commons.string_utils import string_concat


def message():
    """returns 'Hi world'."""
    return string_concat("Hi", " world")


def print_message():
    """Prints message in green."""
    print(green(message()))


if __name__ == "__main__":
    print_message()
