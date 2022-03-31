# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in number_list:
# print(number)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in number_list:
    # print(str(number) + ' Hola!')
    # 1 Hola!
    # 2 Hola!
    # 3 Hola!
    # 4 Hola!
    # 5 Hola!
    # 6 Hola!
    # 7 Hola!
    # 8 Hola!
    # 9 Hola!
    # 10 Hola!

# for number in number_list:
    # if number % 2 == 0:
      #  print(number)
    # else:
       # print('Hey!')
        # Hey!
        # 2
        # Hey!
        # 4
        # Hey!
        # 6
        # Hey!
        # 8
        # Hey!
        # 10
# list_numbers_sum = 0
# for number in number_list:
    # list_numbers_sum = list_numbers_sum + number
   # print(list_numbers_sum)
    # 1
    # 3
    # 6
    # 10
    # 15
    # 21
    # 28
    # 36
    # 45
    # 55
# print(list_numbers_sum)
 #  55  esli print v nachaale stroki, to obshaja summa

# greeting = 'Hello Python!'
# for letter in greeting:
   # print(letter)
    # H
    # e
    # l
    # l
    # o
    #
    # P
    # y
    # t
    # h
    # o
    # n
    # !

# greeting = 'Hello Python!'
# for letter in greeting:
#     if letter == 'o':
#         print(letter)
# o
# 0

# for letter in 'Hello Python!':
    # if letter != 'o':
       # print(letter)
        # H
       # e
       # l
       # l
       #
       # P
       # y
       # t
       # h
       # n
       # !


# for letter in 'Hello Python!':
     # print('One more letter!')
     # One more letter!   # skolko snakov , stolko ras pechataetsja
     # One more letter!
     # One more letter!
     # One more letter!
     # One more letter!
     # One more letter!
     # One more letter!
     # One more letter!
     # One more letter!
     # One more letter!
     # One more letter!
     # One more letter!
     # One more letter!

# tuple_list = [('a', 'b'), ('c', 'd'), ('e', 'f')]
# for item in tuple_list:
    # print(item)
    # ('a', 'b')
    # ('c', 'd')
    # ('e', 'f')

# for letter_1, letter_2 in tuple_list:
    # print(letter_1, letter_2)
    # a b
    # c d
    # e f

# for letter_1, letter_2 in tuple_list:
    # print(letter_1)
    # print(letter_2)
    # a
    # b
    # c
    # d
    # e
    # f

# tuple_list_1 = [('a', 'b', 1), ('c', 'd', 4), ('e', 'f', 5)]
# for letter_1, letter_2, number in tuple_list_1:
    # print(letter_1, letter_2, number)
    # a b 1
    # c d 4
    # e f 5

# dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# key-value pairs in tuples # para snachenij
# for item in dictionary.items(): # .items vysyvaet kluch i snachenie
    # print(item)
    # ('key1', 'value1')
    # ('key2', 'value2')
    # ('key3', 'value3')
#
# # keys
# for item in dictionary:
    # print(item)
# for item in dictionary.keys():
    # print(item)
    # key1
    # key2
    # key3
    # key1
    # key2
    # key3

# for key, value in dictionary.items():
    # print(key)
    # key1
    # key2
    # key3
#
# # values
# for item in dictionary.values():
    # print(item)
    # value1
    # value2
    # value3
# for key, value in dictionary.items():
    # print(value)
    # value1
    # value2
    # value3

# for x in range(5):
    # print(x)
    # 0
    # 1
    # 2
    # 3
    # 4

# for _ in range(5):
    # print('Hello!')
    # Hello!
    # Hello!
    # Hello!
    # Hello!
    # Hello!

# number_list = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# list_numbers_sum = 0
# for number in number_list:
    # if number % 2 == 0:
       # list_numbers_sum = list_numbers_sum + number
       # print(list_numbers_sum)
       # 10
       # 22
       # 36
       # 52
       # 70
       # 90
       # 112
       # 136
       # 162
       # 190
       # 220

# even_numbers_sum = 0

# for number in range(10, 31):
    # if number % 2 == 0:
       # even_numbers_sum += number

# print(even_numbers_sum)
# 220

# for letter in 'Get a number from the user as input':
    # print('Hi!')

# number = input('Please, enter any integer number')

# for _ in range(int(number)):
    # print('Hello!')
    # Please, enter any integer number7
    # Hello!
    # Hello!
    # Hello!
    # Hello!
    # Hello!
    # Hello!
    # Hello!

number = input('Please, enter any integer number')

for number in range(int(number)):
    print('Hello!')
    # Please, enter any integer number5
    # Hello!
    # Hello!
    # Hello!
    # Hello!
    # Hello!