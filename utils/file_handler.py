from utils.scanner import scan_subject_folders
from constants.constants import *
from utils.utilities import LectureFile
from utils.printer import print_confirmation_menu


def automatic_file_processing():
    raise NotImplementedError

def process_file(file_index):
    make_folder(file_index)

def make_folder(file_index):
    scan_subject_folders()
    selected_file.copy(lecture_files[file_index])
    input()
    # TODO: Implement folder generation
    #generate folder path
    #folder_path = path_to_semester.replace('\\', '/') + f'/{lecture_file.lecture.subject.}'

def __confirm_processing():
    print_confirmation_menu()
    # TODO: Implement file processing confirmation 
    raise NotImplementedError