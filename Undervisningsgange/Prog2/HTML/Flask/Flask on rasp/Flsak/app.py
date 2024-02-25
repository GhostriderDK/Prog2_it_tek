from markupsafe import escape
from flask import Flask, abort, render_template
import base64
from io import BytesIO
from matplotlib.figure import Figure
import Adafruit_DHT
import sqlite3
from datetime import datetime
from time import sleep
app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def hello():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/comments/')
def comments():
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]

    return render_template('comments.html', comments=comments)



@app.route('/add/<int:n1>/<int:n2>/')
def add(n1, n2):
    return '<h1>{}</h1>'.format(n1 + n2)


@app.route('/users/<int:user_id>/')
def greet_user(user_id):
    users = ['Bob', 'Jane', 'Adam']
    try:
        return '<h2>Hi {}</h2>'.format(users[user_id])
    except IndexError:
        abort(404)

@app.route('/sensor_data')
def Sensor_data():

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