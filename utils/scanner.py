from utils.utils import empty_list, print_error, paths_to_subjects
from pathlib import Path
from constants.constants import *
from re import search


# Scans existing files
def scan_files():
    try:
        __scan_subject_folders()
        __scan_recordings()
    except:
        print_error('An error occured while scaning files.', True)
    
# Scans subject folders for folder count
def __scan_subject_folders():
    for subject in paths_to_subjects.values():
        subject_path = path_to_semester + '\\' + subject
        paths = sorted(Path(subject_path).iterdir())
        for path in paths:
            path = path.__str__().replace('\\', '\\\\')
            if(path.__str__()[-1] == 'P'):
                __count_folders(path, subject, LectureType.PREDAVANJE.value)
            elif(path.__str__()[-1] == 'V'):
                __count_folders(path, subject, LectureType.VEZBE.value)

# Counts folders and saves that data
def __count_folders(path, subject, lecture_type):
    paths = sorted(Path(path).iterdir())
    folder_count = 0
    for p in paths:
        folder_count += 1
    subject_index = [index.value for index, name in paths_to_subjects.items() if name == subject]
    file_count[subject_index[0]][lecture_type] = folder_count

# Scans existing recordings
def __scan_recordings():
    # Empty file names
    empty_list(file_names)
    
    # Scan files
    paths = sorted(Path(path_to_recordings).iterdir())

    # Filter files with mask and add them to the list
    mask = r'[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}-[0-9]{2}-[0-9]{2}\.mkv'
    for path in paths:
        path = path.__str__().split(path_to_recordings+'\\')[1]
        if search(mask, path):
            file_names.append(path)

