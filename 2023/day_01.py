"""
--- Day 1: Trebuchet?! ---
"""

import re

"""
--- Part One ---
"""
def part_one():

    with open("day_01_input.txt") as f:
        lines = f.readlines()

    sum_cal_vals = 0
    for line in lines:
        numbers = re.sub("[^0-9]", "", line)
        calibration_val = f"{numbers[0]}{numbers[-1]}"
        sum_cal_vals += int(calibration_val)

    print("Sum: ", sum_cal_vals) 


"""
--- Part Two ---
"""
def part_two():

    with open("day_01_input.txt") as f:
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
        "nine": 9
    }

    sum_cal_vals = 0
    for line in lines:
        
        numbers = ""
        for i in range(len(line)):
            if line[i].isdigit():
                numbers += line[i]
            else:
                for number in numbers_dict.keys():
                    if number in line[i:] and line[i:].index(number) == 0:
                        numbers += str(numbers_dict[number])
        
        calibration_val = f"{numbers[0]}{numbers[-1]}"
        sum_cal_vals += int(calibration_val)

    print("Sum: ", sum_cal_vals)           


def main():
    day = "--- Day 1: Trebuchet?! ---"
    print("-"*len(day))
    print(day)
    print("-"*len(day))
    print("--- Part One ---")
    part_one()
    print("--- Part Two ---")
    part_two()


if __name__ == "__main__":
    main()
