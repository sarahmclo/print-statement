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

def typeInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

def welcome():
    """
    Display Print Statement Banner 
    """
    print(Fore.MAGENTA + Style.BRIGHT + r'''
       $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
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
       |        #   #   ######   #   #      #  # # #      #  # #   #    |
       |  #     #   #   #    #   #   #      #    # #      #   ##   #    |
       |   #####    #   #    #   #   ###### #    # ###### #    #   #    |
       +----------------------------------------------------------------+
       $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
''')
    time.sleep(1)
    """
    Display welcome screen text
    """
    typingPrint("                      ** Welcome to Print Statement **\n",Fore.YELLOW + Style.BRIGHT                          )
    time.sleep(1)
    typingPrint("     A sales and inventory management system for Sarah's Screen Prints Inc.",Fore.WHITE)
    print("\n")
    time.sleep(4.5)
    clearScreen()

    print("\n")
    typingPrint(" Print Statement",Fore.YELLOW + Style.BRIGHT )
    typingPrint(" is a comprehensive inventory management system.\n")
    time.sleep(1)
    typingPrint(" This program is for an artist's small screen-printing business.\n")
    time.sleep(1)
    typingPrint(" It enables users to monitor sales, stock, orders and materials.\n")
    time.sleep(3)

welcome()

def options():

    print("\n")

    print(Fore.YELLOW + Style.BRIGHT + " Please choose from the menu below:\n")
    time.sleep(2)
    print ("   1. Market Sales\n"
    "   2. Online Sales\n"
    "   3. Print Stock\n"
    "   4. Product Surplus\n"
    "   5. Materials\n"
    "   6. Exit Program\n")

    while True:
        data_str = input(Fore.YELLOW + Style.BRIGHT + " Enter a number to access data here: \n")

    """
    while True:
        try:
            option = int(typeInput(" Choose a number to access corresponding data:\n"))
            if option == 1:
                view_sales()
                break
            elif option == 2:
                view_stock()
                break
            elif option == 3:
                view_materials()
                break
            elif option == 4:
                update_sales()
                break
            elif option == 5:
                update_stock()
                break
            elif option == 6:
                update_materials()
                break
        except ValueError:
            print(Fore.RED + "Please choose a valid number")
    """
options()