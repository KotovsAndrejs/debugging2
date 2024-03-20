#
# Uzdevums:
# Izmantojot piemēru no pirma uzdevuma, izveidojiet programmu kas atspoguļos laika apstakļus (temperaturu un nokrišņus) pa stundām 
# izmantojot sekojošu datu linku 
# https://api.open-meteo.com/v1/forecast?latitude=56.8&longitude=24.2&hourly=temperature_2m,precipitation&forecast_days=1
# 
import urllib.request
import json

def get_weather_information(time):
    link = f"https://geocoding-api.open-meteo.com/v1/search?name={time}&count=3&language=en&format=json"
    
    with urllib.request.urlopen(link) as response:
        data = response.read().decode('utf-8')

    return json.loads(data)

def display_weather_information(weather_info):
    if weather_info:
        print("Weather Information:")
        for weather_data in weather_info['results']:
            print(f"Time: {weather_data['time']}")
            print(f"Temperature: {weather_data['country']}")
            print(f"Precipitation: {weather_data['precipitation']}")
            print("-----------------------")
    else:
        print("No city information available.")
        
weather_info = get_weather_information()
display_weather_information(weather_info)
