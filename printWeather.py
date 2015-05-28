import sys
import Adafruit_DHT
import Adafruit_BMP.BMP085 as BMP085

humidity, temperature = Adafruit_DHT.read_retry(22, 4)
if humidity is not None and temperature is not None:
    print 'DHT reads Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
else:
    print 'DHT to get reading. Try again!'

sensor = BMP085.BMP085()

temperature = sensor.read_temperature()
pressure = sensor.read_pressure()

if temperature is not None and pressure is not None:
    print 'BMP reads Temp={0:0.1f}*C Preassure={0:0.2f} Pa'.format(temperature, pressure)
else:
    print('BMP failed to get reading. Try again!')
