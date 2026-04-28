import sys
from pathlib import Path

import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


import math_ivs


@pytest.mark.parametrize(
    "value, expected",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (5, 120),
        (7, 5040),
    ],
)
def test_factorial_valid_values(value, expected):
    assert math_ivs.factorial(value) == expected


@pytest.mark.parametrize(
    "value",
    [
        -1,
        -5,
        -10,
    ],
)
def test_factorial_negative_values_raise_error(value):
    with pytest.raises(ValueError):
        math_ivs.factorial(value)


@pytest.mark.parametrize(
    "value",
    [
        2.5,
        5.5,
        "5",
        None,
    ],
)
def test_factorial_invalid_input_types_raise_error(value):
    with pytest.raises((TypeError, ValueError)):
        math_ivs.factorial(value)


@pytest.mark.parametrize(
    "value, expected",
    [
        (0, 0),
        (1, 1),
        (4, 2),
        (9, 3),
        (49, 7),
        (2.25, 1.5),
        (2, 1.414214),
    ],
)
def test_sqrt_valid_values(value, expected):
    assert math_ivs.sqrt(value) == pytest.approx(expected, rel=1e-6)


@pytest.mark.parametrize(
    "value",
    [
        -1,
        -9,
        -100,
    ],
)
def test_sqrt_negative_values_raise_error(value):
    with pytest.raises(ValueError):
        math_ivs.sqrt(value)


@pytest.mark.parametrize(
    "value",
    [
        "abc",
        None,
    ],
)
def test_sqrt_invalid_input_types_raise_error(value):
    with pytest.raises((TypeError, ValueError)):
        math_ivs.sqrt(value)
