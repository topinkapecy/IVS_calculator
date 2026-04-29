import re


def sqrt(x, n=2):
    return x**(1/n)
def factorial(x):
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
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b

def power(a, b):
    return a ** b

def percentage(a):
    return a / 100

def evaluate(expression):
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