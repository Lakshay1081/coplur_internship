import requests

def weather_details(city, api_key):
    final_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(final_url)
        response.raise_for_status()
        data = response.json()

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        feels_like = data["main"]["feels_like"]
        description = data["weather"][0]["description"].capitalize()

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C (Feels like: {feels_like}°C)")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")

    except requests.exceptions.RequestException as a:
        print(f"Error fetching weather data: {a}")

api_key = "193354bd588c02626a0f569688308bc9"
city = input("Enter city name: ")

weather_details(city, api_key)
