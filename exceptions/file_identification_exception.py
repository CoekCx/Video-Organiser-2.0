from utils.utilities import Color, in_color


class FileIdentificationException(Exception):
    def __init__(self, file_name, message = None):
        self.file_name = file_name
        self.message = message
    
    def __str__(self):
        if self.message is None:
            return in_color(f'File \'{self.file_name}\' couldn\'t be identified using the schedule', Color.RED)
        else:
            return in_color(self.message, Color.RED)