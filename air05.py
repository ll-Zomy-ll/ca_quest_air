import sys


# Utils
def get_results(numbers: list, operator: int) -> list:
    results: list = []
    for number in numbers:
        results.append(number + operator)
    return results

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
    for digit in number.lstrip('-+'):
        if not digit.isdigit():
            print('error')
            return False
    return number

# Parsing
def get_arguments() -> tuple:
    args: tuple = sys.argv[1:]
    return args

# Resolution
def add_or_substract() -> list:
    args: tuple = is_valid_arguments(get_arguments())
    if not args:
        return
    numbers: list = []
    for arg in args:
        temp_number = is_valid_number(arg)
        if not temp_number:
            return
        numbers.append(int(temp_number))
    return get_results(numbers[:len(numbers) - 1], numbers[len(numbers) - 1])

# Display
display_array(add_or_substract())
