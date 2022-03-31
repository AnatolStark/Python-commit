# *args and **kwargs

# # *args
# def func_with_args(*args):
#     print(args)
#
#
# func_with_args(1, 2, 3)

# def ten_percent_of_product(x, y, z):
#     return (x * y * z) * 0.1
#
#
# print(ten_percent_of_product(10, 20, 7))

# def ten_percent_of_product_with_args(*args):
#     product = 1
#     for number in args:
#         product = product * number
#     return product * 0.1
#
#
# print(ten_percent_of_product_with_args(10, 20, 2, 1, 4, 345))

# def percent_of_product_with_args(percent, *args):
#     product = 1
#     for number in args:
#         product = product * number
#     return product / 100 * percent
#
#
# print(percent_of_product_with_args(20, 10, 20, 2, 1, 4, 345))

# # **kwargs

# def func_with_kwargs(**kwargs):
#     print(kwargs)
#
#
# func_with_kwargs(first=1, second=2, third=3)
#  {'first' : 1, 'second' : 2, 'third' : 3}

# def hello_with_kwargs(**kwargs):
#     if 'name' in kwargs:
#         print('Hello! Nice to meet you, {}'.format(kwargs['name']))
#     else:
#         print('Hello! What is your name?')
#
#
# hello_with_kwargs(gender='male', age=24, name='Jack')
# hello_with_kwargs(gender='male', age=24)

# def hello_with_greeting_and_kwargs(greeting, **kwargs):
#     if 'name' in kwargs:
#         print('{}! Nice to meet you, {}'.format(greeting, kwargs['name']))
#     else:
#         print('{}! What is your name?'.format(greeting))
#
#
# hello_with_greeting_and_kwargs('Good morning', gender='male', age=24, name='Jack')
# # hello_with_greeting_and_kwargs(gender='male', age=24)

def func_with_args_and_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0], kwargs['food']))

func_with_args_and_kwargs('one', 'two', drink='coffee', food='sandwich')


# ('one', 'two')
# {'drink': 'coffee', 'food': 'sandwich'}
# I would like one sandwich

def is_cat_here(*args):

    args_in_lower_case = [str(arg).lower() for arg in list(args)]
    if 'cat' in args_in_lower_case:
        return True
    else:
        return False


print(is_cat_here('dog', 'CAT', 'cow'))
#  True

def is_item_here(item, *args):
    if item in args:
        return True
    else:
        return False

print(is_item_here('item', 'set', 'text', 'line'))
#  False

def your_favorite_color(my_color, **kwargs):
    if 'color' in kwargs:
        print('My favorite color is ' + str(my_color) + ', but ' + kwargs['color'] + ' is also pretty good!')

    else:
        print('My favorite color is ' + str(my_color) + ', what is your favorite color?')


#  your_favorite_color('white', car = 'Opel',  age = 37, colors = 'black')
#  My favorite color is white, what is your favorite color?

your_favorite_color('white', car = 'Opel', color = 'yellow',  age = 37, colors = 'black')
#  My favorite color is white, but yellow is also pretty good!
