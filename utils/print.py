from constants.constants import *
from utils.utilities import print_in_color, Color, tabulate


# Loads data and prints the table
def load_table():
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
def print_file_input_instructions():
    print_in_color('      0\t', Color.WHITE, Color.BOLD.value, '')
    print('- Automatically process all files')
    print_in_color(f'   1-{len(lecture_files)}\t', Color.WHITE, Color.BOLD.value, '')
    print('- Process file with that index')
    print_in_color('    q/Q\t', Color.WHITE, Color.BOLD.value, '')
    print('- Quit\n')


