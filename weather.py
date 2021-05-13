import requests
url = "http://api.openweathermap.org/data/2.5/weather"
api_key = "cb0714547f040ca2368ac03378d8dad0"
params = {"APPID": api_key, "q": "Новосибирск", "units": "metric", "lang": "ru"}
result = requests.get(url, params=params)
weather = result.json()
print(result.url)