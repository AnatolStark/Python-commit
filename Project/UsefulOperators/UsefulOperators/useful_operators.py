# for x in range(3, 11, 3):  # poslednjaja zifra - shag vypolnenija pechati
#     print(x)
#  3
#  6
#  9

# print(range(5))
#  range(0, 5)

# print(list(range(5)))
#  [0, 1, 2, 3, 4]

letter_index = 0  # - vspomogatelnaja
my_string = 'adfagasg'
for letter in my_string:
    print(letter + ' is at index ' + str(letter_index))
    letter_index = letter_index + 1
    #  a is at index 0
    # d is at index 1
    # f is at index 2
    # a is at index 3
    # g is at index 4
    # a is at index 5
    # s is at index 6
    # g is at index 7

# my_string = 'adfagasg'   # 2-oi sposob
# for index, letter in enumerate(my_string):
#     print(letter + ' is at index ' + str(index))
# a is at index 0
# d is at index 1
# f is at index 2
# a is at index 3
# g is at index 4
# a is at index 5
# s is at index 6
# g is at index 7

# print('a' in 'Jack')
# True
# print('x' in 'Jack')
# False
# print(str(1) in 'Jack')
# False
# print('1' in 'Jack')
# False

# letter_list = ['a', 'b', 'c', True]
# print('a' in letter_list)
# True
# print(True in letter_list)
# True

# dict_1 = {1: 'a', 2: 'b', 3: 'c'} v slovare
# print(1 in dict_1)
# True
# print(1 in dict_1.keys())
# True
# print(4 in dict_1.keys())
# False
# print('c' in dict_1.values())
# True
# print('z' in dict_1.values())
# False

# print(min(1, 3, 56, 4))
# 1
# print(max(1, 3, 56, 4))
# 56
#
# my_list = [1, 3, 56, 4]
# print(min(my_list))
# 1
# print(max('Hello'))
# o
# for letter in 'Hello':
#     print(ord(letter)) # ord - kod chisla
# 72
# 101
# 108
# 108
# 111

from random import shuffle  # import is biblioteki f. shuffle - peremeshat
my_list = [1, 3, 56, 4]
shuffle(my_list)
print(my_list)
# [56, 4, 3, 1]

from random import randint # sluchainyi vybor
print(randint(12,20))
# 17
