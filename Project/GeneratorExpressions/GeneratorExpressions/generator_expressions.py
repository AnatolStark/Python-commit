def get_number_from_range():
    for number in range(10):
        yield number


counter = get_number_from_range()

print(counter)
#  <generator object get_number_from_range at 0x000002509C8B9660>
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

counter1 = (number for number in range(10))
print(counter1)
#  <generator object <genexpr> at 0x000002509C8B9510>
# print(next(counter1))
# print(next(counter1))
# print(next(counter1))
# print(next(counter1))
# print(next(counter1))
# print(next(counter1))
# print(next(counter1))
# print(next(counter1))

# print([number for number in range(10)])  #  [] poluchaem spisok


# Программа на Python для генерации степеней 2
# от 2 до 256
def get_next_num():
    n = 2

    # Бесконечный цикл для генерации степеней 2
    while True:
        yield n
        n *= 2  # При последующем обращении к
        # get_next_num() выполнение
        # продолжится отсюда


# Код для проверки get_next_num()
for num in get_next_num():
    if num > 256:
        break
    print(num)


# Простая программа на Python для демонстрации
# работы yield

# Функция-генератор, которая выдает 2 при
# первом обращении, 4 — при втором и
# 8 — при третьем
def simple_generator():
    yield 2
    yield 4
    yield 8


# Код для проверки simple_generator()
for value in simple_generator():
    print(value)


