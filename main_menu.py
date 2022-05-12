from helpers.handler import Handler
from helpers.loader import Loader
from utils.utilities import system


# Main menu
def menu():
    loader = Loader()
    handler = Handler()

    while True:
        system('cls')
        loader.load_data()
        handler.take_input()
