# import shelve

#  with shelve.open('shelve_test') as cars:
    # cars['opel'] = 'Germany'
    # cars['ford'] = 'USA'
    # cars['mazda'] = 'Japan'
    # cars['renault'] = 'France'

    # print(cars['opel'])
    # print(cars['ford'])
    # print(cars['mazda'])
    # print(cars['renault'])
    #  Germany
    # USA
    # Japan
    # France
     # print(cars['renau'])

    # del cars['renau']

    # cars['kia'] = 'South Korea'

    # for key in cars:
        # print(key + ':' + cars[key])
    # opel:Germany
    # ford:USA
    # mazda:Japan
    # renault:France
    # kia:South Korea


import shelve

university = shelve.open('university_file')
university['schedules'] = {

        'monday_schedule': ['Math', 'English language', 'System programming', 'Python'],
        'tuesday_schedule': ['English language', 'HTML', 'Python', 'Football'],
        'wednesday_schedule': ['Physics', 'English language', 'Python'],
        'thursday_schedule': ['Math', 'Chemistry', 'Java'],
        'friday_schedule': ['Running', 'Math', 'Python']
    }
university['tutors'] = {
        'Math': ['Jack White', 'Jim Black'],
        'Python': ['YouRa Allakhverdov', 'Jane Smith']
    }


x = university['schedules']
print(type(x))
#  <class 'dict'>
print(university['schedules']['wednesday_schedule'])
#  ['Physics', 'English language', 'Python']
print(university['tutors']['Math'])
#  ['Jack White', 'Jim Black']

university.close()

# university = {
#     'schedules': {
#         'monday_schedule': ['Math', 'English language', 'System programming', 'Python'],
#         'tuesday_schedule': ['English language', 'HTML', 'Python', 'Football'],
#         'wednesday_schedule': ['Physics', 'English language', 'Python'],
#         'thursday_schedule': ['Math', 'Chemistry', 'Java'],
#         'friday_schedule': ['Running', 'Math', 'Python']
#     },
#
#     'tutors': {
#         'Math': ['Jack White', 'Jim Black'],
#         'Python': ['YouRa Allakhverdov', 'Jane Smith']
#     }
# }
#
# print(university['schedules']['wednesday_schedule'])
# print(university['tutors']['Math'])

