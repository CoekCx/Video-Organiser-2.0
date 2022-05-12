from constants.constants import lecture_files
from exceptions.invalid_input_exception import InvalidInput
from utils.file_processing import process_file, automatic_file_processing
from utils.utilities import process_exception, print_cursor


class Handler():
    # Take user input and process it
    def take_input(self):
        print_cursor()
        user_input = input()
        self.__handle_input(user_input)

    # Handle input accordingly
    def __handle_input(self, user_input):
        user_input = self.__validate_input(user_input)
        if not user_input:  # Validate input
            return

        if user_input == -1:
            exit()
        elif user_input == 0:
            automatic_file_processing()
        else:
            process_file(user_input - 1)  # Subtracted by 1 to adjust the file index

    # Returns false if input is invalid
    @staticmethod
    def __validate_input(user_input):
        try:
            if user_input == '':
                user_input = None
                return True

            if user_input in ('Q', 'q'):
                user_input = -1
                return True

            user_input = int(user_input)
            if user_input < 0 or user_input > len(lecture_files):
                raise InvalidInput()

            return user_input
        except:
            process_exception(InvalidInput())
            return False