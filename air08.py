import sys


# Utils
def sorted_fusion(first_array: list, second_array: list) -> list:
    i: int = 0
    j: int = 0
    new_array: list = []
    for counter in range(len(first_array + second_array) - 2):
        if first_array[i] < second_array[j]:
            new_array.append(first_array[i])
            if i < len(first_array) - 1:
                i += 1
        else:
            new_array.append(second_array[j])
            if j < len(second_array) - 1:
                j += 1
    return new_array

def display_array(array: list) -> None:
    if array:
        for element in array:
            print(element, end=' ')
        print()

# Error
def is_valid_arguments(args: tuple) -> bool:
    if len(args) < 3:
        print('error')
        return False
    return args

def is_valid_number(number: str) -> bool:
    if number == 'fusion':
        return True
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
    if not args:
        return
    fusion: int = -1
    numbers: list = []
    for i in range(len(args)):
        temp_number = is_valid_number(args[i])
        if not temp_number:
            return
        if (args[i] == 'fusion' and fusion < 0):
            numbers.append(float('inf'))
            fusion = i + 1
        elif (args[i] == 'fusion' and fusion > 0):
            print('error')
            return
        else:
            numbers.append(int(temp_number))
    numbers.append(float('inf'))
    return sorted_fusion(numbers[:fusion], numbers[fusion:])

# Display
display_array(merge_arrays())
