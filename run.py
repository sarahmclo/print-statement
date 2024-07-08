# Expect a terminal of 80 characters wide and 24 rows high
# Import dependencies
import gspread
from google.oauth2.service_account import Credentials
import sys
import os
import time

# Import colorama modules, adapted from tutorial:
# https://linuxhint.com/colorama-python/
import colorama
from colorama import Fore, Back, Style

# Initialise colorama
colorama.init(autoreset=True)

# Import tabulate to return sheet values in table format
from tabulate import tabulate

# IAM Configuration
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('print_statement')  # use spreadsheet name here

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
    print(Fore.MAGENTA + Style.BRIGHT + '''
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
    typingPrint("                      ** Welcome to Print Statement **\n",
                Fore.YELLOW + Style.BRIGHT)
    time.sleep(1)
    typingPrint("     A sales and inventory management system "
                "for Sarah's Screen Prints Inc.", Fore.WHITE)
    print("\n")
    time.sleep(4)
    clearScreen()

    print("\n")
    typingPrint(" Print Statement", Fore.MAGENTA + Style.BRIGHT)
    typingPrint(" is a comprehensive inventory management system.\n")
    time.sleep(1)
    typingPrint(" This program is for an artist's small "
                "screen-printing business.\n")
    time.sleep(1)
    typingPrint(" It enables users to monitor & update sales, "
                "stock, orders and materials data.\n")
    print("\n")
    time.sleep(2)
    typingPrint(" System loading, please wait...", Fore.YELLOW + Style.BRIGHT)
    time.sleep(3)
    clearScreen()


welcome()


def options():
    print("\n")
    print(Fore.GREEN + Style.BRIGHT + " Please choose from the menu below:\n")
    time.sleep(2)
    print("   1. Market Sales\n"
          "   2. Online Sales\n"
          "   3. Print Stock\n"
          "   4. Product Surplus\n"
          "   5. Materials\n"
          "   6. Exit Program\n")

    while True:
        data_str = input(Fore.GREEN + Style.BRIGHT +
                         " Enter a number to access data here and press enter: \n")
        if data_str in ['1', '2', '3', '4', '5', '6']:
            break
        else:
            print(Fore.RED + "Please choose a valid number")

    option = int(data_str)
    if option == 1:
        view_sales('Market Sales')
    elif option == 2:
         view_sales('Online Sales')
    elif option == 3:
        view_stock()
    elif option == 4:
        view_product_surplus()
    elif option == 5:
        view_materials()
    elif option == 6:
        exit_program()


def view_sales(sheet_name):
    """
    View sales data from specified sheet
    """
    sheet = SHEET.worksheet(sheet_name)
    sales_data = sheet.get_all_records()
    clearScreen()
    typingPrint(f"Viewing {sheet_name}...\n", Fore.YELLOW + Style.BRIGHT)
    time.sleep(1)
    # Convert data to list of lists for tabulate
    data_list = [list(record.values()) for record in sales_data]
    # Print data as a table
    print(tabulate(data_list, headers=sales_data[0].keys(), tablefmt='fancy_grid'))
    time.sleep(4)
    options()


def view_stock():
    """
    View stock data
    """
    sheet = SHEET.worksheet('Print Stock')
    stock_data = sheet.get_all_records()
    clearScreen()
    typingPrint(f"Viewing Print Stock...\n", Fore.YELLOW + Style.BRIGHT)
    time.sleep(1)
    data_list = [list(record.values()) for record in stock_data]
    print(tabulate(data_list, headers=stock_data[0].keys(), tablefmt='fancy_grid'))
    time.sleep(4)
    options()


def view_product_surplus():
    """
    View product surplus data
    """
    sheet = SHEET.worksheet('Product Surplus')
    surplus_data = sheet.get_all_records()
    clearScreen()
    typingPrint(f"Viewing Product Surplus...\n", Fore.YELLOW + Style.BRIGHT)
    time.sleep(1)
    data_list = [list(record.values()) for record in surplus_data]
    print(tabulate(data_list, headers=surplus_data[0].keys(), tablefmt='fancy_grid'))
    time.sleep(4)
    options()


def view_materials():
    """
    View materials data
    """
    sheet = SHEET.worksheet('Materials')
    materials_data = sheet.get_all_records()
    clearScreen()
    typingPrint(f"Viewing Materials...\n", Fore.MAGENTA + Style.BRIGHT)
    time.sleep(1)
    data_list = [list(record.values()) for record in materials_data]
    print(tabulate(data_list, headers=materials_data[0].keys(), tablefmt='fancy_grid'))
    time.sleep(4)
    options()


def exit_program():
    clearScreen()
    typingPrint("Exiting the program, thank you...\n", Fore.YELLOW + Style.BRIGHT)
    time.sleep(2)
    clearScreen()
    welcome()
    options()


options()
