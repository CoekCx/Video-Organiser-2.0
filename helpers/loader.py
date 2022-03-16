from helpers.printer import Printer
from helpers.scanner import Scanner
from utils.load import load_files


class Loader():
    def __init__(self):
        self.printer = Printer()
        self.scanner = Scanner()

    # Loads data
    def load_data(self):
        self.scanner.scan_files()
        load_files()
        self.printer.print_file_selection()