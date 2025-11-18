# https://github.com/hatchkor/lab11-RH-YH.git
import math
def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(a, b):
    try:
        math.log(b, a)
    except ValueError as e:
        print(f"{e} for a or b results in undefined output.")
    math.log(b, a)

def exp(a, b):
    return a**b




