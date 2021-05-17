import requests
url = "http://api.openweathermap.org/data/2.5/weather"
api_key = "cb0714547f040ca2368ac03378d8dad0"
def weather(city_name):
    params = {"APPID": api_key, "q": city_name, "units": "metric", "lang": "ru"}
    result = requests.get(url, params=params)
    weather = result.json()
    print(weather)
    result = ""
    if weather['cod'] == '404':
        result = "Город не найден"
    else:
        result = "В городе " + weather["name"] + "\n"
        result += weather["weather"][0]["description"] + "\n"
        result += "Температура " + str(weather["main"]["temp"])+" °С" + "\n"
        result += "Ощущается " + str(weather["main"]["feels_like"])+" °С" + "\n"
        result += "Ветер "+ str(weather["wind"]["speed"])+" м/с" + "\n"
        result += "Давление " + str(weather["main"]["pressure"])+" мм.рт" + "\n"
        result += "Влажность " + str(weather["main"]["humidity"])+"%" + "\n"
        result += "Восход " + str(weather["sys"]["sunrise"]) + "\n"
        result += "Закат " + str(weather["sys"]["sunset"]) + "\n"



    return result


city_name = input("Введите название города: ")
data = weather(city_name)
print(data)
    