import sys


# Utils

# Error
def is_valid_arguments(args: tuple) -> bool:
    if len(args) < 3:
        print('error')
        return False
    return args

def is_valid_number(number: str) -> bool:
    for digit in number.lstrip('-'):
        if not digit.isdigit():
            print('error')
            return False
    return number

# Parsing
def get_arguments() -> tuple:
    args: tuple = sys.argv[1:]
    return args

# Resolution
def merge_arrays() -> list:
    args: tuple = is_valid_arguments(get_arguments())
    if not arg:
        return
    numbers: list = []
    for arg in args:
        temp_number = is_valid_number(arg)
        if not temp_number:
            return
        numbers.append(int(temp_number))
