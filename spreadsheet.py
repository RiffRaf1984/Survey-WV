import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/pi/Downloads/My Project-be73bbc80571.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open('surveys').sheet1

print(wks.get_all_records())
