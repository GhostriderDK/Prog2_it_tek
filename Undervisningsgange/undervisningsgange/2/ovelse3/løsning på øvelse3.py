import Adafruit_DHT
import sqlite3
from datetime import datetime
from time import sleep

# SQL - Opret table hvis den ikke findes
query = """CREATE TABLE IF NOT EXISTS dht11(
        datetime TEXT NOT NULL,
        temperature REAL NOT NULL,
        humidity REAL NOT NULL
        );"""
try: # Forbind til database og opret table
    conn = sqlite3.connect("dht11_data.db")
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
except sqlite3.Error as e: # Vis fejlmeddelse hvis den fejler
    print(f"Error : {e}")
finally: # Lukker database forbindelse
    conn.close()
# SQL - indsæt data parametiseret 
query = """INSERT INTO dht11(
        datetime, temperature ,humidity) 
        VALUES (?, ?, ?);"""
# opret DHT11 objekt
sensor = Adafruit_DHT.DHT11
# GPIO 4 vælges
pin = 4

while True:
    # lav sensormåling og gem resultatet i de to variable3
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None: # hvis data er valid så indsæt i databasen
        print(f'Temp={temperature}*C  Humidity={humidity}%')
        values = (datetime.now(), temperature, humidity)
        try:
            conn = sqlite3.connect("dht11_data.db")
            cur = conn.cursor()
            cur.execute(query, values)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error : {e}")
        finally:
            conn.close()
    else:
        print('Failed to get reading. Try again!')
    sleep(10) # Vent 10 sekunder mellem hver gang data indsætte