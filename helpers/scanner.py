from exceptions.scaning_exception import ScaningException
from utils.scan import scan_recordings, scan_subject_folders
from utils.utilities import process_exception


class Scanner():
    # Scans existing files
    def scan_files(self):
        try:
            scan_subject_folders()
            scan_recordings()
        except:
            process_exception(ScaningException(), True)