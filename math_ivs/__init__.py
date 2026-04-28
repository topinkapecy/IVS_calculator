def sqrt(x):
    return x**(1/2)
def factorial(x):
    res = 1
    for i in range(x+1):
        if i == 0:
            continue
        else:
            res *= i
    return res
