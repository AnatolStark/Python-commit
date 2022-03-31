from collections import defaultdict

my_dict = defaultdict(lambda: 1)
my_dict[1] = 'a'
my_dict = {1: 'a'}
#  print(my_dict[1])  #  a
print(my_dict[2])  #  1
s = 'Hello'
d = defaultdict(int)
for k in s:
    d[k] += 1
print(sorted(d.items()))  #  [('H', 1), ('e', 1), ('l', 2), ('o', 1)]

