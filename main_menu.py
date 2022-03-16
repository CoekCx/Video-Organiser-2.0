from helpers.loader import Loader
from utils.utilities import system
from helpers.handler import request_input


# Main menu
def menu():
    loader = Loader()

    while True:
        system('cls')
        loader.load_data()
        request_input()
