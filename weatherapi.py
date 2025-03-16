import pandas as pd
import requests
import json
import os

API_KEY=os.getEnv['API KEY']
weather_url = f'https://api.openweathermap.org/data/2.5/weather?q=Yangon&appid={API_KEY}'

# Fetch json data from weather_url
weather_json = requests.get(weather_url).json()

# Flatten the nested json file
df_weather = pd.json_normalize(weather_json,record_path='weather',meta=[['main','temp_min'],['main','temp_max']])

columns = ['description','main.temp_min','main.temp_max']
df_weather = df_weather[columns]
df_weather.columns = [['description','temp_min','temp_max']]

print(df_weather.head())