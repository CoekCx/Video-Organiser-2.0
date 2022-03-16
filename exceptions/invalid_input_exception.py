from utils.utilities import Color, in_color


class InvalidInput(Exception):
    def __init__(self, message = None):
        self.message = message
    
    def __str__(self):
        if self.message is None:
            return in_color('Invalid input', Color.RED)
        else:
            return in_color(self.message, Color.RED)