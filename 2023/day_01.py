"""
--- Day 1: Trebuchet?! ---
"""

import re


def part_one():
    """--- Part One ---"""

    with open("day_01_input.txt", encoding="utf-8") as f:
        lines = f.readlines()

    sum_cal_vals = 0
    for line in lines:
        numbers = re.sub("[^0-9]", "", line)
        calibration_val = f"{numbers[0]}{numbers[-1]}"
        sum_cal_vals += int(calibration_val)

    print("Sum: ", sum_cal_vals)


def part_two():
    """--- Part Two ---"""

    with open("day_01_input.txt", encoding="utf-8") as f:
        lines = f.readlines()

    numbers_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    sum_cal_vals = 0
    for line in lines:
        numbers = ""
        for i, s in enumerate(line):
            if s.isdigit():
                numbers += s
            else:
                for number_word, number in numbers_dict.items():
                    if number_word in line[i:] and line[i:].index(number_word) == 0:
                        numbers += str(number)

        calibration_val = f"{numbers[0]}{numbers[-1]}"
        sum_cal_vals += int(calibration_val)

    print("Sum: ", sum_cal_vals)


def main():
    """Main"""

    day = "--- Day 1: Trebuchet?! ---"
    print("-" * len(day))
    print(day)
    print("-" * len(day))

    print("--- Part One ---")
    part_one()

    print("--- Part Two ---")
    part_two()


if __name__ == "__main__":
    main()
