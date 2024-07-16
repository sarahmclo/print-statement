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
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("print_statement")  # use spreadsheet name here

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
    print(
        Fore.MAGENTA
        + Style.BRIGHT
        + """
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
"""
    )
    time.sleep(1)
    """
    Display welcome screen text
    """
    typingPrint(
        "                      ** Welcome to Print Statement **\n",
        Fore.YELLOW + Style.BRIGHT,
    )
    time.sleep(1)
    typingPrint(
        "     A sales and inventory management system "
        "for Sarah's Screen Prints Inc.",
        Fore.WHITE + Style.BRIGHT,
    )
    print("\n")
    time.sleep(1)
    typingPrint("     loading...\n", Fore.MAGENTA + Style.BRIGHT)
    time.sleep(3)
    clearScreen()

    print("\n")
    typingPrint(" Print Statement", Fore.MAGENTA + Style.BRIGHT)
    typingPrint(" is a comprehensive sales and inventory management system.\n")
    time.sleep(1)
    typingPrint(" This program is for an artist's small "
                "screen-printing business.\n")
    time.sleep(1)
    typingPrint(
        " It enables users to monitor & update print sales, "
        "stock & materials.\n"
    )
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
    print(
        "   1. Market Sales\n"
        "   2. Print Stock\n"
        "   3. Materials\n"
        "   4. Exit Program\n"
    )

    while True:
        data_str = input(
            Fore.GREEN
            + Style.BRIGHT
            + " Enter a number to view/update data:"
            + Fore.WHITE
            + Style.BRIGHT
            + " "
        )
        if data_str in ["1", "2", "3", "4"]:
            break
        else:
            print(Fore.RED + Style.BRIGHT + " Please choose a valid number")

    option = int(data_str)
    if option == 1:
        view_sales("Market Sales")
    elif option == 2:
        view_stock()
    elif option == 3:
        view_materials()
    elif option == 4:
        exit_program()


def view_sales(sheet_name):  # Sales Function
    """
    View sales data from specified sheet
    """
    while True:
        sheet = SHEET.worksheet(sheet_name)
        sales_data = sheet.get_all_records()
        headers = sheet.row_values(1)

        clearScreen()
        print("\n")
        typingPrint(f" Viewing {sheet_name}...\n", Fore.YELLOW + Style.BRIGHT)
        print("\n")
        time.sleep(1)

        # Print data as a table
        display_table(sales_data, headers)
        print("\n")
        while True:
            update_option = (
                input(
                    Fore.GREEN
                    + Style.BRIGHT
                    + " Update Data Y or N: "
                    + Fore.WHITE
                    + Style.BRIGHT
                )
                .strip()
                .upper()
            )
            if update_option.upper() == "Y":
                update_data(sheet, headers)
                break
            elif update_option == "N":
                break
            else:
                print(
                    Fore.RED + Style.BRIGHT +
                    " Invalid input. Please enter 'Y' or 'N'"
                )

        while True:
            return_option = (
                input(
                    Fore.GREEN
                    + Style.BRIGHT
                    + " Return to Menu Y/N: "
                    + Fore.WHITE
                    + Style.BRIGHT
                )
                .strip()
                .upper()
            )
            if return_option == "Y":
                clearScreen()
                options()
                return
            elif return_option == "N":
                while True:
                    exit_option = (
                        input(
                            Fore.MAGENTA
                            + Style.BRIGHT
                            + " Exit Program Y/N: "
                            + Fore.WHITE
                            + Style.BRIGHT
                        )
                        .strip()
                        .upper()
                    )
                    if exit_option == "Y":
                        exit_program()
                        return
                    elif exit_option == "N":
                        print("\n")
                        print(Fore.YELLOW + Style.BRIGHT +
                              " Returning to main menu...")
                        time.sleep(2)
                        clearScreen()
                        options()
                        return
                    else:
                        print(
                            Fore.RED
                            + Style.BRIGHT
                            + " Invalid input. Please enter correctly."
                        )
            else:
                print(
                    Fore.RED + Style.BRIGHT +
                    " Invalid input. Please enter correctly."
                )


def update_data(sheet, headers):
    """
    Function to allow for user to update data in sheets.
    """
    # Display current data
    print("\n")
    data = sheet.get_all_records()
    if not data:
        print("No data available to update.")
        return

    while True:
        # Prompt user for print number and day to input data to specific cell
        day = (
            input(
                Fore.YELLOW
                + Style.BRIGHT
                + f" Enter day (Mon, Tues, Wed, Thurs, Fri): "
                + Fore.WHITE
                + Style.BRIGHT
            )
            .strip()
            .capitalize()
        )
        if day not in ["Mon", "Tues", "Wed", "Thurs", "Fri"]:
            print(Fore.RED + Style.BRIGHT +
                  " Invalid input. Please enter correctly.")
            continue

        print_number = input(
            Fore.YELLOW
            + Style.BRIGHT
            + f" Enter print #: (1, 2, 3): "
            + Fore.WHITE
            + Style.BRIGHT
        )
        if print_number not in ["1", "2", "3"]:
            print(Fore.RED + Style.BRIGHT +
                  " Invalid input Please enter correctly.")
            continue

        # Find column index for print and day
        column_index = None
        for i, header in enumerate(headers, start=1):
            if header.startswith(f"print #{print_number}"):
                column_index = i
                break
        if column_index is None:
            print(Fore.RED + Style.BRIGHT +
                  f"Invalid input for #{print_number}.")
            continue

        row_index = None
        for i, record in enumerate(data, start=1):
            if record["Market Sales"] == day:
                row_index = i + 1  # Do not allow for header update
                break
        if row_index is None:
            print(Fore.RED + Style.BRIGHT + f"Invalid input for {day}.")
            continue

        # Input new value
        new_value = input(
            Fore.MAGENTA
            + Style.BRIGHT
            + f" Update data by entering new value for {headers[column_index-1]} on {day}: "
            + Fore.WHITE
            + Style.BRIGHT
        )
        if not new_value.replace(".", "", 1).isdigit():
            print(Fore.RED + Style.BRIGHT +
                  "Invalid input. Please enter correctly.")
            continue

        # Update cell
        cell_to_update = sheet.cell(row_index, column_index)
        try:
            cell_to_update.value = float(new_value)
            sheet.update_cells([cell_to_update])
            print("\n")
            time.sleep(1)
            typingPrint(" Data updated successfully!\n",
                        Fore.GREEN + Style.BRIGHT)
            print("\n")
            time.sleep(1)
            typingPrint(
                " Reloading updated Market Sales...\n",
                Fore.YELLOW + Style.BRIGHT
            )
            time.sleep(3)
            # Reload Market Sales
            view_sales("Market Sales")
            break
        except Exception as e:
            print(f" Error updating data: {e}")


def get_valid_row_index(data):
    while True:
        try:
            row_index = input(
                Fore.YELLOW
                + Style.BRIGHT
                + f" Enter row you want to update (2 to {len(data)+1}): "
                + Fore.WHITE
            )
            if row_index.isdigit() and 2 <= int(row_index) <= len(data) + 1:
                return int(row_index)
            else:
                print(
                    Fore.RED
                    + Style.BRIGHT
                    + f" Invalid row. Please enter a"
                    " number between 2 and {len(data)+1}."
                )
        except ValueError:
            print(
                Fore.RED + Style.BRIGHT +
                " Invalid input. Please enter a valid number."
            )


def get_valid_column_index(headers):
    while True:
        try:
            print("\n")
            print(Fore.GREEN + Style.BRIGHT + " Columns for update: ")
            for i, header in enumerate(headers, start=1):
                print(f" {i}. {header}")
            column_index = int(
                input(
                    Fore.YELLOW
                    + Style.BRIGHT
                    + f" Enter column you want"
                    " to update (1 to {len(headers)}): "
                )
            )
            if 1 <= column_index <= len(headers):
                return column_index
            else:
                print(
                    Fore.RED
                    + Style.BRIGHT
                    + f" Invalid column. Please enter"
                    " a number between 1 and {len(headers)}."
                )
        except ValueError:
            print(
                Fore.RED + Style.BRIGHT +
                " Invalid input. Please enter a valid number."
            )


def display_table(data, headers):
    if not data:
        print("No data available.")
        return
    data_list = [list(record.values()) for record in data]
    print(tabulate(data_list, headers=headers, tablefmt="fancy_grid"))


def view_stock():  # Stock Function
    """
    View stock data
    """
    while True:
        sheet = SHEET.worksheet("Print Stock")
        stock_data = sheet.get_all_records()
        headers = sheet.row_values(1)

        clearScreen()
        print("\n")
        typingPrint(" Viewing Print Stock...\n", Fore.CYAN + Style.BRIGHT)
        print("\n")
        time.sleep(1)

        display_table(stock_data, headers)
        print("\n")

        while True:
            update_option = (
                input(
                    Fore.GREEN
                    + Style.BRIGHT
                    + " Update Data Y/N: "
                    + Fore.WHITE
                    + Style.BRIGHT
                )
                .strip()
                .upper()
            )
            if update_option.upper() == "Y":
                update_stock_data(sheet, headers)
                break
            elif update_option == "N":
                break
            print(Fore.RED + Style.BRIGHT +
                  " Invalid input. Please enter 'Y' or 'N'.")

        while True:
            return_option = (
                input(
                    Fore.GREEN
                    + Style.BRIGHT
                    + " Return to Menu Y/N: "
                    + Fore.WHITE
                    + Style.BRIGHT
                )
                .strip()
                .upper()
            )
            if return_option == "Y":
                clearScreen()
                options()
                return
            elif return_option == "N":
                while True:
                    exit_option = (
                        input(
                            Fore.MAGENTA
                            + Style.BRIGHT
                            + " Exit Program Y/N: "
                            + Fore.WHITE
                            + Style.BRIGHT
                        )
                        .strip()
                        .upper()
                    )
                    if exit_option == "Y":
                        exit_program()
                        return
                    elif exit_option == "N":
                        print("\n")
                        print(Fore.YELLOW + Style.BRIGHT +
                              " Returning to main menu...")
                        time.sleep(2)
                        clearScreen()
                        options()
                        return
                    else:
                        print(
                            Fore.RED
                            + Style.BRIGHT
                            + " Invalid input. Please enter correctly"
                        )
            else:
                print(
                    Fore.RED + Style.BRIGHT +
                    " Invalid input. Please enter correctly"
                )


def update_stock_data(sheet, headers):
    """
    Function to allow for user to update data in sheets.
    """
    # Display current data
    print("\n")
    data = sheet.get_all_records()
    if not data:
        print(" No data available to update.")
        return

    while True:
        # Prompt user for print number and day to input data to specific cell
        stock_type = (
            input(
                Fore.YELLOW
                + Style.BRIGHT
                + f" Enter stock (Current, Production, Forecast): "
                + Fore.WHITE
                + Style.BRIGHT
            )
            .strip()
            .capitalize()
        )
        if stock_type not in ["Current", "Production", "Forecast"]:
            print(Fore.RED + Style.BRIGHT +
                  " Invalid input. Please enter correctly.")
            continue

        print_number = input(
            Fore.YELLOW
            + Style.BRIGHT
            + f" Enter print #: (1, 2, 3): "
            + Fore.WHITE
            + Style.BRIGHT
        )
        if print_number not in ["1", "2", "3"]:
            print(Fore.RED + Style.BRIGHT +
                  " Invalid input. Please enter correctly.")
            continue

        # Find column index for stock type and print number
        column_index = None
        for i, header in enumerate(headers, start=1):
            if header.startswith(f"print #{print_number}"):
                column_index = i
                break
        if column_index is None:
            print(Fore.RED + Style.BRIGHT
                  + f"Invalid input for #{print_number}.")
            continue

        row_index = None
        for i, record in enumerate(data, start=1):
            if record["Stock"] == stock_type:
                row_index = i + 1  # Do not allow for header update
                break
        if row_index is None:
            print(Fore.RED + Style.BRIGHT + f"Invalid input for {stock_type}.")
            continue

        # Input new value
        new_value = input(
            Fore.MAGENTA
            + Style.BRIGHT
            + f" Update data by entering new value for"
            " '{headers[column_index-1]}' on '{stock_type}': "
            + Fore.WHITE
            + Style.BRIGHT
        )
        if not new_value.replace(".", "", 1).isdigit():
            print(Fore.RED + Style.BRIGHT +
                  "Invalid input. Please enter correctly.")
            continue

        # Update indices
        try:
            sheet.update_cell(row_index, column_index, new_value)
            print("\n")
            time.sleep(1)
            typingPrint(" Data updated successfully!\n",
                        Fore.GREEN + Style.BRIGHT)
            print("\n")
            time.sleep(1)
            typingPrint(
                " Reloading updated Print Stock...\n",
                Fore.YELLOW + Style.BRIGHT
            )
            time.sleep(3)
            # Reload Print Stock
            view_stock()
            break
        except Exception as e:
            print(f" Error updating data: {e}")


def view_materials():  # Materials Function
    """
    View materials data
    """
    while True:
        sheet = SHEET.worksheet("Materials")
        materials_data = sheet.get_all_records()
        headers = sheet.row_values(1)

        clearScreen()
        print("\n")
        typingPrint(" Viewing Materials...\n", Fore.MAGENTA + Style.BRIGHT)
        print("\n")
        time.sleep(1)

        display_table(materials_data, headers)
        print("\n")

        while True:
            update_option = (
                input(
                    Fore.GREEN
                    + Style.BRIGHT
                    + " Update Data Y/N: "
                    + Fore.WHITE
                    + Style.BRIGHT
                )
                .strip()
                .upper()
            )
            if update_option.upper() == "Y":
                update_materials_data(sheet, headers)
                break
            elif update_option == "N":
                break
            print(Fore.RED + Style.BRIGHT +
                  " Invalid input. Please enter 'Y' or 'N'.")

        while True:
            return_option = (
                input(
                    Fore.GREEN
                    + Style.BRIGHT
                    + " Return to Menu Y/N: "
                    + Fore.WHITE
                    + Style.BRIGHT
                )
                .strip()
                .upper()
            )
            if return_option == "Y":
                clearScreen()
                options()
                return
            elif return_option == "N":
                while True:
                    exit_option = (
                        input(
                            Fore.MAGENTA
                            + Style.BRIGHT
                            + " Exit Program Y/N: "
                            + Fore.WHITE
                            + Style.BRIGHT
                        )
                        .strip()
                        .upper()
                    )
                    if exit_option == "Y":
                        exit_program()
                        return
                    elif exit_option == "N":
                        print("\n")
                        print(Fore.YELLOW + Style.BRIGHT +
                              " Returning to main menu...")
                        time.sleep(2)
                        clearScreen()
                        options()
                        return
                    else:
                        print(
                            Fore.RED
                            + Style.BRIGHT
                            + " Invalid input. Please enter correctly."
                        )
            else:
                print(
                    Fore.RED + Style.BRIGHT +
                    " Invalid input. Please enter correctly."
                )


def update_materials_data(sheet, headers):
    """
    Function to allow for user to update data in materials sheet.
    """
    # Display current data
    print("\n")
    data = sheet.get_all_records()
    if not data:
        print(" No data available to update.")
        return

    while True:
        # Prompt user for materials and quantity to input data to specific cell
        materials_type = (
            input(
                Fore.YELLOW
                + Style.BRIGHT
                + f" Enter material type"
                "(Screen, Squeegee, Stencil, Plastic, Ink, Paper ): "
                + Fore.WHITE
                + Style.BRIGHT
            )
            .strip()
            .capitalize()
        )
        if materials_type not in [
            "Screen",
            "Squeegee",
            "Stencil",
            "Plastic",
            "Ink",
            "Paper",
        ]:
            print(Fore.RED + Style.BRIGHT +
                  " Invalid input. Please enter correctly.")
            continue

        # Find index for materials type and quantity
        row_index = None
        for i, record in enumerate(data, start=1):
            if record["Materials"] == materials_type:
                row_index = i + 1  # Do not allow for header update
                break
        if row_index is None:
            print(Fore.RED + Style.BRIGHT
                  + f"Invalid input for {materials_type}.")
            continue

        # Input new value
        new_value = input(
            Fore.MAGENTA
            + Style.BRIGHT
            + f" Update data by entering new value"
            " for 'Quantity' on '{materials_type}': "
            + Fore.WHITE
            + Style.BRIGHT
        )
        if not new_value.replace(".", "", 1).isdigit():
            print(Fore.RED + Style.BRIGHT +
                  "Invalid input. Please enter correctly.")
            continue

        # Quantity coumn index
        column_index = 2
        try:
            sheet.update_cell(row_index, column_index, new_value)
            print("\n")
            time.sleep(1)
            typingPrint(" Data updated successfully!\n",
                        Fore.GREEN + Style.BRIGHT)
            print("\n")
            time.sleep(1)
            typingPrint(
                " Reloading updated Materials Stock...\n",
                Fore.YELLOW + Style.BRIGHT
            )
            time.sleep(3)
            # Reload Materials Stock
            view_materials()
            break
        except Exception as e:
            print(f" Error updating data: {e}")


def exit_program():
    clearScreen()
    print("\n")
    typingPrint(" Exiting the program...", Fore.YELLOW + Style.BRIGHT)
    time.sleep(2)
    print("\n")
    typingPrint(" Thank you for using ** Print Statement **")
    time.sleep(3)
    print("\n")
    typingPrint(" Reloading welcome screen...", Fore.MAGENTA + Style.BRIGHT)
    time.sleep(3)
    clearScreen()
    welcome()
    options()


options()
