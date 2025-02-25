import sys


# Utils
def is_separator(string: str, separator: str) -> bool:
    for i in range(len(separator)):
        if string[i] != separator[i]:
            return False
    return True

def get_array(string: str, separator: str) -> list:
    i: int = 0
    array: list = []
    element: str = ''
    while i < len(string):
        if string[i] == separator[0]:
            if is_separator(string[i:], separator):
                array.append(element)
                element = ''
                i += len(separator)
        element += string[i]
        i += 1
    array.append(element)
    return array

def display_array(array: list) -> None:
    if array:
        for element in array:
            print(element)


# Error
def is_valid_arguments(args: tuple) -> bool:
    if len(args) != 2:
        print('error')
        return False
    return args

# Parsing
def get_arguments() -> tuple:
    args: tuple = sys.argv[1:]
    return args

# Resolution
def split_string() -> list:
    args: tuple = is_valid_arguments(get_arguments())
    if not args:
        return args
    return get_array(args[0], args[1])

# Display
display_array(split_string())
