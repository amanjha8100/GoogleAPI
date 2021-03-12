#from __future__ import print_function
#import os.path
from googleapiclient.discovery import build
#from google_auth_oauthlib.flow import InstalledAppFlow
#from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
#settings for json
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'
#Credentials to access ggogle sheets
creds=None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID  of a spreadsheet.
SAMPLE_SPREADSHEET_ID = '1eVb8a2xi_Xrf8OMP6UIoXFk5uEWB726eJJWDLal5ms0'

service = build('sheets', 'v4', credentials=creds)
SAMPLE_RANGE_NAME = "Sheet1!A1:D2"
# Call the Sheets API
sheet = service.spreadsheets()

#reading from google sheets python script
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range=SAMPLE_RANGE_NAME).execute()
values = result.get('values', [])


#writing to google sheets python script
aoa = [["amazon","2021","March","#"]]
request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="Sheet1!A2:D2",valueInputOption="USER_ENTERED", body={"values":aoa}).execute()
print(values)



    