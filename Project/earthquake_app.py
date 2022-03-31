import requests
import sqlite3


def save_eartquakes(place_magnitude_list):
	conn = sqlite3.connect("earthquakes_db.db")
	cursor = conn.cursor()
	cursor.execute("CREATE TABLE earthquakes (place TEXT, magnitude REAL)")
	cursor.executemany("INSERT INTO earthquakes VALUES (?, ?)", place_magnitude_list)
	conn.commit()
	conn.close()


url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'


start_time = input('Enter the start time')
end_time = input('Enter the end time')
latitude = input('Enter the latitude')
longitude = input('Enter the longitude')
max_radius_km = input('Enter the max radius in km')
min_magnitude = input('Enter the min magnitude')

response = requests.get(url, headers={'Accept':'application/json'}, params={
		'format':'geojson',
		'starttime':start_time,
		'endtime':end_time,
		'latitude':latitude,
		'longitude':longitude,
		'maxradiuskm':max_radius_km,
		'minmagnitude':min_magnitude

	})

data = response.json()

earthquake_list = data['features']
place_magnitude_list = []
count = 0
for earthquake in earthquake_list:
	count += 1
	place_magnitude_list.append((earthquake['properties']['place'],earthquake
        ['properties']['mag']))

save_eartquakes(place_magnitude_list)









