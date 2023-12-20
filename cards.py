from flask import Flask, request, render_template_string
from deck import deck

app = Flask(__name__)


@app.route('/')
def index():
    return render_template_string(open('deck.html').read())


@app.route('/generate', methods=['POST'])
def generate_deck():
    file = request.form['file']
    t = request.form['type']
    front = str(request.form['front_color'])
    back = str(request.form['back_color'])
    height = float(request.form['height'])
    width = float(request.form['width'])

    return deck(file, t, front, back, height, width)


if __name__ == '__main__':
    app.run(debug=True)
