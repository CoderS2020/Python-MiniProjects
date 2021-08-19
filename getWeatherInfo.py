import requests
from pprint import pprint #Pretty-print converts from json to dictionary tree

API_KEY='your key will come here'

city=input("Enter your city: ")
base_url="http://api.openweathermap.org/data/2.5/weather?appid="+API_KEY+"&q="+city
weather_data=requests.get(base_url).json();

pprint(weather_data)
