import sys


# Utils
def sort_array(array: list, start: int, end: int) -> int:
    pivot: int = array[end]
    new_pivot: int = start
    for i in range(start, end):
        if array[i] <= pivot:
            array[i], array[new_pivot] = array[new_pivot], array[i]
            new_pivot += 1
    array[new_pivot], array[end] = array[end], array[new_pivot]
    return new_pivot

def my_quick_sort(numbers: list, start: int, end: int) -> list:
    if start < end:
        pivot: int = sort_array(numbers, start, end)
        my_quick_sort(numbers, start, pivot - 1)
        my_quick_sort(numbers, pivot + 1, end)
    return numbers

def display_array(array: list) -> None:
    if array:
        for element in array:
            print(element, end=' ')
        print()

# Errror
def is_valid_arguments(args: tuple) -> bool:
    if len(args) < 2:
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
def apply_quick_sort() -> list:
    args:tuple = is_valid_arguments(get_arguments())
    if not args:
        return
    numbers: list = []
    for arg in args:
        temp_number = is_valid_number(arg)
        if not temp_number:
            return
        numbers.append(int(temp_number))
    return my_quick_sort(numbers, 0, len(numbers) - 1)

# Display
display_array(apply_quick_sort())
