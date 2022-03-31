# Testing is writing the test code that checks bugs in our code
# Assertions  #  utvershdenie

# assert 2 + 2 == 4
# assert 2 + 2 == 5, '2 + 2 must equals 4'
#  AssertionError: 2 + 2 must equals 4


# def divide(a, b):  # delenie
#     assert b != 0, 'b must not equals 0'
#     return a / b
#
#
# print(divide(2, 2))
#  1
# print(divide(2, 0))
#  AssertionError: b must not equals 0

 def multiply_positive_numbers(a, b):
     assert a > 0 and b > 0, 'a and b must be positive'
     print(a * b)



 multiply_positive_numbers(3, 5)
 # 15
 multiply_positive_numbers(3, -5)
#  AssertionError: a and b must be positive


def get_access(password):
    password_list = [111, 222, 333]
    assert int(password) in password_list, 'Password is invalid'
    print('You can make dangerous stuff')


password_1 = input('Please input the password')
get_access(password_1)




