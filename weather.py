import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def current_weather(city):
    # print('\n*** Getting Current Weather Condition*** 🌡️🌡️🌡️\n')
    # city = input('\nPlease Enter a city name:\n')
    
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    
    # print(request_url)
    weather_details = requests.get(request_url).json()
    
    return weather_details
    # print(weather_details)
    # pprint(weather_details)
    # print(f'\nCurrent weather for {weather_details["name"]}')
    # print(f'\nThe Temperature is for {weather_details["main"]["temp"]}')
    # print(f'\nFeels like {weather_details["main"]["feels_like"]} and {weather_details["weather"][0]["description"]}')
       
    
if __name__ == "__main__":   
    print('\n*** Getting Current Weather Condition*** 🌡️🌡️🌡️\n')
    city = input('\nPlease Enter a city name: ')
    
    if not bool(city.strip()):
        city = "Kolkata"
    
    weather_details = current_weather(city)
    print("\n")
    pprint(weather_details)