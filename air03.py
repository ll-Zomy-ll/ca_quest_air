import sys


# Utils
def activate_ascii(array: list) -> list:
    ascii_array = [[ord(char) for char in ascii_string] for ascii_string in array]
    return ascii_array

def is_not_in_even_list(even_list: list, element: list) -> bool:
    for even in even_list:
        if even == element:
            return False
    return True

def has_got_pair(array: list, check: int) -> bool:
    for element in array[check + 1:]:
        if array[check] == element: 
            return True
    return False

def odd_ones_list(array: list) -> list:
    odd_list: list = []
    even_list: list = []
    for i in range(len(array)):
        if is_not_in_even_list(even_list, array[i]):
            if has_got_pair(array, i):
                even_list.append(array[i])
            else:
                odd_list.append(array[i])
    return odd_list

def deactivate_ascii(ascii_array: list) -> list:
    delimiter: str = ''
    string_array: list = []
    for ascii_string in ascii_array:
        temp_string = []
        for ascii_char in ascii_string:
            temp_string.append(chr(ascii_char))
        string_array.append(delimiter.join(temp_string))
    return string_array

def display_array(array: list) -> None:
    if array:
        for element in array:
            print(element)

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
def get_odd_one_out() -> list:
    args: tuple = is_valid_arguments(get_arguments())
    if not args:
        return
    return deactivate_ascii(odd_ones_list(activate_ascii(args)))

# Display
display_array(get_odd_one_out())
