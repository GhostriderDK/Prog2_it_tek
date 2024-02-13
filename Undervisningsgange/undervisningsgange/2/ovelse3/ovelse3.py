import sqlite3
import Adafruit_DHT
import RTC
from time import sleep


conn = sqlite3.connect('dht11.db')

query = 'INSERT INTO airdata (Datetime, Temperature, Humidity) VALUES(?,?,?)'
data = (Time, Temp, Humi)

sensor = Adafruit_DHT.DHT11
pin = 23

rtc = RTC()
while True:

    Time = rtc.datetime()
    Temp = temperature = Adafruit_DHT.read_retry(sensor, pin)
    Humi = humidity = Adafruit_DHT.read_retry(sensor, pin)
    sleep(10)
    try:
        cur = conn.cursor()
        cur.execute(query, data)
        conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        print(f'Could not insert ! {e}')

    except KeyboardInterrupt:
        conn.close()