def count_numbers_of(air: int) -> int:
    if air == 0:
        return 3
    if air == 1:
        return 2
    if air == 2:
        return 2
    if air == 3:
        return 2
    if air == 4:
        return 2
    if air == 5:
        return 2
    if air == 6:
        return 2
    if air == 7:
        return 2
    if air == 8:
        return 2
    if air == 9:
        return 1
    if air == 10:
        return 1
    if air == 11:
        return 1
    if air == 12:
        return 1


def generate_results(air: int, test: int) -> tuple:
    if (air == 0 and test == 1):
        return ("Bonjour les gars", "Bonjour\nles\ngars\n")
    if (air == 0 and test == 2):
        return ("All is good    000", "All\nis\ngood\n000\n")
    if (air == 0 and test == 3):
        return ("Quoique,hmm", "Quoique,hmm_\n")
    if (air == 1 and test == 1):
        return ("Crevette magique dans la mer des étoiles" "la", "Crevette magique dans\n mer des étoiles\n")
    if (air == 1 and test == 2):
        return ("You bdon'tbknowbmy  bbname" "b", "You \ndon't\nknow\nmy  \nname\n")
    if (air == 2 and test == 1):
        return ("je" "teste" "des" "trucs" " ", "je teste des trucs\n")
    if (air == 2 and test == 2):
        return ("overnight celebrity" " slow jamz" " make a movie" " hope" ",", "overnight celebrity, slow jamz, make a movie, hope\n")
    if (air == 3 and test == 1):
        return ("bonjour monsieur bonjour", "monsieur\n")
    if (air == 3 and test == 2):
        return ("1 2 3 4 5 4 3 2 1", "5\n")
    if (air == 4 and test == 1):
        return ("Hello milady,   bien ou quoi ??", "Helo milady, bien ou quoi ?\n")
    if (air == 4 and test == 2):
        return ("Quelllle fffffoliie,,,,, laa   vie", "Quele folie, la vie\n")
    if (air == 5 and test == 1):
        return ("1 2 3 4 5 +2", "3 4 5 6 7\n")
    if (air == 5 and test == 2):
        return ("10 11 12 20 -5", "5 6 7 15\n")
    if (air == 6 and test == 1):
        return ("Michel Albert Thérèse Benoit t", "Michel\n")
    if (air == 6 and test == 2):
        return ("Michel Albert Thérèse Benoit a", "Michel, Thérèse, Benoit\n")
    if (air == 7 and test == 1):
        return ("1 3 4 2", "1 2 3 4\n")
    if (air == 7 and test == 2):
        return ("10 20 30 40 50 60 70 90 33", "10 20 30 33 40 50 60 70 90\n")
    if (air == 8 and test == 1):
        return ("10 20 30 fusion 15 25 35", "10 15 20 25 30 35\n")
    if (air == 8 and test == 2):
        return ("28 34 75 93 390 485 fusion 1 6 38 40 84 209", "1 6 28 34 38 40 75 84 93 209 390 485\n")
    if (air == 9 and test == 1):
        return ("Michel Albert Thérèse Benoit", "Albert, Thérèse, Benoit, Michel\n")
    if (air == 10 and test == 1):
        return ("a.txt", "Je danse le mia\n")
    if (air == 11 and test == 1):
        return ("O 5", "    O    \n   OOO   \n  OOOOO  \n OOOOOOO \nOOOOOOOOO\n")
    if (air == 12 and test == 1):
        return ("6 5 4 3 2 1", "1 2 3 4 5 6\n")
