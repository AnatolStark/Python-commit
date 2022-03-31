greeting = "Hello Python!"
greeting_length = len(greeting)
print(greeting_length)  #oder print(len(greeting))  # 13 snakov

   # Indexing  otschet nachinaetsja c 0, moshno schitat c nachala ili c konza
print(greeting[0])  # H
print(greeting[6])  # P
print(greeting[-1]) # !
print(greeting[12]) # !
print(greeting[-4]) # h

   # Slicing  vyresanie is stroki

print(greeting[2:5])   # llo
print(greeting[6:10])  # Pyth
print(greeting[-5:-2])  # tho
print(greeting[2:])     # llo Python!
print(greeting[:5])     # Hello
print(greeting[:])  # Pechataetsja vce  # Hello Python
print(greeting[::2])  # kashdyi 2 snak  # HloPto!
print(greeting[1::3])  # eoyo
print(greeting[1:9:3])  # s 1 po 9 cheres 3 snaka  # eoy
print(greeting[::-1])   # pechataetsja stroka naoborot  #  !nohtyP olleH
print(greeting[3])
print("Hello Python!"[3])  # 2-oi sposob vyvesti na pechan 3-i snak

greeting = 'Hello Python!'
path = greeting[6] + 'a' + greeting[8:10]
print(greeting[6] + 'a' + greeting[8:10])
