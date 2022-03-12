from utils import Subjects, Lecture, LectureType, Days


# Subjects full names
paths_to_subjects = {
    Subjects.CLOUD: 'Cloud computing u elektroenergetskim sistemima',
    Subjects.OSKO: 'Osnove softvera sa kritičnim odzivom u elektroenergetskim sistemima',
    Subjects.REES: 'Razvoj elektroenergetskog softvera',
    Subjects.RVA: 'Razvoj višeslojnih aplikacija u elektroenergetskim sistemima',
    Subjects.WEB: 'Veb programiranje',
}

schedule = [
    Lecture(Days.MONDAY, 8, 15, Subjects.CLOUD, LectureType.PREDAVANJE),
    Lecture(Days.MONDAY, 11, 15, Subjects.REES, LectureType.PREDAVANJE),
    Lecture(Days.WEDNESDAY, 8, 15, Subjects.WEB, LectureType.PREDAVANJE),
    Lecture(Days.WEDNESDAY, 11, 15, Subjects.RVA, LectureType.PREDAVANJE),
    Lecture(Days.FRIDAY, 8, 15, Subjects.OSKO, LectureType.PREDAVANJE),
]

# Number of files in subject folders
file_count = [
    [0, 0], # CLOUD
    [0, 0], # OSKO
    [0, 0], # REES
    [0, 0], # RVA
    [0, 0]  # WEB
]  # P, V

path_to_semester = 'D:\\Coek\\FTN\\6. Semestar'
path_to_recordings = 'D:\\Coek\\Recording\\6. Semestar'