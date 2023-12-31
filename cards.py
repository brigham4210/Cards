import json


def read_json(key):
    with open("cards.json", "r") as file:
        data = json.load(file)
    return data[key]


def make_cards(key):
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
        justify-content: center; /* Center the content horizontally */
        align-items: center; /* Center the content vertically */
        page-break-after: always; /* Add a page break after each container */
    }
    .card {
        width: 2.5in; /* 4 columns with margin */
        height: 3.5in; /* Height of the card */
        margin-top: 0.25in;
        background-color: #FFFFF1;
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
<div class="container"></div>
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


# Call the function to generate and save the HTML
make_cards("sentences")
