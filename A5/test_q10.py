from unittest import TestCase
from q10 import database_shared_headings


superheroes = {'Captain America':
               {'name': 'Steve Rogers',
                'superpower': 'super strength',
                'born': 1918,
                'member of Avengers': True},
               'Iron Man':
               {'name': 'Tony Stark',
                'superpower': 'intelligence',
                'born': 1970,
                'member of Avengers': True,
                'significant other': 'Pepper Potts'},
               'Aquaman':
               {'name': 'Arthur Curry',
                'superpower': 'breath underwater',
                'born': 1986}}

items = {'Pencil':
               {'brand': 'H2',
                'type': 'classic',
                'eraser': True},
               'Strawberry':
               {'color': 'red',
                'weight': '4lbs',
                'date picked': 2019},
               'Phone':
               {'model': 'iPhone',
                'service provider': 'virgin',
                'owner': 'me'}}


class TestDatabaseSharedHeadings(TestCase):
    def test_database_shared_headings_return_type(self):
        self.assertIsInstance(database_shared_headings(superheroes), set)

    def test_database_shared_headings_correct_values_in_set(self):
        self.assertEqual(database_shared_headings(superheroes), {'name', 'superpower', 'born'})

    def test_database_shared_headings_no_shared_headings(self):
        self.assertEqual(database_shared_headings(items), set())

