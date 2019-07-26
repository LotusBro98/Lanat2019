import requests

params = {
    "key": "d9e7c392a09e442b9c075922192507",
    "q": "56.07,37.98",
    "days": 5
}
r = requests.get("http://api.apixu.com/v1/forecast.json", params)
dict = r.json()
days_dict = dict["forecast"]["forecastday"]

print('Прогноз погоды на 5 дней:')
for day_dict in days_dict:
    print(day_dict["date"], ":", day_dict["day"]["avgtemp_c"], "градусов")
