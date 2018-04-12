import gspread

from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/pi/Downloads/My Project-be73bbc80571.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open('surveys').sheet1

def fetch_all_serveys():
    return wks.get_all_records()

def insert_survey(**kwargs):
    pass

# -------------------------------------------------------------------------- #
# Testing

import unittest

columns = ['Event Name', 'Home Zipcode', 'Visit Accomodations', 'Nights Staying', 'Have Attended Festivall in the Past', 'Number of Events Expecting to Attend', 'Expected non-lodging Expenses', 'Age', 'Education', 'Income', 'Heard of Festival from', 'Favorite Part of Festivall', 'Seggestions for Festivall','Email']

test_column_values = ['TEST: Event Name', 'Home Zipcode', 'TEST: Visit Accomodations', 'TEST: Nights Staying', 'TEST: Have Attended Festivall in the Past', 'TEST: Number of Events Expecting to Attend', 'TEST: Expected non-lodging Expenses', 'TEST: Age', 'TEST: Education', 'TEST: Income', 'TEST: Heard of Festival from', 'TEST: Favorite Part of Festivall', 'TEST: Seggestions for Festivall', 'Email']

column_args = zip(columns, test_column_values)

class TestSpreadsheet(unittest.TestCase):

    def test_insert(self):
        insert_survey(**Column_args)
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
