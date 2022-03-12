from enum import Enum
from constants import *


class Days(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4

class Color(Enum):
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class LectureType(Enum):
    PREDAVANJE = 0
    VEZBE = 1

class Subjects(Enum):
    CLOUD = 0
    OSKO = 1
    REES = 2
    RVA = 3
    WEB = 4

    def __str__(self):
        if self.name == 'CLOUD':
            return f'{Color.YELLOW.value}{paths_to_subjects[self]}{Color.END.value}'
        elif self.name == 'OSKO':
            return f'{Color.GREEN.value}{paths_to_subjects[self]}{Color.END.value}'
        elif self.name == 'REES':
            return f'{Color.BLUE.value}{paths_to_subjects[self]}{Color.END.value}'
        elif self.name == 'RVA':
            return f'{Color.PURPLE.value}{paths_to_subjects[self]}{Color.END.value}'
        elif self.name == 'WEB':
            return f'{Color.RED.value}{paths_to_subjects[self]}{Color.END.value}'

class Lecture():
    def __init__(self, day, start_hour, start_minute, subject, type):
        self.day = day
        self.start_hour = start_hour
        self.start_minute = start_minute
        self.subject = subject
        self.type = type
    
    def __str__(self):
        result = ''

        if self.day.name in ('WEDNESDAY', 'THURSDAY'):
            result = f'{self.day.name}\t{self.start_hour}:{self.start_minute}\t{self.subject}'
        else:
            result = f'{self.day.name}\t\t{self.start_hour}:{self.start_minute}\t{self.subject}'
        if self.subject.name == 'CLOUD':
            result += f'\t\t\t\t{self.type.name}'
        elif self.subject.name == 'OSKO':
            result += f'\t{self.type.name}'
        elif self.subject.name == 'REES':
            result += f'\t\t\t\t\t{self.type.name}'
        elif self.subject.name == 'RVA':
            result += f'\t\t{self.type.name}'
        elif self.subject.name == 'WEB':
            result += f'\t\t\t\t\t\t\t{self.type.name}'

        return result

def printCursor():
    print(f'{Color.CYAN.value}>>{Color.END.value}', end='')
