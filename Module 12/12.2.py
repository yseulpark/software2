import requests, json
city = input("Enter the name of a city: ")
api_key = "cf5fe9c15e666e5c45bb90f61ab93e9f"
request = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
response = requests.get(request).json()
if response.get("cod") != 200:
    print(f"Error: {response.get('message','unknown error')} ")
else:
    description = response["weather"][0]["description"]
    temp_celsius = response["main"]["temp"] - 273.15
    print(f"The weather in {city}: {description} | Temperature: {temp_celsius:.1f} Celsius degrees")
