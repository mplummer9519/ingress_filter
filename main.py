from flask import Flask


app = Flask(__name__)

@app.rout("/hit_rate")
def index():
    print("Congrats its a web app")

