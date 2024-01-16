import requests
import json

def get_weather(api_key,location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q":location,
        "appid":api_key,
        "units":"metric"
    }

    response = requests.get(base_url,params=params)

    if response.status_code == 200:
        weather_data = json.loads(response.text) 
        return weather_data
    else:
        return None
    
def display_weather(weather_data):
    if weather_data:
        print(f"Weather in {weather_data['name']}, {weather_data['sys']['country']}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Weather Conditions: {weather_data['weather'][0]['description']}")
    else:
        print("Error occured while fetching the weather data")

if __name__ == "__main__":
    api_key = "9927aff3699d682e6a04108e1bc6baf1"
    location = input("Enter city or ZIP code: ")

    weather_data = get_weather(api_key,location)

    display_weather(weather_data)
    

    


       
    
   