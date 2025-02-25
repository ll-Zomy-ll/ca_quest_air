import sys


# Utils
def clean_string(string: str) -> str:
    i: int = 0
    while i < len(string) - 1:
        if string[i] == string[i + 1]:
            j: int = 0
            while j < len(string[i:]):
                if string[i] != string[i + j]:
                    break
                j += 1
            string = string[:i + 1] + string[i + j:]
        i += 1
    return string

def display_string(string: str) -> None:
    if string:
        print(string)

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
def just_one_at_time() -> str:
    arg = is_valid_arguments(get_arguments())
    if not arg:
        return
    return clean_string(arg)

# Display
display_string(just_one_at_time())
