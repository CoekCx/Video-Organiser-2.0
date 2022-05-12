from constants.constants import selected_file
from utils.print import load_table, print_file_input_instructions
from utils.utilities import Color, print_in_color, print_cursor, system


class Printer:

    # Prints file selection menu
    @staticmethod
    def print_file_selection():
        print_file_input_instructions()
        load_table()

    # Prints confirmation menu for file processing
    @staticmethod
    def print_confirmation_menu():
        system('cls')
        print_in_color('    y/Y\t', Color.WHITE, Color.BOLD.value, '')
        print('- Process selected file')
        print_in_color('    n/N\t', Color.WHITE, Color.BOLD.value, '')
        print('- Abort processing file\n')
        print(selected_file)
        print()
        print_cursor()
