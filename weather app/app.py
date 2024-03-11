import requests

api_key = '56a1b3d2cce54f496b845c803279658e'

City = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={City}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    print(f"The weather in {City} is: {weather}")
    print(f"The temperature in {City} is: {temp}ºF")