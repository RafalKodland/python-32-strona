from flask import Flask
from random import randint

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Witaj świecie! Test</p>"

@app.route("/test")
def test():
    return f"<p>To jest strona testowa. Liczba testowa: {randint(1, 10)}</p>"

app.run(debug=True)