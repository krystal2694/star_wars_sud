from unittest import TestCase
from q06 import website, get_nasa_image
import os
from unittest.mock import patch, mock_open


class TestWebsite(TestCase):
    @patch('builtins.input', side_effect=['theoren', 'a guy in CST'])
    def test_website_file_exists(self, mock_input):
        website()
        self.assertTrue(os.path.exists('../A5/index.html'))

    @patch('builtins.input', side_effect=['theoren', 'a guy in CST'])
    def test_website_file_writes(self, mock_input):
        with patch('builtins.open', mock_open(read_data="")) as mock_file:
            page_contents = """<!doctype html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <title>HTML using python</title>
    <meta name="description" content="User’s webpage">
    <meta name="author" content="Your name goes here">
   <link rel="stylesheet" href="css/theo_and_krystal.css">
    </head>
    <body id='bg'><h1 id='name'>Theoren</h1>
    a guy in CST
    <h2>Nasa photo of the day<h2>
    <img id='image' src=""" + get_nasa_image() + """ alt='image could not load'>
    </body>
    </html>"""
            website()
            mock_file().write.assert_called_once_with(page_contents)

    @patch('builtins.input', side_effect=['theoren', 'a guy in CST'])
    def test_website_contents_reflects_user_input_name(self, mock_input):
        website()
        with open("index.html") as file_object:
            contents = file_object.read()
        self.assertIn('Theoren', contents)

    @patch('builtins.input', side_effect=['theoren', 'a guy in CST'])
    def test_website_contents_reflects_user_input_description(self, mock_input):
        website()
        with open("index.html") as file_object:
            contents = file_object.read()

        self.assertIn('a guy in CST', contents)

    @patch('builtins.input', side_effect=['theoren', 'a guy in CST'])
    def test_website_contents_reflects_url(self, mock_input):
        website()
        image_url = get_nasa_image()

        with open("index.html") as file_object:
            contents = file_object.read()

        self.assertIn(image_url, contents)


class TestGetNasaImage(TestCase):
    def test_get_nasa_image_return_type(self):
        self.assertIsInstance(get_nasa_image(), str)
