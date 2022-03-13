from utils.utilities import system
from utils.loader import load
from handler import request_input


# Main menu
def menu():
    while True:
        system('cls')
        load()
        request_input()
