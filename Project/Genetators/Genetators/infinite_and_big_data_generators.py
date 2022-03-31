# Infinite process

#
# def create_patterns(): # sosdat uzory
#     max_patterns_number = 100
#     patterns = ('First pattern', 'Second pattern', 'Third pattern',
#                 'Forth pattern')
#     i = 0
#     result_list = []
#     while len(result_list) < max_patterns_number:
#         if i >= len(patterns):
#             i = 0
#         result_list.append(patterns[i])
#         i += 1
#     return result_list
#
#
# print(create_patterns())


def get_current_pattern():  #  poluchit tekushij uzor
    patterns = ('First pattern', 'Second pattern', 'Third pattern',
                'Forth pattern')
    i = 0
    while True:
        if i >= len(patterns):
            i = 0
        yield patterns[i]
        i += 1


current_pattern = get_current_pattern()
print(current_pattern.__next__())
print(current_pattern.__next__())
print(current_pattern.__next__())
print(current_pattern.__next__())
print(current_pattern.__next__())
print(current_pattern.__next__())
# First pattern
# Second pattern
# Third pattern
# Forth pattern
# First pattern
# Second pattern

def get_infinite_square_generator():
    number = 1
    while True:
        yield number * number
        number += 1

infinite_square_generator = get_infinite_square_generator()

print(infinite_square_generator.__next__())
print(infinite_square_generator.__next__())
print(infinite_square_generator.__next__())
print(infinite_square_generator.__next__())
print(infinite_square_generator.__next__())
#  1
# 4
# 9
# 16
# 25




