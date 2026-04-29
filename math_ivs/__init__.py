
"""!
@file math_ivs.py
@brief Mathematical library for the calculator application.

@details This library provides basic and advanced mathematical operations
including addition, subtraction, multiplication, division, factorial,
power,percentage, and root functions and evaluates them for immediate use

@author Samuel Cehlarik
@date 2026
@version 1.0

@copyright GNU GPL v3
"""
import re


def sqrt(x, n=2):
    """!
    @brief Calculates the n-th root of a number and rounds to first 6 digits.
    @param x First number
    @param n Default is set to be 2 -> it's the nth root
    @throws ValueError root degree is zero or the root is negative number
    @return The nth root of x

    """
    if n == 0:
        raise ValueError("Root degree cannot be zero")
    if x < 0:
        raise ValueError("Root of negative number is not supported")
    return round(x ** (1 / n), 6)


def factorial(x):
    """!
    @brief Calculates the factorial of a number(x).
    @param x Number
    @throws ValueError if the number is negative
    @return Factorial of a number

    """
    if not isinstance(x, int):
        raise ValueError("Factorial only supports integers")
    res = 1
    if x < 0:
        raise ValueError("Negative factorial not allowed")
    for i in range(x+1):
        if i == 0:
            continue
        else:
            res *= i
    return res


def add(a, b):
    """!
    @brief Calculates the addition of two numbers.
    @param a First number
    @param b Second number
    @return addition of numbers

    """
    return a + b


def subtract(a, b):
    """!
    @brief Calculates the subtraction of two numbers.
    @param a First number
    @param b Second number
    @return subtraction of numbers

    """
    return a - b


def multiply(a, b):
    """!
    @brief Calculates the multiplication of two numbers.
    @param a First number
    @param b Second number
    @return Multiplication of numbers

    """
    return a * b


def divide(a, b):
    """!
    @brief Calculates the division of two numbers.
    @param a First number
    @param b Second number
    @throws ValueError if b is zero
    @return division of numbers

    """
    if b == 0:
        raise ValueError("Division by zero")
    return a / b


def power(a, b):
    """!
    @brief Calculates the a (number) to the power of b (number).
    @param a First number
    @param b Second number (power)
    @return a^b

    """
    return a ** b


def percentage(a):
    """!
    @brief Converts a number to its percentage value.
    @param a number to convert.
    @return The value of a divided by 100.
    """
    return a / 100


def evaluate(expression):
    """!
    @brief Evaluates the expression using all the functions defined above.
    @param expression A string form of the mathematical expression to solve.
    @return The evaluated result of the expression.
    @throws SyntaxError If the expression is invalid.
    @throws ValueError If the expression contains unsupported operations.
    """
    expression = expression.replace("×", "*").replace("÷", "/").replace("^", "**")
    expression = re.sub(r'(\d+)!', r'factorial(\1)', expression)  # 5! -> factorial(5)
    expression = re.sub(r'(\d+)√(\d+(?:\.\d+)?)', r'sqrt(\2,\1)', expression)  # 3√8 -> sqrt(8,3)
    expression = re.sub(r'√(\d+(?:\.\d+)?)', r'sqrt(\1)', expression)  # √9 -> sqrt(9)
    expression = re.sub(r'\b0+(\d+)', r'\1', expression)  # 09 -> 9, 007 -> 7
    return eval(expression, {"__builtins__": {}}, {
        "add": add, "subtract": subtract, "multiply": multiply,
        "divide": divide, "power": power, "sqrt": sqrt,
        "factorial": factorial, "percentage": percentage,
    })
