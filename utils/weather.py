import requests

API_KEY = "YOUR_API_KEY"

def get_weather(city="Chennai"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(url).json()

    return {
        "temperature": res["main"]["temp"],
        "humidity": res["main"]["humidity"]
    }