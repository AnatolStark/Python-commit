from functools import wraps

#
# def check_if_first_arg_is(value):  #  dekorator s argumentom
#     def inner_dec(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             if args and args[0] != value:
#                 print(f'First argument has to be {value}')
#             return func(*args, **kwargs)
#         return wrapper
#     return inner_dec
#
#
# @check_if_first_arg_is('red')
# def print_rainbow_colors(*colors):
#     print(colors)
#
#
# @check_if_first_arg_is(7)
# def multiply_7(a, b):
#     return a * b
#
#
# print_rainbow_colors('orange', 'yellow', 'green', 'blue',
#                      'indigo', 'violet')
# First argument has to be red
# ('orange', 'yellow', 'green', 'blue','indigo', 'violet')

#
# print(multiply_7(7, 3))
# 21
# print(multiply_7(8, 3))
# First argument has to be 7
# 24



def enforce(*types):  # enforce - prinushdan
    def inner_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            new_args = []
            for a, t in zip(args, types): # zip - novaja posledovatelnost
                new_args.append(t(a))
            return func(*new_args, **kwargs)
        return wrapper
    return inner_dec


@enforce(str, int)
def print_text_n_times(text, n):
    for number in range(n):
        print(text)


print_text_n_times('Hi!', '3')
# Hi!
# Hi!
# Hi!

# *args - ('Hi!', '3')  # ()- forma tupl
# *types - (str, int)
# zip(args, types) - ('Hi!', str) ('3', int)


@enforce(float, float)
def divide(a, b):
    return a / b


print(divide(4, 2))
# 2.0
print(divide('4', '2'))
# 2.0

from functools import wraps
from time import sleep



def wait(n):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            sleep(n)
            print("There was a pause {} seconds before execution {}".format(n, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return inner


@wait(1.5)
def func_1():
    return 'Hi!'


print(func_1())







