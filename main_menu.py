from matplotlib.pyplot import sca
from constants import *
from pathlib import Path
import os

from utils import printCursor

# Main menu
def menu():
    while True:
        os.system('cls')
        load()

# Loads data
def load():
    scan_files()
    printCursor()
    input()

# Scans existing files
def scan_files():
    try:
        scan_subject_folders()
        scan_recordings()
    except:
        pass
    print(file_count)

def scan_recordings():
    # TODO: Implement recordings scaning
    raise NotImplementedError()

# Scans subject folders for folder count
def scan_subject_folders():
    for subject in paths_to_subjects.values():
        subject_path = path_to_semester + '\\' + subject
        paths = sorted(Path(subject_path).iterdir())
        for path in paths:
            path = path.__str__().replace('\\', '\\\\')
            if(path.__str__()[-1] == 'P'):
                count_folders(path, subject, LectureType.PREDAVANJE.value)
            elif(path.__str__()[-1] == 'V'):
                count_folders(path, subject, LectureType.VEZBE.value)

# Counts folders and saves that data
def count_folders(path, subject, lecture_type):
    paths = sorted(Path(path).iterdir())
    folder_count = 0
    for p in paths:
        folder_count += 1
    subject_index = [index.value for index, name in paths_to_subjects.items() if name == subject]
    file_count[subject_index[0]][lecture_type] = folder_count

if __name__ == '__main__':
    menu()