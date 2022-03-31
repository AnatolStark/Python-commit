# Generators are iterators
# Generators can be created with generator functions
# Generators can be created with generator expressions


# def my_function(x):
#     return x
#
#
# print(my_function(4))


def count_up_to(x):
    count = 1
    while count <= x:
        yield count   #  yield - vyrabatyvaetsja
        count += 1


# print(count_up_to(4))
# counter = count_up_to(4)
# # print(counter.__next__())
# # print(counter.__next__())
# # print(counter.__next__())
# # print(counter.__next__())
# # print(counter.__next__())
#
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

counter = count_up_to(10)  # schetchik
print(list(count_up_to(7)))
#  [1, 2, 3, 4, 5, 6, 7]

# for number in counter:
#     print(number)

counter.__next__()
counter.__next__()
counter.__next__()

for number in counter:
    print(number)
#  4
# 5
# 6
# 7
# 8
# 9
# 10

def get_week_day():
    week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for day in week_days:
        yield day
        print(day)


current_day = get_week_day()

current_day.__next__()
current_day.__next__()
current_day.__next__()
current_day.__next__()
current_day.__next__()
current_day.__next__()
current_day.__next__()



def even_odd():
    word = 'even'
    while True:
        yield word
        if word == 'even':
           word = 'odd'
        else:
            word = 'even'

        print(word)

even_odd_generator = even_odd()

even_odd_generator.__next__()
even_odd_generator.__next__()
even_odd_generator.__next__()
even_odd_generator.__next__()
even_odd_generator.__next__()








