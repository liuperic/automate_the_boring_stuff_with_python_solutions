#!/usr/bin/env python3
# umbrella_reminder.py - Checks weather every morning

import bs4, requests, schedule, time

def get_weather():
    # Currently getting weather for San Francisco. Edit link with your own location.
    res = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.7771&lon=-122.4196')
    res.raise_for_status()
    weather_soup = bs4.BeautifulSoup(res.text, 'html.parser')

    forecast_elem = weather_soup.select('.col-sm-10')
    # Prints string of current weather forecast
    print(forecast_elem[0].getText())

schedule.every().day.at("07:30").do(get_weather)

while True:
    schedule.run_pending()
    time.sleep(1)
