# utils.py
def get_favorite_color():
    return 'super-duper color'


def get_favorite_number():
    return 13


print(get_favorite_color())
# super-duper color
print(get_favorite_number())
#  13

from utils import get_favorite_color as main_file
get_favorite_color()

from utils import get_favorite_number as main_file
get_favorite_number()
# super-duper color
#  13

# utils.py
def get_favorite_color():
    return 'super-duper color'


def get_favorite_number():
    return 13
#  super-duper color
#  13

# main_file.py
import utils

color = utils.get_favorite_color()
number = utils.get_favorite_number()

print(color)
print(number)
#  super-duper color
#  13