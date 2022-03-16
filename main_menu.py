from utils.utilities import system
from utils.load import load
from helpers.handler import request_input


# Main menu
def menu():
    while True:
        system('cls')
        load()
        request_input()
