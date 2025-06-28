import requests

API_KEY="ba0a3f5216f5dcb78a2e48552e4e6785"  # 👈 Replace this
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(BASE_URL, params=params)
data = response.json()

print(data)  # 👈 See exact reason if anything fails

if data.get("cod") == 200:
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    print(f"\nWeather in {city.title()}:")
    print(f"Condition: {weather}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
else:
    print("❌ City not found or error in API.")
