from utils.print import load_table, print_file_input_instructions
from utils.utilities import Color, print_in_color, print_cursor, system
from constants.constants import selected_file


class Printer():

    # Prints file selection menu
    def print_file_selection(self):
        print_file_input_instructions()
        load_table()

    # Prints confirmation menu for file processing
    def print_confirmation_menu(self):
        system('cls')
        print_in_color('    y/Y\t', Color.WHITE, Color.BOLD.value, '')
        print('- Process selected file')
        print_in_color('    n/N\t', Color.WHITE, Color.BOLD.value, '')
        print('- Abort processing file\n')
        print(selected_file)
        print()
        print_cursor()