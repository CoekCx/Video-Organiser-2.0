from utils import print_cursor
from os import system
from scanner import *


# Main menu
def menu():
    while True:
        system('cls')
        load()

# Loads data
def load():
    scan_files()
    print_cursor()
    input()


if __name__ == '__main__':
    menu()