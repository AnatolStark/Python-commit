# print(1 < 2)
#  True
# print(type(True))  #  <class 'bool'>
# print(type(False))  #   #  <class 'bool'>
#
# # Comparison operators  sravnenie strok
#
# print(1 == 1)  #  True
# print(1 == 2)  #  False
# print('Hello' == 'Hello')  # #  True
# print('Hello' == 'hello')  #  False

# print(1 != 1)  #  False
# print(1 != 2)  #  True
# print('Hello' != 'Hello')  #  False
# print('Hello' != 'hello')  #  True

# print(1 > 2)   #  False
# print(1 < 2)  #  True
# print(2 >= 2)  #  True
# print(3 >= 2)  #  True
# print(2 <= 2)  #  True
# print(3 <= 2)   #  False
#
# print(ord('a'))  #  97 kod po ASCII
# print(ord('b'))  #  98
# print('a' > 'b')   #  False
# print('hi' > 'hello')  #  True
# print(ord('i'))  #  105
# print(ord('e'))  #  101

# x = 10
# y = 23
#
# print(x > y)   #  False
# print(x < y)  #  True
# print(x == y)   #  False
# print(x != y)  #  True

age = input('Input your age')   #  vvedite svoi vosrast
print('Your age is' + age)
#  Input your age 64
#  Your age is 64

age = int(input('Input your age'))
print('Access is permitted: ' + str(age >= 18))
#  Input your age 64
# Your age is 64
# Input your age64
# Access is permitted: True

x = 12
y = 77
print(x > y)
print(x < y)
print(x >= y)
print(x != y)
print(x == y)
#  False
#  True
#  False
#  True
#  False

print("x" > "X")
#   True
print(ord("A"))
print(ord("S"))
print(ord("C"))
print(ord("I"))
#  65
#  83
#  67
#  73

