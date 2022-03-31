# Special (magic) methods __method_name__


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def __len__(self):
        return self.age

    def __add__(self, other):
        return self.age + other.age

    def __del__(self):   #  del - udalenie obekta
        print('Person object with name ' + self.first_name + ' is deleted'
                                                             ' from memory')


jack = Person('Jack', 'White', 45)
jane = Person('Jane', 'Eyre', 23)

print(jack + jane)
#  68

print([1, 2, 3, 4, 5])
#  [1, 2, 3, 4, 5]
print(jack)
#  Jack White
print(len(jack))
#  45
# del (jack)
# print(jack)
#  Person object with name Jack is deleted from memory
#  Person object with name Jane is deleted from memory
# x = 5
# y = 3
#
# a = '5'
# b = '3'
#
# print(x.__add__(y))
# print(a.__add__(b))
#

class Chain():   #  chain - zep
    def __init__(self, number_of_items):
        self.number_of_items = number_of_items

    def __str__(self):
        return "Chain with " + str(self.number_of_items) + " items"

    def __len__(self):
        return self.number_of_items


chain_1 = Chain(8)
chain_2 = Chain(24)

print(chain_1)
print(chain_2)
#  Chain with 8 items
#  Chain with 24 items

print(len(chain_1))
print(len(chain_2))