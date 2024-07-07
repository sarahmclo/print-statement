# Expect a terminal of 80 characters wide and 24 rows high
# Import dependencies
import gspread
from google.oauth2.service_account import Credentials

# IAM Configuration
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('print_statement') # use spreadsheet name here

# Variables
sales = SHEET.worksheet('sales')

data = sales.get_all_values()

print(data)