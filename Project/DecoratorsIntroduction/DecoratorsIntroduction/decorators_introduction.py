# def simple_function():
#     #  print('Some code before the old code')
#     print('Simple function code')
      #  print('Some code after the old code')

#   Simple function code
#
# simple_function()

# decorated_function = decorator_function(simple_function)
#
# decorated_function()


# def decorator_function(original_function):
#     def wrap_function():  #  wrap - obertochnaja
#         print('Some code before the old code')
#         original_function()
#         print('Some code after the old code')
#     return wrap_function
#
#
# @decorator_function   #  @ -otkluchenie funkzii
# def simple_function():
#     print('Simple function code')


# simple_function()

def make_compliment(func):
    def wrapper(*args, **kwargs):  #  s pomoshiu *args, **kwargs funkzija stanovitsja gibkoi
        print('Nice to meet you!')
        func(*args, **kwargs)
        print('You look great!')
    return wrapper


@make_compliment
def ask_name():
    print('What is your name?')
    #  Nice to meet you!
    # What is your name?
    # You look great!


ask_name()


@make_compliment
def say_name(name):
    print('My name is ' + name)


say_name('Jack')
#  Nice to meet you!
# My name is Jack
# You look great!

@make_compliment
def order(food, drink):
    print(f'Give me {food} and {drink}')


order(food='chips', drink='kola')
#  Nice to meet you!
# Give me chips and kola
# You look great!

def hello_from_decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper


@hello_from_decorator
def say_greeting():
    print('Hello from decorator!')


say_greeting()










