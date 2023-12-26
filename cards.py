import json


def read_json(key):
    with open("cards.json", "r") as file:
        data = json.load(file)

    return data[key]


def make_cards(sentence):
    content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Card</title>
    <style>
    body, html {{
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }}

    /* Basic styling for the card */
    .card {{
        width: 2.5in; /* Width of the card */
        height: 3.5in; /* Height of the card */
        margin: 0.5in;
        background-color: #FFFFF1;
        font-size: 20px;
        border: 0.1in solid #000000; /* Border for the card */
        padding: 0.1in; /* Padding inside the card */
        box-sizing: border-box; /* Includes padding and border in the total width and height */
        display: flex;
        align-items: center;
    }}
</style>
</head>
<body>

<div class="card">
    {sentence}
</div>

</body>
</html>

    """
