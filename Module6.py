
import json
import requests

# data = requests.get("http://api.open-notify.org/astros.json")
data = requests.get("http://www.zurichbroker.ie")
text = data.text
print(text)
# print(type(data))
# print(data('name'))