def add(a, b):
    try:
        # if isinstance(a, int) or isinstance(a, float) or isinstance(b, int) or isinstance(b, float):
        #     raise TypeError
        return a + b
    except TypeError:
        print('a and b must be valid numbers')
def subtract(a, b):
    try:
        return a - b
    except TypeError:
        print('a and b must be valid numbers')
def multiply(a, b):
    try:
        return a * b
    except TypeError:
        print('a and b must be valid numbers')
def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('can not devide a by 0')
    except TypeError:
        print('a and b must be valid numbers')