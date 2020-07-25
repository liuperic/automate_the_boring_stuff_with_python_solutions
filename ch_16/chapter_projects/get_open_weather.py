#!/usr/bin/env python3
# get_open_weather.py - Prints the weather for a location from the command line.

# Note: Using different url than book as it seems that specific API for OpenWeatherMap.org
# is now a paid service.
# Cannot show more than current day forecast with free version.

# Edit and enter your API ID below
APPID = '<Your_API_ID>'

import json, requests, sys

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, if_applicable_2-letter_state_code 2-letter_country_code')
    sys.exit()

unparsed_loc = ' '.join(sys.argv[1:])

# Check if location has necessary state code. (Locations in the U.S. for example need state code for API)
state = input('Is there an applicable 2 letter state code for the location? (y/n) ')
if state == 'y':
    location = '+'.join(sys.argv[1:-2]) + sys.argv[-2] + sys.argv[-1]
else:
    location = ''.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API.
url ='https://api.openweathermap.org/data/2.5/weather?q=%s&APPID=%s' % (location, APPID)
response = requests.get(url)
response.raise_for_status()

# Uncomment to see the raw JSON text:
# print(response.text)

# Load JSON data into a Python variable.
weather_data =json.loads(response.text)

# Print weather descriptions of current day
w = weather_data['weather']
print('Current weather in %s:' % (unparsed_loc))
print(w[0]['main'], '-', w[0]['description'])
