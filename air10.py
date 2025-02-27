import sys


# Utils
def read_file(file_name: str) -> str:
    try:
        file = open(file_name, 'r')
        content = file.read()
    except FileNotFoundError:
        return 'error'
    file.close()
    return content

# Error
def is_valid_arguments(args: tuple) -> bool:
    if len(args) != 1:
        print('error')
        return False
    return args[0]

# Parsing
def get_arguments() -> tuple:
    args: tuple = sys.argv[1:]
    return args

# Resolution
def display_file() -> str:
    arg: str = is_valid_arguments(get_arguments())
    if not arg:
        return
    return print(read_file(arg))

# Display
display_file()
