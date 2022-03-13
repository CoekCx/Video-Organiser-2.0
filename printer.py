from utils import print_in_color, in_color, Color
from constants import *


# Prints file processing menu
def print_file_table():
    print_file_text()
    print_file_header()
    print_files()
    print_file_line()

# Prints input information
def print_file_text():
    print_in_color('      0\t', Color.WHITE, Color.BOLD.value, '')
    print('- Automatically process all files')
    print_in_color(f'   1-{len(lecture_files)}\t', Color.WHITE, Color.BOLD.value, '')
    print('- Process file with that index')
    print_in_color(f'    q/Q\t', Color.WHITE, Color.BOLD.value, '')
    print('- Quit\n')

def print_file_header():
    print_file_line()
    print_in_color(f'| INDEX |      DATE     |      DAY      | TIME  |                                SUBJECT                                |   TYPE   |', Color.CYAN)
    print_file_line()

def print_files():
    index = 1
    for f in lecture_files:
        print_in_color('|   ', Color.CYAN, end='')
        print(in_color(f'{index}\t', Color.WHITE, Color.BOLD.value, ''), end='')
        print(f)
        index += 1

def print_file_line():
    for i in range(0, 132):
        print_in_color('-', Color.CYAN, Color.BOLD.value, '')
    print()