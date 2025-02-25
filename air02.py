import sys


# Utils
def get_string(array: list, separator: str) -> str:
    string: str = ''
    for element in array:
        string += element
        if element != array[len(array) - 1]:
            string += separator
    return string

def display_string(string: str) -> None:
    if string:
        print(string)

# Error
def is_valid_arguments(args: tuple) -> bool:
    if len(args) < 3:
        print('error')
        return False
    return args

# Parsing
def get_arguments() -> tuple:
    args: tuple = sys.argv[1:]
    return args

# Resolution
def concatenate_array() -> str:
    args: tuple = is_valid_arguments(get_arguments())
    if not args:
        return  
    return get_string(args[:len(args) - 1], args[len(args) - 1])

# Display
display_string(concatenate_array())
