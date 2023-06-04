import requests
import os # for accessing the API key from environment variables.

API_KEY = os.environ["WEATHER_API_KEY"] # Your API key goes here.

def current_weather():
    '''This function is used to generate the current weather condition of given location.'''

    QUERY = "&q=" + input("Enter location (Can also pass coordinates in the form: lat long): ")
    AQI = "&aqi=" + input("Do You Want To Include Air Quality Aswell? (yes/no): ")

    URL = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}{QUERY}{AQI}"
    
    response = requests.get(URL)
    data = response.json()
    location = data["location"]
    weather = data["current"]

    print("Name:", location["name"])
    print("Region:", location["region"])
    print("Country:", location["country"])
    print("Local Time:", location["localtime"].split(" ")[1])
    print("Coordinates:", location["lat"], location["lon"])

    print("Last Updated:", weather["last_updated"].split(" ")[1])
    print("Temperature:", weather["temp_c"], "℃", " (", weather["temp_f"], "℉ )")
    print("Wind:", weather["wind_kph"], "Kmph", "(", weather["wind_mph"], "Mph", ")")
    print("Condition: ", weather["condition"]["text"])
    
    try:
        '''If the user has not inputter AQI as 'yes' then key error will be generated.'''
        aqi = weather["air_quality"]
    except KeyError:
        pass
    else:
        print("PM2.5: ", aqi["pm2_5"])
        print("PM10: ", aqi["pm10"])

def forecast():
    '''This function is used to generate weather forecast of upto 10 days'''
    QUERY = "&q=" + input("Enter location (Can also pass coordinates in the form: lat long): ")
    DAYS = "&days=" + input("Number of days of weather forecast (Upto 10): ")
    AQI = "&aqi=" + input("Do You Want To Include Air Quality Aswell? (yes/no): ")
    URL = f"https://api.weatherapi.com/v1/forecast.json?key={API_KEY}{QUERY}{DAYS}{AQI}"

    response = requests.get(URL)
    data = response.json()
    location = data["location"]
    forecast = data["forecast"]
    days = forecast["forecastday"]

    print("Name:", location["name"])
    print("Region:", location["region"])
    print("Country:", location["country"])
    print("Local Time:", location["localtime"].split(" ")[1])
    print("Coordinates:", location["lat"], location["lon"])

    for day in days:
        print("\n")
        date = day["date"].split("-")
        date = "-".join(date[::-1])
        print("Date:", date)
        weather = day["day"]
        print("Maximum Temp: ", weather["maxtemp_c"], "℃ (", weather["maxtemp_f"], "℉ )")
        print("Minimum Temp: ", weather["mintemp_c"], "℃ (", weather["mintemp_f"], "℉ )")
        print("Average Temp: ", weather["avgtemp_c"], "℃ (", weather["avgtemp_f"], "℉ )")
        print("Wind:", weather["maxwind_kph"], "Kmph", "(", weather["maxwind_mph"], "Mph", ")")
        print("Chance Of Raining: ", weather["daily_chance_of_rain"], "%")
        print("Condition: ", weather["condition"]["text"])
        try:
            '''If the user has not inputter AQI as 'yes' then key error will be generated.'''
            aqi = weather["air_quality"]
        except KeyError:
            pass
        else:
            try:
                '''Sometimes the data is not available in forecasting.'''
                print("PM2.5: ", aqi["pm2_5"])
                print("PM10: ", aqi["pm10"])
            except KeyError:
                print("PM2.5: No data")
                print("PM10: No data")

running=False
while running:
    print("\nExit the program -> Enter 0")
    print("Current Weather -> Enter 1")
    print("Weather Forecasting -> Enter 2")
    ch = input("Choose one of the following:")
    if ch=='0':
        running=False
        print("Program Terminated...")
    elif ch=='1':
        print('\n')
        current_weather()
    elif ch=='2':
        print('\n')
        forecast()
    else:
        print("Invalid input, Please try again")