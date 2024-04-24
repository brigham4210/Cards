import json


def read_json(key):
    with open("cards.json", "r") as file:
        data = json.load(file)
    return data[key]


def make_cards(key):
    try:

        sentences = read_json(key)
        content += '<div class="container">'  # Open the container div
        for i, sentence in enumerate(sentences, start=1):
            content += f"""
<div class="card">
    {sentence}
</div>
"""
        # Insert a new container after 8 cards (2 rows * 4 columns)
            if i % 8 == 0:
                content += '</div><div class="container">'  # Close and open a new container

        content += '</div>'  # Close the final container

        content += """
</body>
</html>
"""

        with open("cards.html", "w") as html_file:
            html_file.write(content)
            print("Successfully generated 'cards.html'")

    except Exception as e:
        print(f"Warning: {e}")


# Call the function to generate and save the HTML
make_cards("sentences")
