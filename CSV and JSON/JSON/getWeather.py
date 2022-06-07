#! python3
# WARNING - THIS PROGRAM ONLY WORKS WITH A PAID SUBSCRIPTION TO https://openweathermap.org/. CURRENTLY WILL NOT WORK
import json, requests, sys

APPID = 'eb98d602f51c49ad4dca604109e36d63' # To access openweather API

# detect location from command line
if len(sys.argv) < 2:
	print('Usage: "getWeather.py city_name, 2-letter_country_code"')
	sys.exit()

location = ' '.join(sys.argv[1:])

# Download the JSON data Openweathermap.org API.
url = 'https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s' % (location, APPID)
response = requests.get(url)
response.raise_for_status()

print(response.text) # Raw JSON text

# Load JSON data in Pythons variable
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow: ')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])




