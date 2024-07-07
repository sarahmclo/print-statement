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
    Display welcome screen text
    """
    typingPrint("Welcome to Print Statement\n",Fore.LIGHTMAGENTA_EX)
    typingPrint("A sales revenue and inventory management system for sarah_prints_inc.")
    time.sleep(5)
    clearScreen()

    typingPrint("PRINT STATEMENT  is a comprehensive inventory management system for a small screen printing business that sells at local markets.\n"
    "It enables users to oversee sales, monitor stock, and track materials and preint-runs efficiently.\n")

welcome()