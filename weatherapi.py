import pandas as pd
import requests
import json

API_KEY='f9b73bc8d078910348d0df1a4a04a789'
weather_url=f'https://api.openweathermap.org/data/2.5/weather?q=Yangon&appid={API_KEY}'
weather_json=requests.get(weather_url).json()

df_weather = pd.json_normalize(weather_json,record_path='weather',meta=[['main','temp_min'],['main','temp_max']])

columns = ['description','main.temp_min','main.temp_max']
df_weather = df_weather[columns]
df_weather.columns = [['description','temp_min','temp_max']]

print(df_weather.head())