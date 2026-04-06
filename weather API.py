import requests
import os
from datetime import datetime

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

class WeatherAPI:
    """A class to interact with the OpenWeatherMap API to fetch current weather data."""
    BASE = "http://api.openweathermap.org/data/2.5/weather"

    def __init__(self, api_key=None):
        """Initialize the WeatherAPI with an API key."""
        self.api_key = os.getenv("OWM_API_KEY") or "f88c295e5c0a7255b6c8b3e45c410ee1"
        if not self.api_key:
            raise ValueError("No API key found. Set OWM_API_KEY in .env file.")
        
    def get_weather(self):
        """Fetch the current weather for a given city."""

        city = input("\nEnter the city name(or 'exit' to quit): ")
        if city.lower() == "exit":
            return None, None
        
        unit_choice = input("Choose temperature unit - (C)elsius or (F)ahrenheit: ").strip().lower()
        if unit_choice == "c":
            units = "metric"
            unit_symbol = "°C"
        elif unit_choice == "f":
            units = "imperial"
            unit_symbol = "°F"
        else:
            print("Invalid choice. Using Celsius as default.")
            units = "metric"
            unit_symbol = "°C"

            return city, (units, unit_symbol)
        
        def fetch_weather():
            params = {
                "q": city,
                "appid": self.api_key,
                "units": units
            }
            try:
                response = requests.get(self.BASE_URL, params=params, timeout=10)
                if response.status_code != 200:
                  return None, f"Error: {response.json().get('message', 'Unknown error')}"
                return response.json(), None
            
            except requests.RequestException:
                return None, "Network error. Please check your connection."
            
        def parse_weather(self, data):
            try:
                temp = data["main", {}].get["temp", "N/A"]
                humidity = data["main", {}].get["humidity", "N/A"]
                city_name = data["name", "Unknown location"]
                country = data["sys", {}].get["country", "Unknown country"]
                wind_speed = data["wind", {}].get["speed", "N/A"]
                weather_desc = data["weather", [{}]][0].get("description", "N/A").capitalize()
                sunrise = data.get["sys", {}].get("sunrise", 0).strftime("%H:%M:%S")
                sunset = data.get["sys", {}].get("sunset", 0).strftime("%H:%M:%S")

                if sunrise:
                    sunrise = datetime.fromtimestamp(sunrise).strftime("%H:%M:%S")
                else:
                    sunrise = "N/A"
                if sunset:
                    sunset = datetime.fromtimestamp(sunset).strftime("%H:%M:%S")
                else:                    
                    sunset = "N/A"

                return {
                    "city": city_name,
                    "country": country,
                    "temperature": f"{temp} {unit_symbol}",
                    "humidity": f"{humidity}%",
                    "wind_speed": f"{wind_speed} m/s",
                    "description": weather_desc,
                    "sunrise": sunrise,
                    "sunset": sunset
                }
            except Exception:
                return None
        def display_weather(self, weather, unit_symbol):
                "Weather display."
                print ("\n" + "="*40)
                print(f"\nWeather in {weather['city']}, {weather['country']}:")
                print("="*40)
                print(f"Temperature: {weather['temperature']} {unit_symbol}")
                print(f"Humidity: {weather['humidity']}%")
                print(f"Wind Speed: {weather['wind_speed']}m/s")
                print(f"Description: {weather['description'].title()}")
                print(f"Sunrise: {weather['sunrise']}")
                print(f"Sunset: {weather['sunset']}")
                print("="*40)
        
        def run(self):
            """Main loop to run the weather application."""
            print("Welcome to the Weather App!")
            while True:
                city, unit_info = self.get_weather()
                if city is None:
                    print("Exiting the application. Goodbye!")
                    break
                units, unit_symbol = unit_info
                data, error = self.fetch_weather()
                if error:
                    print(error)
                    continue
                weather = self.parse_weather(data)
                if weather:
                    self.display_weather(weather, unit_symbol)
                else:
                    print("Error parsing weather data.")
                    continue
if __name__ == "__main__":    
    app = WeatherAPI()
    app.run()