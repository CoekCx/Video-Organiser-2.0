from utils import print_cursor, paths_to_subjects
from re import search
from constants import *
from pathlib import Path
from os import system


# Main menu
def menu():
    while True:
        system('cls')
        load()

# Loads data
def load():
    scan_files()
    print_cursor()
    input()

# Scans existing files
def scan_files():
    try:
        scan_subject_folders()
        scan_recordings()
    except:
        system('cls')
        print('An error occured while scaning files.')
        input()
        exit()

# Scans existing recordings
def scan_recordings():
    # Empty file names
    for file_name in range(0, len(file_names)):
        file_names.pop()
    
    # Scan files
    paths = sorted(Path(path_to_recordings).iterdir())

    # Filter files with mask and add them to the list
    mask = r'[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}-[0-9]{2}-[0-9]{2}\.mkv'
    for path in paths:
        path = path.__str__().split(path_to_recordings+'\\')[1]
        if search(mask, path):
            file_names.append(path)
    
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