from exceptions.scaning_exception import ScanningException
from utils.scan import scan_recordings, scan_subject_folders
from utils.utilities import process_exception


class Scanner:
    # Scans existing files
    @staticmethod
    def scan_files():
        try:
            scan_subject_folders()
            scan_recordings()
        except:
            process_exception(ScanningException(), True)
