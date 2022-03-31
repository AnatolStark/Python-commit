from datetime import timedelta, datetime

# year = timedelta(days=365)
# print(year)

today = datetime.now()
print('Today is', today)  #  Today is 2022-03-10 17:07:04.239458
print('23 days from today will be', (today + timedelta(days=23)))  #  23 days from today will be 2022-04-02 17:08:03.436837
print('93 days from today will be', (today + timedelta(days=93)))  #  93 days from today will be 2022-06-11 17:08:03.436837
print('45 days from today will be', (today + timedelta(days=45)))  #  45 days from today will be 2022-04-24 17:08:03.436837
print('230000 seconds from today will be', (today + timedelta(seconds=230000)))  #  230000 seconds from today will be 2022-03-13 09:01:23.436837

today = datetime.now()
last_birthday = datetime(2019, 4, 1)
print('My last birthday was {0} days ago.'.format((today - last_birthday).days))  #  My last birthday was 1074 days ago.

year = timedelta(days=365)
leap_year = timedelta(days=366)
print('There are {0} seconds in a year and {1} seconds in a leap year'  #  There are 31536000.0 seconds in a year and 31622400.0 seconds in a leap year
      .format(year.total_seconds(), leap_year.total_seconds()))

print('There are {0} days in 7 years and {1} days in 7 leap years'
      .format((year * 7).days, (leap_year * 7).days))  #  There are 2555 days in 7 years and 2562 days in 7 leap years


