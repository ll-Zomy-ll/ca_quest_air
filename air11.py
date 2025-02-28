import sys


# Utils
def get_layer(char: str, brick_char: int, brick: int) -> str:
    layer: str = ''
    spaces: int = brick - brick_char
    put_char: bool = True
    for i in range(2):
        for space in range(int(spaces / 2)):
            layer += ' '
        if put_char:
            for j in range(brick_char):
                layer += char
            put_char = False
    return layer

def create_pyramid(char: str, layer: int) -> list:
    brick: int = 1 + 2 * (layer - 1)
    pyramid: list = []
    for i in range(1, layer + 1):
        brick_char = 1 + 2 * (i - 1)
        pyramid.append(get_layer(char, brick_char, brick))
    return pyramid

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

def is_valid_char(char: str) -> bool:
    if len(char) != 1:
        print('error')
        return False
    return True

def is_valid_number(number: str) -> bool:
    for digit in number:
        if not digit.isdigit():
            print('error')
            return False
    return True

# Parsing
def get_arguments() -> tuple:
    args: tuple = sys.argv[1:]
    return args

# Resolution
def generate_pyramid() -> list:
    args: tuple = is_valid_arguments(get_arguments())
    if not args:
        return
    if not is_valid_char(args[0]):
        return
    if not is_valid_number(args[1]):
        return
    return create_pyramid(args[0], int(args[1]))

# Display
display_array(generate_pyramid())
