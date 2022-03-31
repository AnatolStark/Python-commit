x = 1
y = 2

# print(x > 1)  #  False
# print(y > 1)  #  True

# and, or, not
# print(x > 1 and y > 1)  #  False
# print(x > 1 or y > 1)   #  True
# print(not x > 1)  #  True
# print(not y > 1)  #  False

print(True and True)  #  True
print(True or True)   #  True
print(not True)       #  False

print(False and False)  #  False
print(False or False)  #  False
print(not False)  #  True

print(True and False)  #  False
print(True or False)  #  True

name = 'John'
age = 13
is_married = False  #  shenat li Jhon

if age > 18 and is_married == False:
    print('Hi {}! You can find a girl of your dream here!'.format(name))
    # privetstvie ne vyvoditsja t.k. age =13 i stoit uslovie 'and'

if age > 18 or is_married == False:
     print('Hi {}! You can find a girl of your dream here!'.format(name))
     # t.k. uslovie 'or', to vyvoditsja "Hi John! You can find a girl of your dream here!"

