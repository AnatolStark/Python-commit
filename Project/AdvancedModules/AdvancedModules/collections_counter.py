from collections import Counter

number_list = [1, 1, 1, 4, 4, 5, 77, 77, 3, 3, 3, 3, 3]

print(Counter(number_list)) # Counter({3:5, 1:3, 4:2, 5:1})

string = 'dddddkkkkeeeooooooooiiiiiiiiiii'

print(Counter(string))  #  Counter({'i': 11, 'o': 8, 'd': 5, 'k': 4, 'e': 3})

sentence = "Hello how are you doing? Hello I'm fine. How do you do? Hey Hey Hey !"

print(Counter(sentence.split(' ')))  #  Counter({'Hey': 3, 'Hello': 2, 'you': 2, 'how': 1, 'are': 1, 'doing?': 1, "I'm": 1, 'fine.': 1, 'How': 1, 'do': 1, 'do?': 1, '!': 1})

c = Counter(sentence.split(' '))

print(sum(c.values()))  #  16 elementov
# c.clear()  #  0

# print(list(c))  # ['Hello', 'how', 'are', 'you', 'doing?', "I'm", 'fine.', 'How', 'do', 'do?', 'Hey', '!']
# print(set(c))   #  {'do?', 'Hello', 'Hey', 'are', "I'm", 'doing?', '!', 'do', 'fine.', 'how', 'How', 'you'}
# print(dict(c))   #  {'Hello': 2, 'how': 1, 'are': 1, 'you': 2, 'doing?': 1, "I'm": 1, 'fine.': 1, 'How': 1, 'do': 1, 'do?': 1, 'Hey': 3, '!': 1}
c = c.items()

# print(c)  #  dict_items([('Hello', 2), ('how', 1), ('are', 1), ('you', 2), ('doing?', 1), ("I'm", 1), ('fine.', 1), ('How', 1), ('do', 1), ('do?', 1), ('Hey', 3), ('!', 1)])

c = Counter(dict(c)) #  poluchaem obratno Counter

# print(c)  #  Counter({'Hey': 3, 'Hello': 2, 'you': 2, 'how': 1, 'are': 1, 'doing?': 1, "I'm": 1, 'fine.': 1, 'How': 1, 'do': 1, 'do?': 1, '!': 1})

print(c.most_common())  # [('Hey', 3), ('Hello', 2), ('you', 2), ('how', 1), ('are', 1), ('doing?', 1), ("I'm", 1), ('fine.', 1), ('How', 1), ('do', 1), ('do?', 1), ('!', 1)]

# [:-2-1:1)] - redko vstrechaushiesja 2 elementa
#print(c.most_common()[:-2-1:-1])  #  [('!', 1), ('do?', 1)]

# chasto vstrechaushiesja elementy
print(c.most_common(3))  #  [('Hey', 3), ('Hello', 2), ('you', 2)]