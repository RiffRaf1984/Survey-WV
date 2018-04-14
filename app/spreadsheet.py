import gspread
from flask import redirect, session
from oauth2client.service_account import ServiceAccountCredentials
import bcrypt

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/pi/Downloads/My Project-be73bbc80571.json', scope)

gc = gspread.authorize(credentials)

workbook = gc.open('surveys')

surveys_sheet = workbook.worksheet('Surveys')

volunteers_sheet = workbook.worksheet('Volunteers')

def fetch_all_surveys():
    return surveys_sheet.get_all_records()

def insert_survey(cell_list):
    surveys_sheet.insert_row(cell_list, 2)

def email_exists(submitted_email):
    emails = volunteers_sheet.col_values(3)
    return submitted_email in emails
	
def hash_password(password):
	return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def insert_volunteer(f, l, em, ph, pw):
    volunteers_sheet.insert_row([f, l, em, ph, hash_password(pw)], 2)

def get_password_hash(email):
	row = volunteers_sheet.find(email).row
	column = 5
	password_hash = worksheet.cell(row, column).value
	return password_hash
  
def password_is_correct(email, password):
    encoded_password = password.encode()
    stored_hash = get_password_hash(email)
    return bcrypt.checkpw(encoded_password, stored_hash)

def load_user(email, password):
    # check if user is in database
    if email_exists(email):
        if password_is_correct(email, password):
            volunteer = volunteers.row_values(volunteers_sheet.find(email).row)
            session['volunteer'] = volunteer
            return redirect('/')
	#If password is incorrect, say so
	# If email is not found, say so
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
    #unittest.main()
    print(check_for_email('Stev'))
