import base64
from io import BytesIO
from flask import Flask
from matplotlib.figure import Figure

app = Flask(__name__)
@app.route("/")
def hello():

    fig = Figure()
    ax= fig.subplots()
    y = [1, 8, 1, 7]
    x = [1, 6, 9, 12]
    ax.set_facecolor("#000") # inner plot background color HTML black
    fig.patch.set_facecolor('#000') # outer plot background color HTML black
    ax.plot(x, y, linestyle = 'dashed', c = '#11f', linewidth = '1.5',
        marker = 'o', mec = 'hotpink', ms = 10, mfc = 'hotpink' )
    ax.set_xlabel('X-axis ')
    ax.set_ylabel('Y-axis ')
    ax.xaxis.label.set_color('hotpink') #setting up X-axis label color to hotpink
    ax.yaxis.label.set_color('hotpink') #setting up Y-axis label color to hotpink
    ax.tick_params(axis='x', colors='white') #setting up X-axis tick color to white
    ax.tick_params(axis='y', colors='white') #setting up Y-axis tick color to white
    ax.spines['left'].set_color('blue') # setting up Y-axis tick color to blue
    ax.spines['top'].set_color('blue') #setting up above X-axis tick color to blue
    ax.spines['bottom'].set_color('blue') #setting up above X-axis tick color to blue
    ax.spines['right'].set_color('blue') #setting up above X-axis tick color to 

    buf = BytesIO()
    fig.savefig(buf, format="png")

    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"
if __name__ == "__main__":
    app.run()
