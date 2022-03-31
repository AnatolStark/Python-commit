# tuple_1 = 1, 2, 3
#  print(tupl_1)
#  (1, 2, 3)

#  print(typeTuple_1))
#  <class 'tuple'>

# tuple_2 = ('one', 'hello')
#  print(tuple_2)
#  ('one', 'hello')

# tuple_3 = (3, 2.3, 'three')
#  print(tuple_3)
#  (3, 2.3, 'three')

#  print(tuple_1[1])
#  2

# # tuple_1[1] = 3  ne vernyi kod, tuple, t.e. kortesh ne ismenjaetcja

# poetomu sosdaem novyi tupie

# new_tuple = (tuple_1[0], 3, tuple_1[2])
# print(new_tuple)
#  (1, 3, 3)



x = y = z = 12
#  print(x, y, z)
#  12 12 12

x, y, z = 12, 13, 14

print(x, y, z)

person_tuple = ('John', 'Smith', 1986)
first_name, last_name, year_of_birth = person_tuple

print(first_name, last_name, year_of_birth)
#  John Smith 1986

t1 = (1, 2, 5, 1, 7, 9)
print(t1.count(1))
#  2 rasa vstrechaetsja 1

greetings_tuple = ('hello', 'hi', 'hey', 'hi')
print(greetings_tuple.count('hola'))
#  0 net takogo elementa

print(t1.index(1))
#  0 ediniza nachoditsja na 1 meste

print(greetings_tuple.index('hi'))
#  1 'hi' na 2-m meste

computer_tuple = ('Medion Akoya', 'prozessor Core', '8 GB RAM', '512 GB SSD', 'silver')
brand, prozessor, RAM, SSD, color = computer_tuple
print(brand, prozessor, RAM, SSD, color)
#  Medion Akoya prozessor Core 8 GB RAM 512 GB SSD silver
