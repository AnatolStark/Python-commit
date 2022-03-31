from functools import wraps


def print_function_data(function):
    """
    This is decorator function
    :param function:
    :return:
    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"You are using {function.__name__}")
        print(f"Function documentation {function.__doc__}")
        return function(*args, **kwargs)
    return wrapper


@print_function_data
def squares_sum(a, b):
    """

    :param a: first number
    :param b: second number
    :return: sum of squares first and second numbers: (a * a + b * b)
    """
    return a * a + b * b


# print(squares_sum(2, 3))
# 13
print(squares_sum.__doc__)
#   :param a: first number
#     :param b: second number
#     :return: sum of squares first and second numbers: (a * a + b * b)
print(squares_sum.__name__)
#  squares_sum
help(squares_sum)
#  Help on function squares_sum in module __main__:
#  squares_sum(a, b)
#     :param a: first number
#     :param b: second number
#     :return: sum of squares first and second numbers: (a * a + b * b)



def print_args(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print('*args', *args)
        print('**kwargs', **kwargs)
        return function(*args, **kwargs)
    return wrapper


@print_args
def function_1():
    print('arg')

function_1()
#  *args
# **kwargs
# arg

def hello_from_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return str(result) + ' ' + 'Hello from decorator!'
    return wrapper


@hello_from_decorator
def funk_1():
    return 'Programmer!'


print(funk_1())

