# x = 5

# while x >= 1:
     # print(x)
     # x = x - 1  # x -= 1
     # 5
     # 4
     # 3
     # 2
     # 1


# while x < 10:
#     print(x)
#     x += 1 # (x = x + 1),to she samoe ,chto (x += 1)
# 5
# 6
# 7
# 8
# 9

# while x < 10:
#     print(x)
#     x += 2
# print('Next code')
# 5
# 7
# 9
# Next code

x = 0
while x < 10:
    print(str(x) + ' x is less than 10')
    x += 1
else:
    print(str(x) + ' x now is not less than 10')
    # 0 x is less than 10
    # 1 x is less than 10
    # 2 x is less than 10
    # 3 x is less than 10
    # 4 x is less than 10
    # 5 x is less than 10
    # 6 x is less than 10
    # 7 x is less than 10
    # 8 x is less than 10
    # 9 x is less than 10
    # 10 x now is not less than 10

for x in range(10):
    print(str(x) + ' x is less than 10')
else:
    x += 1
    print(str(x) + ' x now is not less than 10')
    #  # 0 x is less than 10
    # 1 x is less than 10
    # 2 x is less than 10
    # 3 x is less than 10
    # 4 x is less than 10
    # 5 x is less than 10
    # 6 x is less than 10
    # 7 x is less than 10
    # 8 x is less than 10
    # 9 x is less than 10
    # 10 x now is not less than 10



# break, continue, pass   #

my_list = [1, 2, 3]

# for item in my_list:
#     pass  # funkzija bes tela, potom moshno vernutsja i prodolshit
# print('Another code')
# Another code

# for item in my_list:
#     if item == 2:
#         break #  otprawljaet nasad, t.e.  cikl sakanchivaetsja
#     print(item)
# 1 (1 != 2, dalee 2 = 2 i operazija sakanchivaetsja)
#
# print('Another code')
# 1
# Another code

for item in my_list:
    if item == 2:
        continue  #  vosvrashaet v pered, t.e. cikl prodolshaetsja dalshe posle 2 ,gde (1, 2, 3)
    print(item)

print('Another code')
# 1
# 3
# Another code
