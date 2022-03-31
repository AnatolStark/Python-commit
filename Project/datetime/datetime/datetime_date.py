from datetime import date

# today = date.today()
# print(today)   #  2022-03-09 15:40:02.074988
# print(today.year)
# print(today.month)
# print(today.day)

# date_1 = date(2019, 12, 25)
# date_2 = date(2018, 12, 25)
# diff = date_1 - date_2
# print(diff)  #  365 days, 0:00:00
# print(type(date_1))  #  <class 'datetime.date'>
# print(type(date_2))  #  <class 'datetime.date'>
# print(type(diff))   # <class 'datetime.timedelta'>


# today = date.today()
# print(today)
#
# my_birthday = date(today.year, 4, 1)
# if my_birthday < today:
#     my_birthday = my_birthday.replace(year=today.year + 1)
# print(my_birthday)
# days_until_birthday = my_birthday - today
# print('You will celebrate your birthday in', days_until_birthday.days, 'days!') # #  You will celebrate your birthday in 351 days, 0:00:00 days!


# today = date.today()
#
# week_day = today.weekday()
# print(week_day)  #  2 ,t.e. sreda

# week_day = today.isoweekday()
# print(week_day)  #  3 ,t.e. sreda


year = input('Please enter a year ')
month = input('Please enter a month ')
day = input('Please enter a day ')

date_1 = date(int(year), int(month), int(day))
# print(date_1)

week_day = date_1.weekday()

if week_day == 0:
    print(date_1, 'is a Monday.')
elif week_day == 1:
    print(date_1, 'is a Tuesday.')
elif week_day == 2:
    print(date_1, 'is a Wednesday.')
elif week_day == 3:
    print(date_1, 'is a Thursday.')
elif week_day == 4:
    print(date_1, 'is a Friday.')
elif week_day == 5:
    print(date_1, 'is a Saturday.')
elif week_day == 6:
    print(date_1, 'is a Sunday.')  #  2032-10-21 is a Thur.


