from utils.utils import Color, in_color


class ScaningException(Exception):
    def __init__(self, message = None):
        self.message = message
    
    def __str__(self):
        if self.message is None:
            return in_color('An error occured while scaning files.', Color.RED)
        else:
            return in_color(self.message, Color.RED)

class FileIdentificationException(Exception):
    def __init__(self, file_name, message = None):
        self.file_name = file_name
        self.message = message
    
    def __str__(self):
        if self.message is None:
            return in_color(f'File \'{self.file_name}\' couldn\'t be identified using the schedule.', Color.RED)
        else:
            return in_color(self.message, Color.RED)