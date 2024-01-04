import json


def read_json(key):
    with open("cards.json", "r") as file:
        data = json.load(file)
    return data[key]


def make_cards(key):
    try:
        content = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Card</title>
    <style>
    .container {
        display: flex;
        flex-wrap: wrap;
        margin: auto;
        font-size: 500px;
        border-width: 0.6in 0.3in; /* Top/Bottom 0.5in, Left/Right 0.2in */
        border-style: solid;
        border-color: #00FF00;        justify-content: center; /* Center the content horizontally */
        width: 10in; /* Optional: Adjust maximum width of the container */
        height: 7in; /* Optional: Adjust maximum height of the container */
        page-break-after: always; /* Add a page break after each container */
}

    .card {
        width: 2.5in; /* 4 columns with margin */
        height: 3.5in; /* Height of the card */
        margin: auto;
        background-color: #FFFFFF;
        font-size: 20px;
        border: 0.1in solid #000000; /* Border for the card */
        padding: 0.1in; /* Padding inside the card */
        box-sizing: border-box; /* Includes padding and border in the total width and height */
        display: flex;
        align-items: center;
    }
    </style>
</head>
<body>
<div class="container">OFF</div>
"""

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
