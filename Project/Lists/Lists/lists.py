# number_list = [32, 21, 48, 34.56]
# print(number_list)  # [32, 21, 48, 34.56]
# some_list = [12, 35.334, 'hello']
# print(some_list)   #  [12, 35.334, 'hello']
# print(len(some_list))  #  3 elementa
# print(some_list[1])  #  35.334 - 2-oi element
# another_list = some_list[:2]
# print(another_list)  #  [12, 35.334] -vyresanie 2-x elementov
# some_list[2] = 'hi'
# print(some_list)  #  [12, 35.334, 'hi']  - v list moshno menjat dannye!
# new_list = some_list + another_list
# print(new_list)  #  [12, 35.334, 'hi', 12, 35.334]
#
# # Adding items   #  dobavlenie elementov
#
# # new_list[5] = 'new item'  #  oshibka 6 elementa net!
# new_list.append('new item')  #  metod append - dobavlenie elementa  #  [12, 35.334, 'hi', 12, 35.334, 'new item']
# new_list.insert(0, 'start')  #  metod insert - vstavljat element  # ['start',12, 35.334, 'hi', 12, 35.334, 'new item']
# new_list.insert(2, 13)  #  ['start', 12, 13, 35.334, 'hi', 12, 35.334, 'new item']
#
# # Removing items  #  udalenie elementov
# # new_list.pop(-1)  # ['start', 12, 13, 35.334, 'hi', 12, 35.334]
# # new_list.pop(0)  #  [12, 13, 35.334, 'hi', 12, 35.334]
# # new_list.pop(-3)  #  [12, 13, 35.334, 12, 35.334]
#
# deleted_item = new_list.pop()
# print(deleted_item)  #  new item -vosvrashenie ()-poslednego elementa
# deleted_item = new_list.pop(-3)  #  hi
#
# deleted_item = new_list.remove(12)  #  udalenie snachenija  ['start', 13, 35.334, 'hi', 12, 35.334]
# None
#
# print(new_list)
# print(deleted_item)
#
number_list = [45, 12, 3, -455, 22]  #  [-455, 3, 12, 22, 45]
letter_list = ['s', 'w', 't', 'a']  #  ['a', 's', 't', 'w']

x = number_list.sort()  #  None
letter_list.sort()
new_list = letter_list  #  ['a', 's', 't', 'w']


print(x)
print(new_list)
number_list.reverse()  #  metod reverse - obratnyi porjadok  #  [45, 22, 12, 3, -455]
letter_list.reverse()  #  ['w', 't', 's', 'a']

number_list.append(letter_list)  #  [45, 22, 12, 3, -455, ['w', 't', 's', 'a']]

print(number_list)
print(letter_list)

list_1 = ['one', 387, -897, 'Hello', 45.387, 'Hi']
print(list_1)

list_2 = list_1[1:4]
print(list_2)

list_3 = list_1 + list_2
print(list_3)