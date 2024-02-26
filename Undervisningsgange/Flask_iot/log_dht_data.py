import sqlite3
from datetime import datetime
from random import randint
from time import sleep

def log_stue_dht11():
    while True:
        query = """INSERT INTO stue (datetime, temperature, humidity) VALUES(?, ?, ?)"""
        data = (datetime.now(), randint(0, 30), randint(0, 100))

        try:
            conn = sqlite3.connect("database/sensor_data.db")
            cur = conn.cursor()
            cur.execute(query, data)
            conn.commit()
                        
        except sqlite3.Error as sql_e:
            print(f"sqlite error occurred: {sql_e}")
            conn.rollback()

        except Exception as e:
            print(f"Another error occured: {e}")
        finally:
            conn.close

        sleep(1)

log_stue_dht11()