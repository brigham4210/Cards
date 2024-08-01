import json
from flask import Flask, render_template, request, session

app = Flask(__name__)


@app.route('/')
def index():
    with open("cards.json", "r") as file:
        data = json.load(file)
        keys = data.keys()
    return render_template('index.html', keys=keys)


@app.route('/<key>')
def cards(key):
    with open("cards.json", "r") as file:
        data = json.load(file)[key]
    return render_template('card.html', texts=data)


if __name__ == '__main__':
    app.run(debug=True)
