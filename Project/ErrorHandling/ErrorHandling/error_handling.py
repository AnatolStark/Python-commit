# SyntaxError
# de(f)s function_1():  # vmesto 'f'- 's'
#     x = 1 + 1
#     print(x)


# NameError
# prin(t)s(x)  # vmesto 't' -'s' ili 'x' - neopredeleno

# TypeError
# len(1)
# my_list = [1, 2, 3]
# print(my_list + 'hello')  # list so strokoi nedopuskaetsja

# IndexError
# my_list = [1, 2, 3]
# print(my_list[3])  # index lista vne diaposone
# print('hello'[5])

# ValueError
# print(int('43'))
# print(int('he'))  #  ne rasposnaet
# print(int([43]))  #  int ne prinemaet spisok

# KeyError
# my_dict = {'first': 'apple', 'second': 'orange'}
# # my_dict['third']  #  net klucha v slovare
# my_dict['first']

# AttributeError  #
'red'.attr()
# AttributeError: 'str' object has no attribute 'attr'
