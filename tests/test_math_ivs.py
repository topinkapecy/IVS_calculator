import pytest

import math_ivs


def test_factorial_values():
    assert math_ivs.factorial(0) == 1
    assert math_ivs.factorial(1) == 1
    assert math_ivs.factorial(5) == 120
    assert math_ivs.factorial(7) == 5040

@pytest.mark.parametrize(
    "value, expected",
    [
        (0, 0),
        (1, 1),
        (4, 2),
        (49, 7),
        (2.25, 1.5),
        (2, 1.414214)
    ],
)
def test_sqrt_common_values(value, expected):
    assert math_ivs.sqrt(value) == pytest.approx(expected)
