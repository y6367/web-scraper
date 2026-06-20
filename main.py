import datetime
from weather import get_weather
from database import insert_weather
from charts import show_charts

while True:
    print("Welcome to the Weather CLI, what do you want to do?")
    print("1. Log today's weather")
    print("2. View temperature chart")
    print("3. Quit")
    action = input("Input: ")

    if action == "1":
        date = datetime.datetime.now().date()
        name, temp, feels_like, humidity, wind, description = get_weather("Seattle")
        insert_weather(date, name, temp, feels_like, humidity, wind, description)
    elif action == "2":
        show_charts()
    else:
        break