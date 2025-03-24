from os import path
import subprocess
import tests


# Utils
def print_in_color(string: str, color: str) -> None:
    if color == 'red':
        print("\033[91m {}\033[00m" .format(string))
    if color == 'green':
        print("\033[92m {}\033[00m" .format(string))
    if color == 'yellow':
        print("\033[93m {}\033[00m" .format(string))

def display_results(tests_total: tuple) -> None:
    if tests_total[0] == tests_total[1]:
        print_in_color(f'\n\nTotal success: ({tests_total[0]}/{tests_total[1]})\n', 'green')
    else:
        print_in_color(f'\n\nTotal success: ({tests_total[0]}/{tests_total[1]})\n', 'red')

# Resolution
def verify_exercises() -> tuple:
    tests_total: int = 0
    tests_succeded: int = 0
    for f in range(13):
        if path.exists(f'air{f:02d}.py'):
            tests_by_file = tests.count_numbers_of(f)
            for test in range(1, tests_by_file + 1):
                input_test, output_test = tests.generate_results(f, test)
                result = subprocess.run(["python3",f'air{f:02d}.py'] + input_test,
                                            capture_output=True, text=True)
                if result.stdout == output_test:
                    print_in_color(f'air{f:02d} ({test}/{tests_by_file}) : success', 'green')
                    tests_succeded += 1
                else:
                    print_in_color(f'air{f:02d} ({test}/{tests_by_file}) : failure', 'red')
                tests_total += 1
        else:
            print_in_color(f'air{f:02d}.py doesn\'t exist', 'yellow')
    return (tests_succeded, tests_total)

# Display
display_results(verify_exercises())
