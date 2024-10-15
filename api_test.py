import requests

def get_weather(api_key, city_name):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    try:
        response = requests.get(base_url, params=params, timeout=10)  # Set a timeout for the request
        response.raise_for_status()  # Raise an HTTPError for bad responses
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
        print(f"Timeout error occurred: {timeout_err}")
    return None

if __name__ == "__main__":
    api_key = "d8ed53877b624518b5601493d68ba014"  # Replace with your OpenWeatherMap API key
    city = input("Enter the city name: ")  # Get city name from user input
    weather = get_weather(api_key, city)
    if weather:
        print(f"City: {weather['city']}")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Weather: {weather['description']}")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Pressure: {weather['pressure']} hPa")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
    else:
        print("Failed to get weather data")
