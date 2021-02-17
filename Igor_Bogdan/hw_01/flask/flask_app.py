from flask import Flask
from flask import render_template


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def hello_world():
    return render_template("1.html")
