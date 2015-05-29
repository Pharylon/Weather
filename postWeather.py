import sys
import Adafruit_DHT
import Adafruit_BMP.BMP085 as BMP085
import requests

def getReadings():
    humidity, dht_temp = Adafruit_DHT.read_retry(22, 4)
    if humidity is not None and dht_temp is not None:
        bmp_sensor = BMP085.BMP085()
        pressure = bmp_sensor.read_pressure()
        bmp_temp = bmp_sensor.read_temperature()
        if pressure is not None and bmp_temp is not None:
            data = {}
            data['temperatureBmp'] = bmp_temp
            data['temperatureDht'] = dht_temp
            data['humidity'] = humidity
            data['pressure'] = pressure
            return data
    return None


data = getReadings()
print(data)
requests.post('http://pharylonapi.azurewebsites.net/api/weather/reading', data)
