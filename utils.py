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
            return in_color(paths_to_subjects[self], Color.YELLOW)
        elif self.name == 'OSKO':
            return in_color(paths_to_subjects[self], Color.GREEN)
        elif self.name == 'REES':
            return in_color(paths_to_subjects[self], Color.BLUE)
        elif self.name == 'RVA':
            return in_color(paths_to_subjects[self], Color.PURPLE)
        elif self.name == 'WEB':
            return in_color(paths_to_subjects[self], Color.RED)

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
        return in_color(f'{self.file_name}:\t{self.lecture}', Color.CYAN)

def print_error(message):
        system('cls')
        print_in_color(message, Color.RED)
        input()
        exit()

def wrong_input():
    system('cls')
    print(f'{Color.RED.value}You\'ve entered an invalid value!{Color.END.value}')
    input()

print_cursor = lambda : print(f'{Color.CYAN.value}>>{Color.END.value}', end='')
print_in_color = lambda text, color, end='\n': print(f'{color.value}{text}{Color.END.value}', end=end)
in_color = lambda text, color, bold='': f'{bold}{color.value}{text}{Color.END.value}'

# Subjects full names
paths_to_subjects = {
    Subjects.CLOUD: 'Cloud computing u elektroenergetskim sistemima',
    Subjects.OSKO: 'Osnove softvera sa kritičnim odzivom u elektroenergetskim sistemima',
    Subjects.REES: 'Razvoj elektroenergetskog softvera',
    Subjects.RVA: 'Razvoj višeslojnih aplikacija u elektroenergetskim sistemima',
    Subjects.WEB: 'Veb programiranje',
}