from enum import Enum
from os import system


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

class SelectedFile():
    def __init__(self, file_path, lecture):
        self.__file_path = file_path
        self.__file_name = file_path
        self.__lecture = lecture
    
    @property
    def file_path(self):
        return self.__file_path
    
    @file_path.setter
    def file_path(self, new_file_path):
        self.__file_path = new_file_path
    
    @property
    def file_name(self):
        return self.__file_name
    
    @file_name.setter
    def file_name(self, new_file_name):
        self.__file_name = new_file_name
    
    @property
    def lecture(self):
        return self.__lecture
    
    @lecture.setter
    def lecture(self, new_lecture):
        self.__lecture = new_lecture
    
    def __str__(self):
        return f'{Color.CYAN.value}{self.file_name}:\t{self.lecture}{Color.END.value}'

def print_cursor():
    print(f'{Color.CYAN.value}>>{Color.END.value}', end='')

def wrong_input():
    system('cls')
    print(f'{Color.RED.value}You\'ve entered an invalid value!{Color.END.value}')
    input()

# Subjects full names
paths_to_subjects = {
    Subjects.CLOUD: 'Cloud computing u elektroenergetskim sistemima',
    Subjects.OSKO: 'Osnove softvera sa kritičnim odzivom u elektroenergetskim sistemima',
    Subjects.REES: 'Razvoj elektroenergetskog softvera',
    Subjects.RVA: 'Razvoj višeslojnih aplikacija u elektroenergetskim sistemima',
    Subjects.WEB: 'Veb programiranje',
}