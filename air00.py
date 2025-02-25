import sys


# Utils
def is_not_same(char: str, separator: str) -> bool:
    for sep in separator:
        if char == sep:
            return False
    return True

def get_array(string: str) -> list:
    array: list = []
    element: str = ''
    for char in string:
        if is_not_same(char, ' \t\n'):
            element += char
        else:
            array.append(element)
            element = ''
    array.append(element)
    return array

def display_array(array: list) -> None:
    for element in array:
        print(element)

# Error
def is_valid_arguments(args: tuple) -> tuple:
    if len(args) != 1 :
        print('error')
        return False
    return args[0]

# Parsing
def get_arguments() -> tuple:
    args = sys.argv[1:]
    return args

# Resolution
def split_string() -> list:
    arg: str = is_valid_arguments(get_arguments())
    if not arg:
        return
    return get_array(str(arg))

# Display
display_array(split_string())
