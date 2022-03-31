test = 5
test1 = 5.7
test2 = 'Abraham'
print('test')


from colorama import init
from colorama import Fore, Back, Style

init()
print(Fore.BLACK)
print(Back.GREEN)





a = float(input('Erste number:'))
print(Back.YELLOW)
what = input('(+, -):')
print(Back.CYAN)
b = float(input('Zweite number:'))
print(Back.YELLOW)




if what == '+':
	c = a + b
	print(str(c))
elif what == '-':
	c = a - b
	print(str(c))
else:
	print('False')