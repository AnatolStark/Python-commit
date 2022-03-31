from functools import wraps


def prohibit_kwargs(func):  #  prohibit - zapretit
    @wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError('Keyword arguments are prohibited')
        return func(*args, **kwargs)
    return wrapper


def prohibit_int_arguments(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for val in args:
            if type(val) == int:
                raise ValueError('Integer arguments are prohibited')
        for key, val in kwargs.items():
            if type(val) == int:
                raise ValueError('Integer arguments are prohibited')
        return func(*args, **kwargs)
    return wrapper


#   @prohibit_int_arguments #  pri etoi funkzii pojavljaetsja oshibka
#   ValueError: Integer arguments are prohibited
@prohibit_kwargs
def print_hello(name):
    print(f'Hello {name}!')


print_hello('Jack')
print_hello(3)
#  Hello Jack!
# Hello 3!

def prohibit_more_than_2_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) < 3:
            return func(*args, **kwargs)
        else:
            raise ValueError("Function must have less than 3 arguments!")
    return wrapper



@prohibit_more_than_2_args
def func_1(a, b):
    return'2 args'




print(func_1(2, 'arg'))
# 2 args
print(func_1('more than', 2, 'args'))
#  raise ValueError("Function must have less than 3 arguments!")





