"""Test math utilities."""

from commons.math_utils import math_sum


def test_math_sum() -> None:
    """Tests math_sum."""
    result = math_sum(1, 10)
    assert result == 11
