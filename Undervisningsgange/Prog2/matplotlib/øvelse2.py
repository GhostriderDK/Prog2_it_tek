import base64
from io import BytesIO
from flask import Flask
from matplotlib.figure import Figure
import Adafruit_DHT
import sqlite3
from datetime import datetime
from time import sleep

app = Flask(__name__)
@app.route("/")

def database_collect():
    query = """SELECT * FROM dht11 LIMIT 20;"""
    try:
        conn = sqlite3.connect("dht11.db")
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        result = cur.execute(query)
        rows = result.fetchall()
        for row in rows:   
        print(f"""\ttimestamp: {row["datetime"]}\n
        temperature: {row["temperature"]}\n
        humidity: {row["humidity"]}\n""")
        

    except sqlite3.Error as e: 
        print(f"Error : {e}")
    
    finally:
        conn.close()

def hello():

    fig = Figure()
    time_temp= fig.subplots()
    temp = {row["temperature"]}
    time = {row["datetime"]}
    time_temp.set_facecolor("#000") # inner plot background color HTML black
    fig.patch.set_facecolor('#000') # outer plot background color HTML black
    time_temp.plot(time, temp, linestyle = 'dashed', c = '#11f', linewidth = '1.5',
        marker = 'o', mec = 'hotpink', ms = 10, mfc = 'hotpink' )
    time_temp.set_xlabel('X-axis ')
    time_temp.set_ylabel('Y-axis ')
    time_temp.xaxis.label.set_color('hotpink') #setting up X-axis label color to hotpink
    time_temp.yaxis.label.set_color('hotpink') #setting up Y-axis label color to hotpink
    time_temp.tick_params(axis='x', colors='white') #setting up X-axis tick color to white
    time_temp.tick_params(axis='y', colors='white') #setting up Y-axis tick color to white
    time_temp.spines['left'].set_color('blue') # setting up Y-axis tick color to blue
    time_temp.spines['top'].set_color('blue') #setting up above X-axis tick color to blue
    time_temp.spines['bottom'].set_color('blue') #setting up above X-axis tick color to blue
    time_temp.spines['right'].set_color('blue') #setting up above X-axis tick color to 

    buf = BytesIO()
    fig.savefig(buf, format="png")

    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"

if __name__ == "__main__":
    app.run()
