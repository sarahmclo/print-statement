# Expect a terminal of 80 characters wide and 24 rows high
# Import dependencies
import gspread
from google.oauth2.service_account import Credentials

# Import colorama modules, adapted from tutorial: https://linuxhint.com/colorama-python/
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

import sys
import os
import time

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

# Functions
def clearScreen():
    """
    Clear CLI function
    """
    os.system("clear")

def typingPrint(text, color=Fore.WHITE):
    """
    Use typingPrint() in place of print() creates typing effect
    """
    for character in text:
        sys.stdout.write(color + character)
        sys.stdout.flush()
        time.sleep(0.05)

def welcome():
    """
    Display Print Statement Banner 
    """
    print(Fore.MAGENTA + r'''

  +----------------------------------------------------------------+
  |  ######                                                        |
  |  #     # #####  # #    # #####                                 |
  |  #     # #    # # ##   #   #                                   |
  |  ######  #    # # # #  #   #                                   |
  |  #       ####   # #  # #   #                                   |
  |  #       #   #  # #   ##   #                                   |
  |  #       #    # # #    #   #                                   |
  |   #####                                                        |
  |  #     # #####   ##   ##### ###### #    # ###### #    # #####  |
  |  #         #    #  #    #   #      ##  ## #      ##   #   #    |
  |   #####    #   #    #   #   #####  # ## # #####  # #  #   #    |
  |        #   #   ######   #   #      #    # #      #  # #   #    |
  |  #     #   #   #    #   #   #      #    # #      #   ##   #    |
  |   #####    #   #    #   #   ###### #    # ###### #    #   #    |
  +----------------------------------------------------------------+
''')
    time.sleep(1)
    """
    Display welcome screen text
    """
    typingPrint("                     Welcome to Print Statement\n",Fore.YELLOW                            )
    time.sleep(1)
    typingPrint(" A sales revenue and inventory management system for sarah_prints_inc.",Fore.WHITE)
    time.sleep(4.5)
    clearScreen()

    typingPrint(" PRINT STATEMENT is a comprehensive inventory management system.\n")
    time.sleep(1)
    typingPrint(" This program is for a small screen-printing business.\n")
    time.sleep(1)
    typingPrint(" It enables user to oversee sales, monitor stock, track materials and print-runs.\n")
    time.sleep(3)

    print("\n")

    print(Fore.CYAN + " Please choose a number from one of the following options:\n")
    
    print (" 1. View Sales\n"
    " 2. View Stock\n"
    " 3. View Materials\n"
    " 4. Update Sales\n"
    " 5. Update Stock\n"
    " 6. Update Materials\n")

welcome()