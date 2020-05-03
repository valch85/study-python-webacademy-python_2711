from functools import wraps

def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " function was called")
        return func(*args, **kwargs)
    return with_logging

def logged2(func):
    def with_logging(*args, **kwargs):
        print(func.__name__ + " function was called")
        return func(*args, **kwargs)
    return with_logging

@logged
def summ(x):
    """does some math"""
    return x + x + x

@logged2
def mult(x):
    """does some math"""
    return x * x * x

print(f"result of the function is {summ(3)}")

print(f"result of the function is {mult(3)}")