import requests

response = requests.get("http://api.open-notify.org/astros")
print(response.json())