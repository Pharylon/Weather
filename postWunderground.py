import requests

def getForecast(apiObj):
    forecast = {}
    forecast['high'] = apiObj['high']['celsius']
    forecast['low'] = apiObj['low']['celsius']
    forecast['dateFor'] = apiObj['date']['epoch']
    forecast['humidity'] = apiObj['avehumidity']
    return forecast
    

r = requests.get('http://api.wunderground.com/api/58ad3c15401bd354/forecast/q/NC/Cherryville.json')
response = r.json()
forecasts = response['forecast']['simpleforecast']['forecastday']
data = []
for f in forecasts:
    data = getForecast(f)
    requests.post('http://pharylonapi.azurewebsites.net/api/weather/forecast', data)

