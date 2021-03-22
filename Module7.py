from bs4 import BeautifulSoup
import requests
import json

url = 'http://www.omdbapi.com/?apikey=72bc447a&t=snakes+on+a+plane'

r = requests.get(url)
json_data = r.json()
for key, value in json_data.items():
    print(key, value)