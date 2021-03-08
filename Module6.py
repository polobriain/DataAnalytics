
import json
import requests

# data = requests.get("http://api.open-notify.org/astros.json")
data = requests.get("http://api.open-notify.org/astros.json")

print(type(data))
print(data('name'))