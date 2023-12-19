from flask import Flask, request, render_template_string
from deck import deck

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string(open('index.html').read())

@app.route('/generate', methods=['POST'])
def generate_deck():
    file = request.form['file']
    t = request.form['type']
    front = request.form['front_color']
    back = request.form['back_color']
    height = float(request.form['height'])
    width = float(request.form['width'])

    # Generate deck of cards
    cards = deck(file, t, front, back, height, width)

    # Inject generated cards into HTML
    cards_html = ''
    for card in cards:
        cards_html += f'<div class="card" style="height: {height}rem; width: {width}rem; background-color: {front}; color: {back};">{card}</div>'

    # Load the template and inject generated cards
    html = open('index.html').read().replace('<!-- Generated cards will appear here -->', cards_html)
    return html

if __name__ == '__main__':
    app.run(debug=True)
