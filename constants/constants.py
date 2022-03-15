from utils.utilities import Subjects, Lecture, LectureType, LectureFile, Days


schedule = [
    Lecture(Days.MONDAY, 8, 15, Subjects.CLOUD, LectureType.PREDAVANJE),
    Lecture(Days.MONDAY, 11, 15, Subjects.REES, LectureType.PREDAVANJE),
    Lecture(Days.WEDNESDAY, 8, 15, Subjects.WEB, LectureType.PREDAVANJE),
    Lecture(Days.WEDNESDAY, 11, 15, Subjects.RVA, LectureType.PREDAVANJE),
    Lecture(Days.FRIDAY, 8, 15, Subjects.OSKO, LectureType.PREDAVANJE),
]

# Number of files in subject folders
file_count = {
   Subjects.CLOUD:  [0, 0],
   Subjects.OSKO:   [0, 0],
   Subjects.REES:   [0, 0],
   Subjects.RVA:    [0, 0],
   Subjects.WEB:    [0, 0]
  }                # P, V

path_to_recordings = 'D:\\Coek\\Recording\\6. Semestar'
path_to_semester = 'D:\\Coek\\FTN\\6. Semestar'
selected_file = LectureFile()
lecture_files = []
file_names = []