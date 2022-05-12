from enum import Enum
from os import system

from tabulate import tabulate


class Days(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4

    def __str__(self):
        if self.name in ('MONDAY', 'FRIDAY'):
            return f'{self.name}    '
        elif self.name == 'TUESDAY':
            return f'{self.name}   '
        elif self.name == 'WEDNESDAY':
            return f'{self.name} '
        elif self.name == 'THURSDAY':
            return f'{self.name}  '


class Color(Enum):
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = ''
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
    NONE = None

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
    def __init__(self, day='', start_hour='', start_minute=None, subject=Subjects.NONE, type=None):
        self.day = day
        self.start_hour = start_hour
        self.start_minute = start_minute
        self.subject = subject
        self.type = type

    def __eq__(self, object):
        if self.day == object.day.value and self.start_hour == object.start_hour:
            return True
        return False

    def __str__(self):
        return tabulate([[self.day.name, f'{self.start_hour}:{self.start_minute}', str(self.subject), self.type.name]])


class LectureFile():
    def __init__(self, file_path='', date='', file_name='', lecture=Lecture()):
        self.__file_path = file_path
        self.date = date
        self.__lecture = lecture
        self.__file_name = file_name

    def copy(self, lecture_file):
        self.__file_path = lecture_file.file_path
        self.date = lecture_file.date
        self.__lecture = lecture_file.lecture
        self.__file_name = lecture_file.file_name

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
        self.__file_path = new_file_name

    @property
    def lecture(self):
        return self.__lecture

    @lecture.setter
    def lecture(self, new_lecture):
        self.__lecture = new_lecture

    def __str__(self):
        return tabulate([[in_color(self.file_name, Color.CYAN), self.date, str(self.lecture.subject)]],
                        ['File name', 'Date created', 'Subject'])


def process_exception(exception, exit=False):
    system('cls')
    print(exception)
    print_cursor()
    input()
    system('cls')
    if exit:
        exit()


def empty_list(list):
    for item in range(0, len(list)):
        list.pop()


print_cursor = lambda: print_in_color('>> ', Color.DARKCYAN, Color.BOLD.value, '')
print_in_color = lambda text, color, bold='', end='\n': print(f'{bold}{color.value}{text}{Color.END.value}', end=end)
in_color = lambda text, color, bold='': f'{bold}{color.value}{text}{Color.END.value}'

# Subjects full names
paths_to_subjects = {
    Subjects.CLOUD: 'Cloud computing u elektroenergetskim sistemima',
    Subjects.OSKO: 'Osnove softvera sa kritičnim odzivom u elektroenergetskim sistemima',
    Subjects.REES: 'Razvoj elektroenergetskog softvera',
    Subjects.RVA: 'Razvoj višeslojnih aplikacija u elektroenergetskim sistemima',
    Subjects.WEB: 'Veb programiranje',
}
