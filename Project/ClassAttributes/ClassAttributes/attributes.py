class Car:

    wheels_number = 4  # pri odinakovyh snachenijah pischetsja otdelno cverhu

    def __init__(self, name, color, year, is_crashed):  # init - sosdat
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed  #  byla v avarii


mazda_car = Car(name='Mazda CX7', color='red', year=2017, is_crashed=True)

print(mazda_car.name)
#  Mazda CX7
print(mazda_car.is_crashed)
#  True
print(mazda_car.wheels_number)
#  4

bmw_car = Car(name='BMW', color='black', year=2018, is_crashed=False)

print(bmw_car.name)
#  BMW
print(bmw_car.year)
#  2018
print(bmw_car.wheels_number)
#  4
print(bmw_car.is_crashed)
#  False

number_of_wheels_3_car = Car.wheels_number * 3
print(number_of_wheels_3_car)
#  12

class BlogPost:
    def __init__(self, user_name, text, number_of_likes):
        self.user_name = user_name
        self.text = text
        self.number_of_likes = number_of_likes

my_blog_post = BlogPost(user_name='Anatol', text='Hello Darling!', number_of_likes= 8)
blog_post = BlogPost('Jon', 'Hi my friend', 8)

blog_post.number_of_likes = 30
print(my_blog_post.number_of_likes)
# 8

print(blog_post.number_of_likes)
#  30

class BlogPost:
    def __init__(self, user_name, text, number_of_likes):
        self.user_name = user_name
        self.text = text
        self.number_of_likes = number_of_likes


post_about_politicians = BlogPost('John', 'I like politicians', 0)
post_about_cats = BlogPost('Jane', 'I like cats', 0)

post_about_cats.number_of_likes = 1000

print(post_about_politicians.number_of_likes)
print(post_about_cats.number_of_likes)
