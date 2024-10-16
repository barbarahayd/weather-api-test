import os
import requests
import logging
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv() # load environment variables from .env file

def get_weather(api_key, city_name):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # celsius temperature unit
    }
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()  # exceção para respostas de erro (4xx, 5xx)
        data = response.json()
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'wind_speed': data['wind']['speed']
        }
        return weather
    except requests.exceptions.Timeout as timeout_err:
        logging.error(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        logging.error(f"Error during the request: {req_err}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    return None

def display_weather(weather):

    print(f"City: {weather['city']}")
    print(f"Temperature: {weather['temperature']:.2f}°C")
    print(f"Weather: {weather['description'].capitalize()}")
    print(f"Humidity: {weather['humidity']}%")
    print(f"Pressure: {weather['pressure']} hPa")
    print(f"Wind Speed: {weather['wind_speed']} m/s")

if __name__ == "__main__":
    api_key = os.getenv('OPENWEATHER_API_KEY')  # acesso a chave da API de uma variável de ambiente
    if not api_key:
        logging.error("API key not found. Please set the OPENWEATHER_API_KEY environment variable.")
        exit(1)

    city = input("Enter the city name: ").strip()  # get city name from user input

    if not city:
        logging.error("Invalid city name. Please enter a valid city name.")
        exit(1)

    weather = get_weather(api_key, city)
    if weather:
        display_weather(weather)
    else:
        logging.error("Failed to get weather data")
        
input("\nPress Enter to exit...")
