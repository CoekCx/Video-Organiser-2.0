from utils import print_cursor
from os import system
from printer import *
from scanner import *
from loader import *


# Main menu
def menu():
    while True:
        system('cls')
        load()

# Loads data
def load():
    scan_files()
    load_files()
    print_file_selection()
    print_cursor()
    input()


if __name__ == '__main__':
    menu()