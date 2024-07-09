# Import libraries and dependencies
import gspread
from google.oauth2.service_account import Credentials
import sys
import os
import time
from tabulate import tabulate

# Import colorama modules, adapted from tutorial:
# https://linuxhint.com/colorama-python/
import colorama
from colorama import Fore, Style

# Initialise colorama
colorama.init(autoreset=True)

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
                "for Sarah's Screen Prints Inc.", Fore.WHITE + Style.BRIGHT)
    print("\n")
    time.sleep(1)
    typingPrint("     loading...", Fore.MAGENTA + Style.BRIGHT)
    time.sleep(3)
    clearScreen()

    print("\n")
    typingPrint(" Print Statement", Fore.MAGENTA + Style.BRIGHT)
    typingPrint(" is a comprehensive sales and inventory management system.\n")
    time.sleep(1)
    typingPrint(" This program is for an artist's small "
                "screen printing business.\n")
    time.sleep(1)
    typingPrint(" It enables users to monitor & update sales, "
                "print stock & materials.\n")
    print("\n")
    time.sleep(2)
    typingPrint(" System loading, please wait...", Fore.YELLOW + Style.BRIGHT)
    time.sleep(3)
    clearScreen()


welcome()


def options():
    print("\n")
    print(Fore.GREEN + Style.BRIGHT + " Main Menu:\n")
    time.sleep(2)
    print("   1. Market Sales\n"
          "   2. Online Sales\n"
          "   3. Print Stock\n"
          "   4. Product Surplus\n"
          "   5. Materials\n"
          "   6. Exit Program\n")

    while True:
        data_str = input(Fore.GREEN + Style.BRIGHT +
                         " Enter a number to view/update data:" + Fore.WHITE + " ")
        if data_str in ['1', '2', '3', '4', '5', '6']:
            break
        else:
            print(Fore.RED + " Please choose a valid number")

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


def view_sales(sheet_name): # Sales Function
    """
    View sales data from specified sheet
    """
    while True:
        sheet = SHEET.worksheet(sheet_name)
        sales_data = sheet.get_all_records()
        clearScreen()
        print("\n")
        typingPrint(f" Viewing {sheet_name}...\n", Fore.YELLOW + Style.BRIGHT)
        print("\n")
        time.sleep(1)
        # Convert data to list of lists for tabulate
        data_list = [list(record.values()) for record in sales_data]
        # Print data as a table
        print(tabulate(data_list, headers=sales_data[0].keys(),
              tablefmt='fancy_grid'))
        print("\n")
        while True:
            update_option = input(Fore.GREEN + Style.BRIGHT + " Update Data Y or N: " + Fore.WHITE + Style.BRIGHT).strip().upper()
            if update_option in ['Y', 'N']:
                break
            else:
                print(Fore.RED + Style.BRIGHT + " Invalid input. Please enter Y or N.")

        if update_option.upper() == 'Y':
            # LOGIC - UPDATE LATER
            print("\n")
            print(Fore.YELLOW + " Updating data...")
            time.sleep(2)
            print(Fore.GREEN + Style.BRIGHT + " Data updated successfully.")
            time.sleep(2)
            print("\n")
        
        while True:
            return_option = input(Fore.GREEN + Style.BRIGHT +
                                  " Return to Menu Y or N: " + Fore.WHITE +
                              Style.BRIGHT).strip().upper()
            if return_option == 'Y':
                clearScreen()
                options()
                return
            elif return_option == 'N':
                exit_option = input(Fore.MAGENTA + Style.BRIGHT +
                                    " Exit Program Y or N: " + Fore.WHITE +
                              Style.BRIGHT).strip().upper()
                if exit_option == 'Y':
                    exit_program()
                    return
                elif exit_option == 'N':
                    print("\n")
                    print(Fore.YELLOW + Style.BRIGHT + " Returning to main menu...")
                    time.sleep(2)
                    clearScreen()
                    options()
                    return
                else:
                    print(Fore.RED + Style.BRIGHT + "Invalid input. Please enter correctly")
            else:
                print(Fore.RED + Style.BRIGHT + " Invalid input. Please enter correctly")
        break


def view_stock(): # Stock Function
    """
    View stock data
    """
    while True:
        sheet = SHEET.worksheet('Print Stock')
        stock_data = sheet.get_all_records()
        clearScreen()
        typingPrint(f" Viewing Print Stock...\n", Fore.CYAN + Style.BRIGHT)
        print("\n")
        time.sleep(1)
        data_list = [list(record.values()) for record in stock_data]
        print(tabulate(data_list, headers=stock_data[0].keys(),
              tablefmt='fancy_grid'))
        print("\n")

        update_option = input(Fore.GREEN + Style.BRIGHT + " Update Data Y/N:"
                              + Fore.WHITE + Style.BRIGHT + " ")

        if update_option.upper() == 'Y':
            # LOGIC - UPDATE LATER
            print("\n")
            print(Fore.YELLOW + " Updating data...")
            time.sleep(2)
            print(Fore.GREEN + Style.BRIGHT + " Data updated successfully.")
            time.sleep(2)
            print("\n")
        
        while True:
            return_option = input(Fore.GREEN + Style.BRIGHT +
                                  " Return to Menu Y or N: " + Fore.WHITE +
                              Style.BRIGHT).strip().upper()
            if return_option == 'Y':
                clearScreen()
                options()
                return
            elif return_option == 'N':
                exit_option = input(Fore.MAGENTA + Style.BRIGHT +
                                    " Exit Program Y or N: " + Fore.WHITE +
                              Style.BRIGHT).strip().upper()
                if exit_option == 'Y':
                    exit_program()
                    return
                elif exit_option == 'N':
                    print("\n")
                    print(Fore.YELLOW + Style.BRIGHT + " Returning to main menu...")
                    time.sleep(2)
                    clearScreen()
                    options()
                    return
                else:
                    print(Fore.RED + Style.BRIGHT + "Invalid input. Please enter correctly")
            else:
                print(Fore.RED + Style.BRIGHT + " Invalid input. Please enter correctly")
        break


def view_product_surplus(): # Surplus Function
    """
    View product surplus data
    """
    while True:
        sheet = SHEET.worksheet('Product Surplus')
        surplus_data = sheet.get_all_records()
        clearScreen()
        typingPrint(f" Viewing Product Surplus...\n", Fore.CYAN + Style.BRIGHT)
        print("\n")
        time.sleep(1)
        data_list = [list(record.values()) for record in surplus_data]
        print(tabulate(data_list, headers=surplus_data[0].keys(),
              tablefmt='fancy_grid'))
        print("\n")

        update_option = input(Fore.GREEN + Style.BRIGHT +
                              " Update Data Y/N:" + Fore.WHITE
                              + Style.BRIGHT + " ")

        if update_option.upper() == 'Y':
            # LOGIC - UPDATE LATER
            print("\n")
            print(Fore.YELLOW + " Updating data...")
            time.sleep(2)
            print(Fore.GREEN + Style.BRIGHT + " Data updated successfully.")
            time.sleep(2)
            print("\n")
        
        while True:
            return_option = input(Fore.GREEN + Style.BRIGHT +
                                  " Return to Menu Y or N: " + Fore.WHITE +
                              Style.BRIGHT).strip().upper()
            if return_option == 'Y':
                clearScreen()
                options()
                return
            elif return_option == 'N':
                exit_option = input(Fore.MAGENTA + Style.BRIGHT +
                                    " Exit Program Y or N: " + Fore.WHITE +
                              Style.BRIGHT).strip().upper()
                if exit_option == 'Y':
                    exit_program()
                    return
                elif exit_option == 'N':
                    print("\n")
                    print(Fore.YELLOW + Style.BRIGHT + " Returning to main menu...")
                    time.sleep(2)
                    clearScreen()
                    options()
                    return
                else:
                    print(Fore.RED + Style.BRIGHT + "Invalid input. Please enter correctly")
            else:
                print(Fore.RED + Style.BRIGHT + " Invalid input. Please enter correctly")
        break


def view_materials(): # Materials Function
    """
    View materials data
    """
    while True:
        sheet = SHEET.worksheet('Materials')
        materials_data = sheet.get_all_records()
        clearScreen()
        typingPrint(f" Viewing Materials...\n", Fore.MAGENTA + Style.BRIGHT)
        print("\n")
        time.sleep(1)
        data_list = [list(record.values()) for record in materials_data]
        print(tabulate(data_list, headers=materials_data[0].keys(),
              tablefmt='fancy_grid'))
        print("\n")

        update_option = input(Fore.GREEN + Style.BRIGHT +
                              " Update Data Y/N:" + Fore.WHITE +
                              Style.BRIGHT + " ")

        if update_option.upper() == 'Y':
            # LOGIC - UPDATE LATER
            print("\n")
            print(Fore.YELLOW + " Updating data...")
            time.sleep(2)
            print(Fore.GREEN + Style.BRIGHT + " Data updated successfully.")
            time.sleep(2)
            print("\n")
        
        while True:
            return_option = input(Fore.GREEN + Style.BRIGHT +
                                  " Return to Menu Y or N: " + Fore.WHITE +
                              Style.BRIGHT).strip().upper()
            if return_option == 'Y':
                clearScreen()
                options()
                return
            elif return_option == 'N':
                exit_option = input(Fore.MAGENTA + Style.BRIGHT +
                                    " Exit Program Y or N: " + Fore.WHITE +
                              Style.BRIGHT).strip().upper()
                if exit_option == 'Y':
                    exit_program()
                    return
                elif exit_option == 'N':
                    print("\n")
                    print(Fore.YELLOW + Style.BRIGHT + " Returning to main menu...")
                    time.sleep(2)
                    clearScreen()
                    options()
                    return
                else:
                    print(Fore.RED + Style.BRIGHT + "Invalid input. Please enter correctly")
            else:
                print(Fore.RED + Style.BRIGHT + " Invalid input. Please enter correctly")
        break


def exit_program():
    clearScreen()
    typingPrint(Fore.YELLOW + Style.BRIGHT + " Exiting the program, thank you for using Print Statement.")
    time.sleep(3)
    clearScreen()
    welcome()
    options()


options()
