"""
--- Day 9: Mirage Maintenance ---
"""

import os


def gen_next_sequence(numbers):
    """Generate the next sequence"""
    new_list = []
    for a, b in zip(numbers, numbers[1:]):
        new_list.append(b - a)

    if all([number == 0 for number in numbers]):
        return 0
    return numbers[-1] + gen_next_sequence(new_list)


def part_one():
    """--- Part One ---"""

    # Import the input
    file_name = os.path.basename(__file__).split(".")[0]
    with open(f"{file_name}_input.txt", encoding="utf-8") as f:
        lines = f.readlines()
    lines = [line.rstrip("\n") for line in lines]

    result = 0
    for line in lines:
        numbers = line.split(" ")
        numbers = [int(number) for number in numbers]
        result += gen_next_sequence(numbers)

    print(result)


def part_two():
    """--- Part Two ---"""

    # Import the input
    file_name = os.path.basename(__file__).split(".")[0]
    with open(f"{file_name}_input.txt", encoding="utf-8") as f:
        lines = f.readlines()
    lines = [line.rstrip("\n") for line in lines]

    result = 0
    for line in lines:
        numbers = line.split(" ")
        numbers = [int(number) for number in numbers]
        numbers = numbers[::-1]
        result += gen_next_sequence(numbers)

    print(result)


def main():
    """Main"""

    day = "--- Day 9: Mirage Maintenance ---"
    print("-" * len(day))
    print(day)
    print("-" * len(day))

    print("--- Part One ---")
    part_one()

    print("--- Part Two ---")
    part_two()


if __name__ == "__main__":
    main()
