import requests

def get_weather_info(city):
    url = "http://api.weatherapi.com/v1/current.json"
    PARAMS = {
        "key": "ae4c48ab7cd141b282d151037242906",
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
