"""
--- Day 3: Gear Ratios ---
"""

import os
from functools import reduce
from operator import mul


def check_surroundings(idx_character, lines):
    """Checks if there is a character in the surrounding area"""

    i, j = idx_character
    rows = len(lines[0])
    cols = len(lines)

    surrounding_indices = [
        (x, y)
        for x in range(max(0, i - 1), min(rows, i + 2))
        for y in range(max(0, j - 1), min(cols, j + 2))
        if (x, y) != (i, j)
    ]

    for idx in surrounding_indices:
        i, j = idx
        if lines[i][j] != "." and not lines[i][j].isdigit():
            return True

    return False


def check_gears(idx_character, lines):
    """Checks if there is a character in the surrounding area"""

    i, j = idx_character
    rows = len(lines[0])
    cols = len(lines)

    surrounding_indices = [
        (x, y)
        for x in range(max(0, i - 1), min(rows, i + 2))
        for y in range(max(0, j - 1), min(cols, j + 2))
        if (x, y) != (i, j)
    ]

    for idx in surrounding_indices:
        i, j = idx
        if lines[i][j] == "*":
            return (i, j)

    return None


def part_one():
    """--- Part One ---"""

    file_name = os.path.basename(__file__).split(".")[0]
    with open(f"{file_name}_input.txt", encoding="utf-8") as f:
        lines = f.readlines()
    lines = [line.rstrip("\n") for line in lines]

    numbers = []
    for i, line in enumerate(lines):
        number = ""
        is_valid = False
        for j, s in enumerate(line):
            if s.isdigit():
                number += s
                is_valid = is_valid or check_surroundings((i, j), lines)
            if j == len(line) - 1 or not line[j + 1].isdigit():
                if is_valid:
                    numbers.append(int(number))
                number = ""
                is_valid = False

    print(sum(numbers))


def part_two():
    """--- Part Two ---"""

    file_name = os.path.basename(__file__).split(".")[0]
    with open(f"{file_name}_input.txt", encoding="utf-8") as f:
        lines = f.readlines()
    lines = [line.rstrip("\n") for line in lines]

    gears = {}
    for i, line in enumerate(lines):
        for j, _ in enumerate(line):
            gears[(i, j)] = []

    for i, line in enumerate(lines):
        number = ""
        is_valid = False
        gear_location = None
        for j, s in enumerate(line):
            if s.isdigit():
                number += s
                if check_gears((i, j), lines):
                    is_valid = True
                    gear_location = check_gears((i, j), lines)
            if j == len(line) - 1 or not line[j + 1].isdigit():
                if is_valid:
                    gears[gear_location].append(int(number))
                number = ""
                is_valid = False

    gears_filtered = {
        key: reduce(mul, value)
        for key, value in gears.items()
        if value and len(value) == 2
    }
    print(sum(gears_filtered.values()))


def main():
    """Main"""

    day = "--- Day 3: Gear Ratios ---"
    print("-" * len(day))
    print(day)
    print("-" * len(day))

    print("--- Part One ---")
    part_one()

    print("--- Part Two ---")
    part_two()


if __name__ == "__main__":
    main()
