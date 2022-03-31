# Immutable  neismenjaemye
first_name = 'Jake'
print(first_name[2])  # k
# first_name[2] = 'n'
# print(first_name)    #  nekorektnyi kod

first_two_letters = first_name[:2]
print(first_two_letters)            # Ja
last_letter = first_name[-1:]
print(last_letter)                  # e

# Concatenable  szeplenie snakov i strok
new_first_name = first_two_letters + 'n' + last_letter
print(new_first_name)                # Jane

greeting = 'Hello'
greeting = greeting + ' Python!'
print(greeting)                   # Hello Python

# Multiplication  umnoshenie strok
yummy = 'Yum '
print(yummy * 3)                   # Yum Yum Yum

print(yummy.upper())            # YUM  (metod .upper()) saglavnye bukvy
print(yummy.lower())            # yum  (metod .lower()) malenkie bukvy
print(yummy)

long_string = 'This is the long string'
print(long_string.split('s'))     # ['Thi', 'i', 'the long', 'tring']   metod .split('s') rasdeljaet stroki

long_2_string = 'This is the long string'
print(long_2_string.split())      # ['This', 'is', 'the', 'long', 'string']

greeting = 'Hello Python!'
first_two_letters = greeting[5:7]
print(first_two_letters)            # P
last_letter = greeting[8:10]
print(last_letter)                  # th
letter = "a"
new_world = first_two_letters + letter + last_letter
print(new_world)                    # Path

next_letter = "z"
print(next_letter * 7)              # zzzzzzz
                                     # kette_letter = next_letter * 7 (drugoi variant)
print((next_letter * 7).upper())         # ZZZZZZZ