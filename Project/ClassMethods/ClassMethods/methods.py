class Car:

     wheels_number = 4

     def __init__(self, name, color, year, is_crashed):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed

     def drive(self, city):
        print(self.name + ' is driving to ' + city)

     def change_color(self, new_color):
        self.color = new_color


opel_car = Car('Opel Tigra', 'grey', '1999', True)
opel_car.drive('London')
#  Opel Tigra is driving to London
mazda_car = Car('Mazda CX7', 'black', 2014, False)
mazda_car.drive('Paris')
#  Mazda CX7 is driving to Paris
mazda_car.change_color('yellow')
print(mazda_car.color)
#  yellow
#
#
#
# # print(opel_car.drive)
# # print(opel_car.wheels_number)
# # print(opel_car.name)
# # print(opel_car.color)
# # print(opel_car.year)
# # print(opel_car.is_crashed)


class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.circumference = 2 * Circle.pi * self.radius

    def get_area(self):    #  poluchit ploshad kruga
        return self.pi * (self.radius ** 2)

    # def get_circumference(self):  #  dlina okrushnosti
    #     return 2 * self.pi * self.radius



circle_1 = Circle(5)
print(circle_1.get_area())
print(circle_1.circumference)
# print(circle_1.get_circumference())
# circle_2 = Circle(3)
# print(circle_2.get_area())
# print(circle_2.get_circumference())
# circle_3 = Circle(5)
# circle_area = circle_3.get_area()
# print(circle_area)
# print(circle_3.get_circumference())

class BankAccount:

    def __init__(self, client_id, client_first_name, client_last_name, balance):  # moshno  "balance" ne vnosit
        self.client_id = client_id
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        self.balance = balance = 0.0

    def add(self, ante):
        self.balance += ante

    def withdraw(self, ante):  #  withdraw  snjat co scheta
        self.balance -= ante

bank_account = BankAccount(578946, 'Max', 'Stern', 'balance')  # esli v __init__ 'balance' net, to i sdes ne nado

bank_account.add(1000)
print(bank_account.balance)
bank_account.withdraw(500)
print(bank_account.balance)

class Gamer:

    active_gamers = 0

    # metod class

    @classmethod
    def get_active_gamers(cls):
        print(cls)
        return Gamer.active_gamers

    @classmethod
    def gamer_from_string(cls, data_string):  #  sosdanie igroka is stroki
        nickname, age, level, points = data_string.split(',')
        return cls(nickname, age, level, points)



    def __init__(self, nickname, age, level, points):
        self.nickname = nickname
        self.age = age
        self.level = level
        self.points = points
        Gamer.active_gamers += 1

    def logout(self):
        Gamer.active_gamers -= 1

    def get_nickname(self):
        return self.nickname

    def get_age(self):
        return self.age

    def get_level(self):
        return self.level

    def get_points(self):
        return self.points

    def is_adult(self):
        return self.age >= 18

    def get_adult_level_permission(self):
        if self.is_adult():
            print('You can go to adult level')
        else:
            print("You can\'t go to adult level")

print(Gamer.active_gamers)
#  0

gamer_1 = Gamer('hell_boy', 23, 5, 13)
gamer_2 = Gamer('heli_boy', 13, 7, 34)
print(Gamer.active_gamers)
#  2

gamer_3 = Gamer('harry_potter', 35, 13, 125)

print(gamer_1.get_age())
gamer_1.get_adult_level_permission()
#  23
#  You can go to adult level

print(gamer_2.get_age())
gamer_2.get_adult_level_permission()
#  13
#  You can't go to adult level

print(gamer_3.get_age())
print(gamer_3.get_adult_level_permission())
#   35
# You can go to adult level
# None, t.k. pered ('gamer_3.get_adult_level_permission())' ctoit 'print'

print(Gamer.active_gamers)
#  3

gamer_1.logout()
print(Gamer.active_gamers)
#  2
Gamer.get_active_gamers()
#  <class '__main__.Gamer'>

print(Gamer.get_active_gamers())  # cheres metod '@classmethod'
#  2

#  james = Gamer.gamer_from_string('hell', 23, 5, 13)
#  jane = Gamer.gamer_from_string('harry', 35, 13, 125)

#  sosdanie spiska is slovarja

my_dict = dict.fromkeys((1, 2, 3), ('apple', 'orange', 'banana'))
print(my_dict)
# {1: ('apple', 'orange', 'banana'), 2: ('apple', 'orange', 'banana'), 3: ('apple', 'orange', 'banana')}




