from datetime import datetime
from constants.exceptions import FileIdentificationException
from constants.constants import *
from utils.utilities import LectureFile, empty_list, process_exception
from utils.printer import print_file_selection
from utils.scanner import scan_files


# Loads data
def load():
    scan_files()
    __load_files()
    print_file_selection()

def __load_files():
    # Empty lecture files
    empty_list(lecture_files)

    # Identify files
    for file in file_names:
        try:
            __determine_lecture_by_file(file)
        except FileIdentificationException as e:
            process_exception(e)

# Returns false if lecture couldn't be determined
def __determine_lecture_by_file(file):
    # Parse data from file name
    data = file.split('-')
    year, month, day, hour = int(data[0]), int(data[1]), int(data[2].split(' ')[0]), int(data[2].split(' ')[1])
    weekday = datetime(year, month, day).weekday()
    current_lecture = Lecture(weekday, hour)

    # Determine lecture from schedule
    for lecture in schedule:
        if current_lecture == lecture:  # Add lecture file to the list of lecture files
            current_lecture.day = lecture.day
            current_lecture.start_minute = lecture.start_minute
            current_lecture.subject = lecture.subject
            current_lecture.type = lecture.type
            file_path = path_to_recordings + '\\' + file
            temp_lecture_file = LectureFile(file_path, f'{day}.{month}.{year}', file, lecture)
            lecture_files.append(temp_lecture_file)
            return
            
    # Raise exception if file couldn't be identified using the schedule
    raise FileIdentificationException(file)