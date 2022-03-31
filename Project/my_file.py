def get_access(password):
    password_list = [111, 222, 333]
    assert int(password) in password_list, 'Password is invalid'
    print('You can make dangerous stuff')


password_1 = input('Please input the password')
get_access(password_1)

import pyowm

owm = pyowm.OWM('your-API-key', language = 'ru')

place = input('Welche Stadt?:')

observation = owm.weather_at_place(place)
w = observation.get_weather()

temp = w.get_temperature('celsius')['temp']

print('В городе' + place + 'сейчас' + w.get_detailed_status())
print( 'Temperatura seichas' + str(temp))

if temp < 10:
    print('Prochladno!')
elif temp < 20:
    print('Normalno!')
else:
    print('Otlichno!')

