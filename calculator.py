import math
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def log(a, b):
    try:
        return math.log(b, a)
    except ValueError as e:
        print(f"{e} for a or b results in undefined output.")

def exp(a, b):
    return a**b




