import sqlite3
import Adafruit_DHT
import datetime

conn = sqlite3.connect('dht11.db')

query = 'INSERT INTO airdata (Datetime, Temperature, Humidity) VALUES(?,?,?)'
data = (Time, Temp, Humi)

sensor = Adafruit_DHT.DHT11
pin = 23

timedata = datetime.datetime.now()

temperature = Adafruit_DHT.read_retry(sensor, pin)
humidity = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading. Try again!')

Time = str(timedata)
Temp = temperature
Humi = humidity


try:
    cur = conn.cursor()
    cur.execute(query, data)
    conn.commit()
except sqlite3.Error as e:
    conn.rollback()
    print(f'Could not insert ! {e}')


finally:
    conn.close()
    
