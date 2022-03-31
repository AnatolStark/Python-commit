rainbow_colors = {'red', 'orange', 'yellow', 'green', 'blue',
                  'indigo', 'violet'}  #  v set, t.e. mnoshestvo ne moshet byt odinakovych snachenij

print(rainbow_colors)
#  {'violet', 'orange', 'indigo', 'red', 'green', 'yellow', 'blue'}

print(type(rainbow_colors))
#  <class 'set'>

empty_set = set()  # pustoe mnoshestvo
print(empty_set)
#  set()

print(type(empty_set))
#  <class 'set'>

number_list = [1, 43, 56, 3, 3, 3, 3]
text_tuple = ('sfds', 'aafg', 'afadsf', 'hi', 'hi', 'hi')
set_from_list = set(number_list)
set_from_tuple = set(text_tuple)
#  print(set_from_list)
#  {56, 1, 43, 3}  ne uporjadochnoe mnoshestvo

#  print(set_from_tuple)
#  {'sfds', 'hi', 'aafg', 'afadsf'}  ne uporjadochnoe mnoshestvo

set_from_list.add(777)
#  print(set_from_list)
#  {1, 3, 777, 43, 56}

set_from_tuple.add('hello')
#  print(set_from_tuple)
#  {'afadsf', 'sfds', 'hello', 'aafg', 'hi'}
set_from_list.add(777)  # dublikat ne dobavljaetsja
set_from_tuple.add('hello') #  dublikat ne dobavljaetsja

set_from_list.pop()  # udalenie snachenija slachainym obrasom
print(set_from_list)
#  {3, 777, 43, 56}  udalena 1
set_from_list.remove(3)
print(set_from_list)
#  {777, 43, 56}  udalena 3


set_from_list.discard(43)
print(set_from_list)
#  {777, 56}  udalen 43
# set_from_list.remove(3) oshibka net 3 v set
# set_from_list.discard(3)  oshibka net 3 v set
set_from_list.clear()
print(set_from_list.clear())
#  None

sentence_set = set('A set is a collection' 'which is' 'unordered and unindexed.')

print(sentence_set)
#  {'r', 'a', ' ', 'n', 'e', 'l', 't', 'u', '.', 's', 'i', 'x', 'o', 'A', 'h', 'w', 'c', 'd'}
print(type(sentence_set))
#  <class 'set'>
