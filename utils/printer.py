from constants.constants import *
from utils.utilities import print_in_color, Color, system, tabulate, print_cursor


# Prints file selection menu
def print_file_selection():
    __print_file_input_instructions()
    __load_table()

# Loads data and prints the table
def __load_table():
    data = []
    __parse_files(data)
    print(__generate_file_table(data))

# Generates table for the file selections menu
__generate_file_table = lambda data: tabulate(data, headers=['Index', 'Date', 'Day', 'Time', 'Subject', 'Type'])

# Parse files into data structure
def __parse_files(data):
    index = 1
    for file in lecture_files:
        data.append([index, file.date, file.lecture.day.name, f'{file.lecture.start_hour}:{file.lecture.start_minute}', file.lecture.subject, file.lecture.type.name])
        index += 1

# Prints input information
def __print_file_input_instructions():
    print_in_color('      0\t', Color.WHITE, Color.BOLD.value, '')
    print('- Automatically process all files')
    print_in_color(f'   1-{len(lecture_files)}\t', Color.WHITE, Color.BOLD.value, '')
    print('- Process file with that index')
    print_in_color('    q/Q\t', Color.WHITE, Color.BOLD.value, '')
    print('- Quit\n')

# Prints confirmation menu for file processing
def print_confirmation_menu():
    system('cls')
    print_in_color('    y/Y\t', Color.WHITE, Color.BOLD.value, '')
    print('- Process selected file')
    print_in_color('    n/N\t', Color.WHITE, Color.BOLD.value, '')
    print('- Abort processing file\n')
    print(selected_file)
    print()
    print_cursor()
