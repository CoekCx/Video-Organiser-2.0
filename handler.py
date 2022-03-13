from constants.exceptions import InvalidInput
from constants.constants import lecture_files
from utils.utilities import process_exception, print_cursor


# Take user input and process it
def request_input():
    print_cursor()
    user_input = input()
    handle_input(user_input)

# Handle input accordingly
def handle_input(user_input):
    if validate_input(user_input):
        # TODO: Implement input handling
        raise NotImplementedError

# Returns false if input is invalid
def validate_input(user_input):
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

        return True
    except:
        process_exception(InvalidInput())
        return False