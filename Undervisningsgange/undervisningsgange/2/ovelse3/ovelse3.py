import sqlite3
import Adafruit_DHT

conn = sqlite3.connect('dht11.db')

query = 'INSERT INTO airdata (Datetime, Temperature, Humidity) VALUES(?,?,?)'
data = (Time, Temp, Humi)

sensor = Adafruit_DHT.DHT11
pin = 23

Time = 
Temp = temperature = Adafruit_DHT.read_retry(sensor, pin)
Humi = humidity = Adafruit_DHT.read_retry(sensor, pin)


try:
    cur = conn.cursor()
    cur.execute('SELECT * FROM airdata')