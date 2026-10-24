import time
import requests

print("Welcome to the weather machine! I was created to get up to date weather anywhere in the world! Lets begin!")

city = input("Where in the world would you like to know the temperature for? ")

print(f"Looking up weather for {city}")

for i in range(3):
    time.sleep(1)
    print("...")

url = "https://geocoding-api.open-meteo.com/v1/search"

response = requests.get(
    url,
    params={"name": city, "count": 1},
    timeout=10
)

data = response.json()

latitude = data["results"][0]["latitude"]
longitude = data["results"][0]["longitude"]
weather_url = "https://api.open-meteo.com/v1/forecast"
response = requests.get(
    weather_url,
    params={
    "latitude": latitude,
    "longitude": longitude,
    "current": "temperature_2m"},
    timeout=10
)
weather_data = response.json()
temperature = weather_data["current"]["temperature_2m"]
temperature_unit = weather_data["current_units"]["temperature_2m"]
print(f"the temperature in {city} is {temperature}{temperature_unit}")
