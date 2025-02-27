import sys


# Utils
def rotate_left(array: list) -> list:
    new_array: list = [] 
    for i in range(1, len(array)):
        new_array.append(array[i])
    new_array.append(array[0])
    return new_array

def display_array(array: list) -> None:
    if array:
        for i in range(len(array)):
            print(array[i], end='')
            if array[i] != array[len(array) - 1]:
                print(', ', end='')
        print()

# Error
def is_valid_arguments(args: tuple) -> bool:
    if len(args) < 2:
        print('error')
        return False
    return args

# Parsing
def get_arguments() -> tuple:
    args: tuple = sys.argv[1:]
    return args

# Resolution
def lrotate_array() -> list:
    args: tuple = is_valid_arguments(get_arguments())
    if not args:
        return
    return rotate_left(args)

# Display
display_array(lrotate_array())
