import sys


# Utils
def is_not_included(string: str, reference: str) -> bool:
    included: bool = False
    for i in range(len(string)):
        if string[i] == reference[0]:
            j: int = 0
            while (j < len(reference) and len(string[i:]) >= len(reference)):
                if string[i + j] != reference[j]:
                    break
                j += 1
            if j == len(reference):
                return False
    return True

def delete_elements(array: list, reference: str) -> list:
    new_array: list = []
    i: int = 0
    while i < len(array):
        if is_not_included(array[i], reference):
            new_array.append(array.pop(i))
        else:
            i += 1
    return new_array

def display_array(array: list) -> None:
    if array:
        for i in range(len(array)):
            print(array[i], end='')
            if i != len(array) - 1:
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
def control_health_pass() -> list:
    args: tuple = is_valid_arguments(get_arguments())
    if not args:
        return
    return delete_elements(args[:len(args) - 1], args[len(args) - 1])

# Display
display_array(control_health_pass())
