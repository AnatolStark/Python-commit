# car_prices = {'opel': 5000, 'toyota': 7000, 'bmw': 10000 } # {} slovar sodershit kluch i snachenie
# print(car_prices)  #  {'opel': 5000, 'toyota': 7000, 'bmw': 10000 }
# print(car_prices['toyota'])  # 7000
# car_prices['mazda'] = 4000  # dobavlenie b slovar
# print(car_prices)  #   {'opel': 5000, 'toyota': 7000, 'bmw': 10000, 'mazda' : 4000}
# car_prices['opel'] = 2000  #  esli odinakovye kluchi, to idet samena snachenija
# print(car_prices)  #   {'opel': 2000, 'toyota': 7000, 'bmw': 10000, 'mazda' : 4000}
# del car_prices['toyota']   #  del - udalenie klucha
# print(car_prices)  #   {'opel': 5000, 'bmw': 10000, 'mazda' : 4000}
# # del car_prices
# car_prices.clear()  #  metod clear - ochistka clovarja
# print(car_prices)  #  {}

person = {
    'first name': 'Jack',
    'last name': 'Brown',
    'age': 43,
    'hobbies': ['football', 'singing', 'photo'],  #  spisok
    'children': {'son': 'Michael', 'daugter': 'Pamela'}  #  slovar
}

print(person['age'])  #  43
print(person['hobbies'])  #  ['football', 'singing', 'photo']
hobbies = person['hobbies']
print(hobbies[2])  #  photo

print(person['hobbies'][2])  #  photo


children = person['children']
print(children['son'])  #  Michael

print(person['children']['son'])  #  Michael

person['car'] = 'Mazda'
print(person)  #  {'first name': 'Jack', 'last name': 'Brown', 'age': 43, 'hobbies': ['football', 'singing', 'photo'], 'children': {'son': 'Michael', 'daugter': 'Pamela'}, 'car': 'Mazda'}
person['hobbies'][0] = 'basketball'  #  samena

print(person.keys())  #  dict_keys(['first name', 'last name', 'age', 'hobbies', 'children', 'car'])
print(person.values())  #  dict_values(['Jack', 'Brown', 43, ['basketball', 'singing', 'photo'], {'son': 'Michael', 'daugter': 'Pamela'}, 'Mazda'])
print(person.items())  #  dict_items([('first name', 'Jack'), ('last name', 'Brown'), ('age', 43), ('hobbies', ['basketball', 'singing', 'photo']), ('children', {'son': 'Michael', 'daugter': 'Pamela'}), ('car', 'Mazda')

smartphone_prices = {"samsung": 530, 'apple': 839, "huawei": 299}
print(smartphone_prices["apple"])

# dictionary, opisyvaet computer
computer = {
    'brand': 'medion akoya',
    'prozessor': 'core',
    'RAM': '8GB',
    'SSD': '512GB',
    'color': 'silver'
}