import requests
import pytz
import time
import os
from colorama import Fore, Style
from datetime import datetime

def get_weather_info():
  api_key = 'your api_key'
  latitude = 'your latitude'
  longitude = 'your longitude'
  url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&APPID={api_key}'
  response = requests.get(url)

  if response.status_code == 200:
    data = response.json()
    location = data['name']
    description = data['weather'][0]['description']
    temperature = data['main']['temp'] -273.15
    feels_like = data['main']['feels_like'] -273.15
    min_temp = data['main']['temp_min'] -273.15
    max_temp = data['main']['temp_max'] -273.15
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    print(Fore.GREEN + Style.BRIGHT + f"Location: {Style.RESET_ALL}{location}")
    print(Fore.CYAN + Style.BRIGHT + f"Description: {Style.RESET_ALL}{description}")
    print(Fore.BLUE + Style.BRIGHT + f"Temperature: {Style.RESET_ALL}{temperature:.2f} °C")
    print(Fore.BLUE + Style.BRIGHT + f"Feels like: {Style.RESET_ALL}{feels_like:.2f} °C")
    print(Fore.BLUE + Style.BRIGHT + f"Min Temperature: {Style.RESET_ALL}{min_temp:.2f} °C")
    print(Fore.BLUE + Style.BRIGHT + f"Max Temperature: {Style.RESET_ALL}{max_temp:.2f} °C")
    print(Fore.YELLOW + Style.BRIGHT + f"Humidity: {Style.RESET_ALL}{humidity}%")
    print(Fore.YELLOW + Style.BRIGHT + f"Wind speed: {Style.RESET_ALL}{wind_speed} m/s")

    timezone = pytz.timezone('America/New_York')
    current_time = datetime.now(timezone)
    formatted_time = current_time.strftime("%I:%M:%S %p")
    print (Fore.RED + Style.BRIGHT + f"Current Time: {Style.RESET_ALL}{formatted_time}")

  else:
    print(Fore.RED + Style.BRIGHT + f"ERROR: STATUS CODE: {Style.RESET_ALL}{response.status_code}")

while True:
  get_weather_info()
  time.sleep(2)
  os.system('clear')
