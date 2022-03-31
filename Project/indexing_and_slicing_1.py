greeting = "Hello Python!"

print(len(greeting))  #  13
print(greeting[1])    #  e
print(greeting[6])    #  P
print(greeting[-1])   #  !
print(greeting[12])   #  !
print(greeting[-4])   #  h
print(greeting[2:5])    #   llo
print(greeting[6:10])   #   Pyth
print(greeting[-5:-2])  #   tho
print(greeting[2:])     #    llo Python!
print(greeting[:5])     #    Hello
print(greeting[:])      #    Hello Python!
print(greeting[::2])    #    HloPto!
print(greeting[::1])    #    Hello Python!
print(greeting[::3])    #    HlPh!
print(greeting[1::3])   #    eoyo
print(greeting[1:9:3])  #    eoy
print(greeting[::-1])   #    !nohtyP olleH
print(greeting[3])      #    l
print(greeting[:2])     #    He
print(greeting[:-11])   #    He

greeting = "Hallo Python!"
path = greeting[6] + "a" + greeting[8:10]
print(greeting[6] + "a" + greeting[8:10])   #  Path

greeting = "Hello Python!"
greeting_length = len(greeting)
print(greeting_length)
print(greeting[1])
print(greeting[6])
print(greeting[-1])
print(greeting[12])
print(greeting[-4])
#slicing
print(greeting[2:5])
print(greeting[6:10])
print(greeting[-5:-2])
print(greeting[2:])
print(greeting[:5])
print(greeting[:])
print(greeting[::2])
print(greeting[::1])
print(greeting[::3])
print(greeting[1::3])
print(greeting[1:9:3])
print(greeting[::-1])
print(greeting[3])
print(greeting[-10])
print(greeting[:2])
print(greeting[:-11])
path = greeting[6] + "a" + greeting[8:10]
print(greeting[6] + "a" + greeting[8:10])

#Immutable
first_name = "Jake"
print(first_name[2])    #    k
first_two_letters = first_name[:2]
print(first_two_letters)     #  Ja
last_letter = first_name[-1:]
print(last_letter)           #  e

#Concatenable
new_first_name = first_two_letters + "n" + last_letter
print(new_first_name)      #   Jane

greeting = "Hello"
greeting = greeting + " " + "Python"
print(greeting)                        #  Hello Python!

#Multiplication

yummy = 'Yum'
print(yummy * 2)      #   YumYum
print(yummy * 5)      #   YumYumYumYumYum

#Metods
print(yummy.upper())   #   YUM
print(yummy.lower())   #   yum

long_string = 'This is the long string'
print(long_string.split())    #  ['This', 'is', 'the', 'long', 'string']
print(long_string.split("s"))     #     ['Thi', ' i', ' the long ', 'tring']
print(long_string.split("t"))     #     ['This is ', 'he long s', 'ring']

greeting = "Hello Python!"
print(greeting[6])    #   P
greeting_two_letters = greeting[8:10]
print(greeting_two_letters)   #    th
new_world = greeting[6] + "a" + greeting_two_letters
print(new_world)              #     Path

letter = "z"
print(letter * 7)               #   zzzzzzz
print((letter * 7).upper())     #   ZZZZZZZ

