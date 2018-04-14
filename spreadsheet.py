import gspread

from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/pi/Downloads/My Project-be73bbc80571.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open('surveys').sheet1

def fetch_all_surveys():
    return wks.get_all_records()

print(fetch_all_surveys())

def insert_survey(cell_list):
    wks.insert_row(cell_list, 2)

# -------------------------------------------------------------------------- #
# Testing

import unittest

#
columns = ['Event Name', 'Home Zipcode', 'Visit Accomodations', 'Nights Staying', 'Have Attended Festivall in the Past', 'Number of Events Expecting to Attend', 'Expected non-lodging Expenses', 'Age', 'Education', 'Income', 'Heard of Festival from', 'Favorite Part of Festivall', 'Seggestions for Festivall','Email']

#
test_column_values = ['TEST: Event Name', 'Home Zipcode', 'TEST: Visit Accomodations', 'TEST: Nights Staying', 'TEST: Have Attended Festivall in the Past', 'TEST: Number of Events Expecting to Attend', 'TEST: Expected non-lodging Expenses', 'TEST: Age', 'TEST: Education', 'TEST: Income', 'TEST: Heard of Festival from', 'TEST: Favorite Part of Festivall', 'TEST: Seggestions for Festivall', 'Email']

#
column_args = dict(zip(columns, test_column_values))

class TestSpreadsheet(unittest.TestCase):

    def test_insert(self):
        insert_survey(test_column_values)
        surveys = fetch_all_surveys()
        self.assertEqual(surveys[0]['Event Name'], 'TEST: Event Name')

if __name__ == '__main__':
    unittest.main()
