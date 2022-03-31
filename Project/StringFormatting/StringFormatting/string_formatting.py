# print(1 + 1)                                                                   # 2
# print('1' + '1')                                                               # 11
# age = 23
# print('Jack is ' + str(age) + ' years old.')                                   # str (obosnachenie stroki)
# print('Jack is ' + str(23) + ' years old.')                                    # Jack is 23 years old

     # formatirovanie

# name = 'Jack'
# age = 23
# name_and_age = 'My name is {0}. I\'m {1} years old.'.format(name, age)    # { } sapolnitel
# print(name_and_age)
# name_and_age = 'My name is {0}. I\'m {1} years old.'.format('Jack', 23)   # My name is Jack. I'm 23 years old.
# print(name_and_age)
# name_and_age = 'My name is {}. I\'m {} years old.'.format(23, 'Jack')     # My name is 23. I'm Jack years old.
# print(name_and_age)
# week_days = 'There are 7 days in a week: {5}, {0}, {3}, {1}, {2}, {4}, {6}.'\
#     .format('Monday', 'Wednesday', 'Thursday','Tuesday', 'Friday', 'Sunday',   # esli ne po poradku, nado v {} ukasyvat chisla
#             'Saturday')
# print(week_days)
# week_days = 'There are 7 days in a week: {su}, {mo}, {tu}, {we}, {th},' \
#             ' {fr}, {sa}.' \
#     .format(mo = 'Monday', we = 'Wednesday', th = 'Thursday',
#             tu = 'Tuesday', fr = 'Friday', su = 'Sunday',
#             sa = 'Saturday')
# print(week_days)
# week_days = 'There are 7 days in a week: {su}, {su}, {su}, {su}, {su},' \
#             ' {su}, {su}.' \
#     .format(mo = 'Monday', we = 'Wednesday', th = 'Thursday',
#             tu = 'Tuesday', fr = 'Friday', su = 'Sunday',
#             sa = 'Saturday')
# print(week_days)

# float_result = 1000 / 7      # peremennaja
# print(float_result)          # 142.85714285714286
# print('The result of division is {0:10.3f}'.format(float_result))      # {0:10.3f} vtoroi snak (10) ukasyvaet kolichestvo snakov vsego
# The result of division is 142.857 {0:1.3f}, esli 2-i snak > 6, to pered chislami budut probely. The result of division is    142.857
# print('''                                                              # tretij snak (3) kolichestvo snakov posle ,
#  {0:10.2f} {1:10.2f} {2:10.2f}
#  {3:10.2f} {4:10.2f} {5:10.2f}
#  {6:10.2f} {7:10.2f} {8:10.2f}
# '''.format(1.45778, 345.232352, 34.2344, 1234.23,
#            1.45778, 345.232352, 34.2344, 1234.23,
#            456.43234))

name = 'Jack'
age = 23
name_and_age = 'My name is {0}. I\'m {1} years old.'.format(name, age)
print(name_and_age)   # My name is Jack. I'm 23 years old.
name_and_age = f'My name is {name}. I\'m {age} years old.' # 2-i sposob formatirovanija: v peredi stavim f
print(name_and_age)   # My name is Jack. I'm 23 years old.

print('My name is %s. %s %d years old' % (name, "I'm", age))   # metod Python2 ne rekomenduetsja
# My name is Jack. I'm 23 years old.

float_result = 1687965 / 9
print(float_result)

print('''                                                             
 {0:10.4f} {1:10.4f} {2:10.4f} {6:10.4f}      
 {3:10.4f} {4:10.4f} {5:10.4f} {7:10.4f} 
'''.format(1.45778, 345.232352, 34.2344, 1234.23,
           1.45778, 345.232352, 34.2344, 1234.23))
#      1.4578   345.2324    34.2344    34.2344
#   1234.2300     1.4578   345.2324  1234.2300

print('The result of division is {0:15.4f}'.format(float_result))
# The result of division is     187551.6667