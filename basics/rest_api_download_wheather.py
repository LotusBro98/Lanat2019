import requests

params = {
    "key": "PASTE YOUR KEY HERE",
    "q": "56.07,37.98"
}
r = requests.get("http://api.apixu.com/v1/forecast.json", params)
dict = r.json()
temperature = dict["forecast"]["forecastday"][0]["day"]["avgtemp_c"]
print("Температура за окном:", temperature, "градусов")
