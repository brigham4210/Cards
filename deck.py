import json


# Read the data from the JSON file
def deck(json_file, t, front_color, back_color, height, width):
    q = int((8.27 // (height + 0.35)) * (11.69 // (width * 1.05)))

    with open(json_file, 'r') as file:
        data = json.load(file)
        cards = data[t]

    # HTML structures for the cards of cards (3.5"x2.5") with rounded corners
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{t}</title>
        <style>
            body {{
                display: flex;
                justify-content: center;
                align-items: center;
                margin-top: 0px;
            }}
            .page {{
                margin-top: 0in;
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                align-items: center;
            }}
            .card {{
                outline: 5px solid black;
                outline-offset: 0px;            
                width: {width}in; /* Card width */
                height: {height}in; /* Card height */
                margin-right: 0.1in;
                margin-left: 0.1in;
                margin-top: 0.25in;
                margin-bottom: 0.1in;
                text-align: left;
                background-color: {front_color};
                border-radius: 20px; /* Rounded corners */
                font-size: 150%; /* Adjust font size as needed */
                display: flex;
                justify-content: center;
                align-items: center;
                box-sizing: border-box; /* Include padding and border in the element's total width and height */
                padding: 30px;
            }}
            .back {{
                outline: 5px solid black;
                outline-offset: 0px;            
                width: {width}in; /* Card width */
                height: {height}in; /* Card height */
                margin-right: 0.1in;
                margin-left: 0.1in;
                margin-top: 0.25in;
                margin-bottom: 0.1in;
                text-align: left;
                background-color: {back_color};
                border-radius: 20px; /* Rounded corners */
                font-size: 150%; /* Adjust font size as needed */
                display: flex;
                justify-content: center;
                align-items: center;
                box-sizing: border-box; /* Include padding and border in the element's total width and height */
                padding: 30px;
            }}
            .text {{
                width: 100%;
                height: 100%;
                display: flex;
                justify-content: center;
                align-items: center;
            }}
            .container-break {{
                page-break-after: always; /* Page break after each container */
            }}
        </style>
    </head>
    <body>
    <div class="page">
    """

    # Counter for cards
    card_count = 0

    # Iterate through each sentence and create a card for it
    for sentence in cards:
        # Add card content
        html_content += f"""
        <div class="card"><div class="text">{sentence}</div></div>
        """
        # Increment card count
        card_count += 1

        # Check if it's time to break the page
        if card_count % q == 0:
            html_content += f"""
        <div class="container-break"></div>
            """
            for i in range(0, q):
                html_content += f"""
        <div class="back"><div class="text">{t}</div></div>
                """
            html_content += f"""
        <div class="container-break"></div>
            """

    # Closing tags for HTML content
    html_content += """
    </div>
    </body>
    </html>
    """

    # Write the generated HTML content to a file
    with open(f'{t}.html', 'w') as html_file:
        html_file.write(html_content)

    print(f"HTML content generated and saved to '{t}.html'")

    return html_content
