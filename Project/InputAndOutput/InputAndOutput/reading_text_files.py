# # Input
# x = input('Input something')
#
# # Output
# print('Output something' + x)

# print(1, 2, 3, sep=':', end='\n')
# 1:2:3
# print(1, 2, 3, sep=',', end=' ')
# print(1, 2, 3, sep=';', end='')
# 1,2,3 1;2;3

# lorem_ipsum_text = open('/Users/Anatol/PycharmProjects/pythonProject/sample.txt', 'r')
# for line in lorem_ipsum_text:
   #  print(line, end='')
# lorem_ipsum_text.close()
#  When I find myself in times of trouble, Mother Mary comes to me
# Speaking words of wisdom, let it be
# And in my hour of darkness she is standing right in front of me...
...
# Process finished with exit code 0

# lorem_ipsum_text = open('/Users/Anatol/PycharmProjects/pythonProject/sample.txt', 'r')
# for line in lorem_ipsum_text:
    # if 'mary' in line.lower():
        # print(line, end='')
# lorem_ipsum_text.close()
# When I find myself in times of trouble, Mother Mary comes to me
# I wake up to the sound of music, Mother Mary comes to me

# with open('/Users/Anatol/PycharmProjects/pythonProject/sample.txt', 'r') as lorem_ipsum_text:
    # for line in lorem_ipsum_text:
        # if 'mary' in line.lower():
            # print(line, end='')
# When I find myself in times of trouble, Mother Mary comes to me
# I wake up to the sound of music, Mother Mary comes to me

# with open('/Users/Anatol/PycharmProjects/pythonProject/sample.txt', 'r') as lorem_ipsum_text:
    # line = lorem_ipsum_text.readline()
    # while line:
        # print(line, end='')
        # line = lorem_ipsum_text.readline()
#  When I find myself in times of trouble, Mother Mary comes to me
# Speaking words of wisdom, let it be
# And in my hour of darkness she is standing right in front of me...
...
# Process finished with exit code 0

with open('/Users/Anatol/PycharmProjects/pythonProject/sample.txt', 'r') as lorem_ipsum_text:
    lines = lorem_ipsum_text.readlines()
print(lines)
# ['When I find myself in times of trouble, Mother Mary comes to me\n', 'Speaking words of wisdom, let it be\n'......]
#
for line in lines[::-1]:  #  text v obratnom porjadke
    print(line)

# with open('/Users/Anatol/PycharmProjects/pythonProject/sample.txt', 'r') as lorem_ipsum_text:
#     text = lorem_ipsum_text.read()
# print(text)
#  #  When I find myself in times of trouble, Mother Mary comes to me
# # Speaking words of wisdom, let it be
# # And in my hour of darkness she is standing right in front of me...
# ...
# # Process finished with exit code 0


