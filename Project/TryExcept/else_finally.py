# If we have an error - except block fires and else block doesn't fire
# If we haven't an error - else block fires and except block doesn't fire
# Finally block fires anyway


# while True:  #  beskonechnyi zikl
#     try:
#         number = int(input('Enter some number'))
#         print(number / 2)
#     except:
#         print('You have to enter a number!')
#     else:
#         print('Good job! This is a number!')
#         break
#     finally:
#         print('Finally block')
#
# print('Code after error handling')


def divide(x, y):  #  delenie
    try:
        return x / y
    except ZeroDivisionError as e:
        print('You can\'t divide by zero!')
        print(e)
    except TypeError as e:
        print('x and y must be numbers')
        print(e)
    else:
        print('x was divided by y')
    finally:
        print('finally block')



# print(divide(4, 0))
#  You can't divide by zero!
# division by zero
# finally block
# None

# print(divide(4, 'w'))
#  x and y must be numbers
# unsupported operand type(s) for /: 'int' and 'str'
# finally block
# None

print(divide(44,33))
#  finally block
# 1.3333333333333333
