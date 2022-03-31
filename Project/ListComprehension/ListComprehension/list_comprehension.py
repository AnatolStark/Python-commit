# List Comprehension - ponimanie spiska, t.e. sosdavat spiski is raslichnyh posledovatelnostej bolee elegantno i korotko
greeting = 'hello!'
letter_list = []  # sosdat pustoi spisok
for letter in greeting:
    letter_list.append(letter)  # dobavlenie bukv v spisok
print(letter_list)
# ['h', 'e', 'l', 'l', 'o', '!']

# bolee udobnyi sposob

# letter_list = [letter for letter in greeting]
# print(letter_list)
# ['h', 'e', 'l', 'l', 'o', '!']

number_list = [number for number in '0123456789']
print(number_list)
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

number_list_1 = [num for num in range(0, 10)]
print(number_list_1)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

number_list_2 = [num ** 2 for num in range(0, 10)]
print(number_list_2)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

number_list_3 = [- ((num - 3) / 2) ** 2 for num in range(0, 10)]
print(number_list_3)
# [-2.25, -1.0, -0.25, -0.0, -0.25, -1.0, -2.25, -4.0, -6.25, -9.0]

number_list_4 = [6, 43, -2, 11, -55, -12, 3, 345,0]
new_list = [number ** 3 / 2 for number in number_list_4 if number > 0]
print(new_list)
# [108.0, 39753.5, 665.5, 13.5, 20531812.5]

new_list_1 = ['+' if number > 0 else '-' for number in number_list_4]
print(new_list_1)
# ['+', '+', '-', '+', '-', '-', '+', '+']

new_list_1 = ['+' if number > 0 else '-' if number < 0  else 'zero' for number in number_list_4]
print(new_list_1)
#  ['+', '+', '-', '+', '-', '-', '+', '+', 'zero']

# # Dictionary Comprehension  # slovar
# number_dict = {'first': 1, 'second': 2, 'third': 3}
# new_dict = {key: value ** 3 for key, value in number_dict.items()}
# print(new_dict)
# {'first': 1, 'second': 8, 'third': 27}

# number_list = [6, 43, 0, -2, 11, -55, -12, 3, 345]   # is lista  delaem spisok
# number_dict = {number: number ** 2 for number in number_list}
# print(number_dict)
# {6: 36, 43: 1849, -2: 4, 11: 121, -55: 3025, -12: 144, 3: 9, 345: 119025}

# number_dict = {number: 'positive' if number > 0
# else 'negative' if number < 0 else 'zero' for number in number_list}
# print(number_dict)
# {6: 'positive', 43: 'positive', 0: 'zero -2: 'negative', 11: 'positive', -55: 'negative', -12: 'negative', 3: 'positive', 345: 'positive'}

# Set Comprehension   #  mnoshestva
number_list = [6, 43, 0, -2, 11, -55, -12, 3, 345]
number_set = {number ** 2 for number in number_list}
print(number_set)
#  {0, 121, 36, 4, 9, 144, 3025, 119025, 1849} ne uporjadochnaja posledovatelnost

number_set = {number ** 2 for number in range(3, 11)}
print(number_set)
#  {64, 36, 100, 9, 16, 49, 81, 25}

letter_set = {letter.upper() for letter in 'hello'}  #  .upper - saglavnye bukvy
print(letter_set)
#  {'E', 'O', 'H', 'L'}

greetings = ['hello', 'hi', 'hey', 'hola']
letter_list =[]
for greeting in greetings:
    letter_list.append(greeting[1])
    print(letter_list)
    # ['e']
    # ['e', 'i']
    # ['e', 'i', 'e']
    # ['e', 'i', 'e', 'o']
letter_list = [greeting[1] for greeting in greetings]
print(letter_list)
# ['e', 'i', 'e', 'o']

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
number_list = []
for number in digits:
    if number % 2 == 1:
       number_list.append(number)
       print(number_list)
       #  [1]
       # [1, 3]
       # [1, 3, 5]
       # [1, 3, 5, 7]
       # [1, 3, 5, 7, 9]

number_list = [number for number in digits if number % 2 == 1]
print(number_list)
# [1, 3, 5, 7, 9]

# Vloshennye cikly

for number in range(11):
    count = 0
    emoticons = ''
    while count <= number:
        emoticons += '\U0001f600'
        count += 1
        print(emoticons)
        #  😀
        # 😀
        # 😀😀
        # 😀
        # 😀😀
        # 😀😀😀
        # 😀
        # 😀😀
        # 😀😀😀
        # 😀😀😀😀
        # 😀
        # 😀😀
        # 😀😀😀
        # 😀😀😀😀
        # 😀😀😀😀😀
        # 😀
        # 😀😀
        # 😀😀😀
        # 😀😀😀😀
        # 😀😀😀😀😀
        # 😀😀😀😀😀😀
        # 😀
        # 😀😀
        # 😀😀😀
        # 😀😀😀😀
        # 😀😀😀😀😀
        # 😀😀😀😀😀😀
        # 😀😀😀😀😀😀😀
        # 😀
        # 😀😀
        # 😀😀😀
        # 😀😀😀😀
        # 😀😀😀😀😀
        # 😀😀😀😀😀😀
        # 😀😀😀😀😀😀😀
        # 😀😀😀😀😀😀😀😀
        # 😀
        # 😀😀
        # 😀😀😀
        # 😀😀😀😀
        # 😀😀😀😀😀
        # 😀😀😀😀😀😀
        # 😀😀😀😀😀😀😀
        # 😀😀😀😀😀😀😀😀
        # 😀😀😀😀😀😀😀😀😀
        # 😀
        # 😀😀
        # 😀😀😀
        # 😀😀😀😀
        # 😀😀😀😀😀
        # 😀😀😀😀😀😀
        # 😀😀😀😀😀😀😀
        # 😀😀😀😀😀😀😀😀
        # 😀😀😀😀😀😀😀😀😀
        # 😀😀😀😀😀😀😀😀😀😀
        # 😀
        # 😀😀
        # 😀😀😀
        # 😀😀😀😀
        # 😀😀😀😀😀
        # 😀😀😀😀😀😀
        # 😀😀😀😀😀😀😀
        # 😀😀😀😀😀😀😀😀
        # 😀😀😀😀😀😀😀😀😀
        # 😀😀😀😀😀😀😀😀😀😀
        # 😀😀😀😀😀😀😀😀😀😀😀

# vtoroi sposob
for number in range(11):
    emoticons = ''
    for count in range(number + 1) :
        emoticons += '\U0001f600'
        print(emoticons)

# 3-i sposob

for number in range(1, 11):
    print('\U0001f600' * number)
    #  😀
    # 😀😀
    # 😀😀😀
    # 😀😀😀😀
    # 😀😀😀😀😀
    # 😀😀😀😀😀😀
    # 😀😀😀😀😀😀😀
    # 😀😀😀😀😀😀😀😀
    # 😀😀😀😀😀😀😀😀😀
    # 😀😀😀😀😀😀😀😀😀😀

count = 1
while count < 11:
    print('\U0001f600' * count)
    count += 1
    #  😀
    # 😀😀
    # 😀😀😀
    # 😀😀😀😀
    # 😀😀😀😀😀
    # 😀😀😀😀😀😀
    # 😀😀😀😀😀😀😀
    # 😀😀😀😀😀😀😀😀
    # 😀😀😀😀😀😀😀😀😀
    # 😀😀😀😀😀😀😀😀😀😀

    #  vloshennye spiski

nested_list = [[1, 2, 3], [4, 5, 6],[7, 8, 9]]
print(nested_list)
#  [[1, 2, 3], [4, 5, 6],[7, 8, 9]]
print(len(nested_list))
#  3 - kollichestvo spiskov v spiske
print(len(nested_list[1]))
#  3 dlina 2-go spiska
print(nested_list[1][1])
#  5  2-oi snak vo 2-om spiske

# Print nested_list

for inner_list in nested_list:
    print(inner_list)
    #  [1, 2, 3]
    # [4, 5, 6]
    # [7, 8, 9]


for inner_list in nested_list:
    for number in inner_list:
        print(number)
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9

#    List comprehension

[[print(number) for number in inner_list] for inner_list in nested_list]
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9





