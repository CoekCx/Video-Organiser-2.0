from re import search
from pathlib import Path
from exceptions.scaning_exception import ScaningException
from constants.constants import *
from utils.utilities import empty_list, process_exception, paths_to_subjects


# Scans existing files
def scan_files():
    try:
        scan_subject_folders()
        __scan_recordings()
    except:
        process_exception(ScaningException(), True)
    
# Scans subject folders for folder count
def scan_subject_folders():
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
def __count_folders(path, subject_name, lecture_type):
    paths = sorted(Path(path).iterdir())
    folder_count = 0
    for p in paths:
        folder_count += 1
    subject = [index for index, name in paths_to_subjects.items() if name == subject_name]
    (file_count[subject[0]])[lecture_type] = folder_count

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

