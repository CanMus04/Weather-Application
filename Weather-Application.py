import requests

def get_weather(city, api_key):
    """Gets weather data for a city"""
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric", 
        "lang": "en"        
    }
    
    try:
        
        response = requests.get(base_url, params=params)
        
        
        if response.status_code == 200:
            weather_data = response.json()
            return weather_data
        else:
            print(f"Error: {response.status_code}")
            if response.status_code == 404:
                print(f"City '{city}' not found.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None

def display_weather(weather_data):
    """Displays weather data in a readable format"""
    if weather_data:
        city = weather_data["name"]
        country = weather_data["sys"]["country"]
        temperature = weather_data["main"]["temp"]
        feels_like = weather_data["main"]["feels_like"]
        description = weather_data["weather"][0]["description"]
        humidity = weather_data["main"]["humidity"]
        
        print(f"\nCurrent weather in {city}, {country}:")
        print(f"Temperature: {temperature}°C (feels like {feels_like}°C)")
        print(f"Conditions: {description}")
        print(f"Humidity: {humidity}%")


print("Welcome to the Weather App!")
print("With this program, you can check the current weather for any city.")


API_KEY = "your_api_key_here"  # Replace this with your own API key

while True:
    city = input("\nEnter a city name (or 'q' to quit): ")
    
    if city.lower() == 'q':
        print("Goodbye!")
        break
    
    print(f"Fetching weather data for {city}...")
    weather_data = get_weather(city, API_KEY)
    
    if weather_data:
        display_weather(weather_data)
