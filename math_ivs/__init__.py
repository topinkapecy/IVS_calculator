def sqrt(x):
    return x**(1/2)
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
