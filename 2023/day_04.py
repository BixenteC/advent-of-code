"""
--- Day 4: Scratchcards ---
"""

import os


def part_one():
    """--- Part Two ---"""

    file_name = os.path.basename(__file__).split(".")[0]
    with open(f"{file_name}_input.txt", encoding="utf-8") as f:
        lines = f.readlines()
    lines = [line.rstrip("\n") for line in lines]

    points = 0
    for line in lines:
        left, right = line.split("|")
        left = left.split(":")[1]
        left = [int(number) for number in left.split(" ") if number != ""]
        right = [int(number) for number in right.split(" ") if number != ""]

        winning = len([number for number in right if number in left])
        points += pow(2, winning - 1) if winning > 0 else 0

    print(points)


def part_two():
    """--- Part Two ---"""

    file_name = os.path.basename(__file__).split(".")[0]
    with open(f"{file_name}_input.txt", encoding="utf-8") as f:
        lines = f.readlines()
    lines = [line.rstrip("\n") for line in lines]

    copies = {}
    for i, _ in enumerate(lines):
        copies[i + 1] = 1

    for line_number, line in enumerate(lines):
        left, right = line.split("|")
        left = left.split(":")[1]
        left = [int(number) for number in left.split(" ") if number != ""]
        right = [int(number) for number in right.split(" ") if number != ""]

        winning = len([number for number in right if number in left])

        for i in range(1, winning + 1):
            copies[line_number + 1 + i] += copies[line_number + 1]

    print(sum(copies.values()))


def main():
    """Main"""

    day = "--- Day 4: Scratchcards ---"
    print("-" * len(day))
    print(day)
    print("-" * len(day))

    print("--- Part One ---")
    part_one()

    print("--- Part Two ---")
    part_two()


if __name__ == "__main__":
    main()
