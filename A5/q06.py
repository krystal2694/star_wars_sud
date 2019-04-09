# Krystal Wong
# A01089672
# Theoren Leveille
# A01070327
# 08/04/2019
import requests
import json


def website():
    """Create a simple HTML web page."""

    html_page = 'index.html'

    name = input('\nHello user, what is your name?').title().strip()
    description = input('\nHow would you describe yourself in a single sentence?')

    page_contents = """<!doctype html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <title>HTML using python</title>
    <meta name="description" content="User’s webpage">
    <meta name="author" content="Your name goes here">
   <link rel="stylesheet" href="css/theo_and_krystal.css">
    </head>
    <body id='bg'><h1 id='name'>""" + name + """</h1>
    """ + description + """
    <h2>Nasa photo of the day<h2>
    <img id='image' src=""" + get_nasa_image() + """ alt='image could not load'>
    </body>
    </html>"""

    with open(html_page, 'w') as file_object:
        file_object.write(page_contents)


def get_nasa_image():
    """Obtain the url of the nasa photo of the day using their API."""

    url = 'https://api.nasa.gov/planetary/apod?api_key=JyDMQqotVJTGjc5DbDUccg6LCVPq9ZRuEB5myO8G'

    response = requests.get(url)
    response.raise_for_status()

    string_of_json_data = json.loads(response.text)
    return string_of_json_data['url']


def main():
    website()


if __name__ == '__main__':
    main()
