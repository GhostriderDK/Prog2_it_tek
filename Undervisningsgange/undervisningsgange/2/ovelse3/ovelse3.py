import sqlite3
import Adafruit_DHT
import datetime
import time 


conn = sqlite3.connect('dht11.db')

query = 'INSERT INTO airdata (Datetime, Temperature, Humidity) VALUES(?,?,?)'


sensor = Adafruit_DHT.DHT11
pin = 23
while True:

    Time = datetime.now()
    Temp = temperature = Adafruit_DHT.read_retry(sensor, pin)
    Humi = humidity = Adafruit_DHT.read_retry(sensor, pin)
    data = (Time, Temp, Humi)
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