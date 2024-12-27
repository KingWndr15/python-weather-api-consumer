import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather_info(city):
    url = "http://api.weatherapi.com/v1/current.json"
    API_KEY = os.getenv('API_KEY')
    PARAMS = {
        "key": API_KEY,
        "q": city
    }
    try:
        response = requests.get(url=url, params=PARAMS)
        print(f"Status code: {response.status_code}")
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        return f"An error occurred: {e}"

city = "lagos"
print(get_weather_info(city))
