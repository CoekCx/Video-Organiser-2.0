from utils.utilities import Color, in_color


class ScanningException(Exception):
    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        if self.message is None:
            return in_color('An error occurred while scanning files', Color.RED)
        else:
            return in_color(self.message, Color.RED)
