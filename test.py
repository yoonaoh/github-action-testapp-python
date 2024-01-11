from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Testing out this python webapp - Yoona"
