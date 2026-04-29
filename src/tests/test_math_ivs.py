import sys
from pathlib import Path

import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import math_ivs


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-2, 3, 1),
        (0, 0, 0),
        (2.5, 1.5, 4.0),
    ],
)
def test_addition(a, b, expected):
    assert math_ivs.add(a, b) == pytest.approx(expected)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 4, 6),
        (-2, -3, 1),
        (0, 5, -5),
        (2.5, 1.5, 1.0),
    ],
)
def test_subtraction(a, b, expected):
    assert math_ivs.subtract(a, b) == pytest.approx(expected)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 7, 42),
        (-3, 4, -12),
        (-3, -4, 12),
        (0, 10, 0),
        (2.5, 4, 10.0),
    ],
)
def test_multiplication(a, b, expected):
    assert math_ivs.multiply(a, b) == pytest.approx(expected)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (8, 2, 4),
        (7, 2, 3.5),
        (-12, 3, -4),
        (0, 5, 0),
    ],
)
def test_division(a, b, expected):
    assert math_ivs.divide(a, b) == pytest.approx(expected)


def test_division_by_zero_error():
    with pytest.raises(ValueError):
        math_ivs.divide(5, 0)


@pytest.mark.parametrize(
    "value, expected",
    [
        (0, 1),
        (1, 1),
        (3, 6),
        (5, 120),
    ],
)
def test_factorial_valid_values(value, expected):
    assert math_ivs.factorial(value) == expected


@pytest.mark.parametrize("value", [-1, -5, -10])
def test_factorial_negative_values_error(value):
    with pytest.raises(ValueError):
        math_ivs.factorial(value)


@pytest.mark.parametrize("value", [2.5, 5.5])
def test_factorial_invalid_input_error(value):
    with pytest.raises((TypeError, ValueError)):
        math_ivs.factorial(value)


@pytest.mark.parametrize(
    "base, exponent, expected",
    [
        (2, 0, 1),
        (2, 1, 2),
        (2, 4, 16),
        (3, 3, 27),
        (-2, 3, -8),
        (-2, 4, 16),
        (4, 0.5, 2)
    ],
)
def test_power_with_natural_exponents(base, exponent, expected):
    assert math_ivs.power(base, exponent) == pytest.approx(expected)

@pytest.mark.parametrize(
    "value, degree, expected",
    [
        (0, 2, 0),
        (1, 2, 1),
        (4, 2, 2),
        (2.25, 2, 1.5),
        (2, 2, 1.414214),
        (8, 3, 2),
    ],
)
def test_root_valid_values(value, degree, expected):
    assert math_ivs.sqrt(value, degree) == pytest.approx(expected, rel=1e-6)


@pytest.mark.parametrize("degree",[4,2])
def test_root_of_negative_number_error(degree):
    with pytest.raises(ValueError):
        math_ivs.sqrt(-16, degree)

@pytest.mark.parametrize(
    "value, expected",
    [
        (50, 0.5),
        (100, 1.0),
        (-25, -0.25),
        (2.5, 0.025),
    ],
)
def test_percentage(value, expected):
    assert math_ivs.percentage(value) == pytest.approx(expected)


@pytest.mark.parametrize(
    "expression, expected",
    [
        ("2+3", 5),
        ("10-4", 6),
        ("6×7", 42),
        ("8÷2", 4),
        ("2^4", 16),
        ("3-5!", -117),
        ("4!+2^4", 40),
        ("√49", 7),
        ("3√8", 2),
        ("09+1", 10),
    ],
)
def test_valid_calculator_expression(expression, expected):
    assert math_ivs.evaluate(expression) == pytest.approx(expected, rel=1e-6)


@pytest.mark.parametrize(
    "expression",
    [
        "5÷0",
        "5.5!",
        "√-9",
        "0√16",
        "",
    ],
)
def test_invalid_calculator_expression_error(expression):
    with pytest.raises(Exception):
        math_ivs.evaluate(expression)
