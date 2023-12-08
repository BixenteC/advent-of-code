"""
--- Day 6: Wait For It ---
"""

import os
import math


def part_one():
    """--- Part Two ---"""

    file_name = os.path.basename(__file__).split(".")[0]
    with open(f"{file_name}_input.txt", encoding="utf-8") as f:
        lines = f.readlines()
    lines = [line.rstrip("\n") for line in lines]

    times = lines[0].split(":")[1].split()
    records = lines[1].split(":")[1].split()
    times = [int(time) for time in times]
    records = [int(record) for record in records]

    result = 1
    for time, record in zip(times, records):
        count = 0
        for option in list(range(0, time + 1)):
            dist = option * (time - option)

            if dist > record:
                count += 1

        result *= count
    print(result)


def part_two():
    """--- Part Two ---"""

    file_name = os.path.basename(__file__).split(".")[0]
    with open(f"{file_name}_input.txt", encoding="utf-8") as f:
        lines = f.readlines()
    lines = [line.rstrip("\n") for line in lines]

    time = int(lines[0].split(":")[1].replace(" ", ""))
    record = int(lines[1].split(":")[1].replace(" ", ""))

    discriminant = pow(time, 2) - 4 * (-1) * (-record)

    zeros = [
        (-time + math.sqrt(discriminant)) / (2 * -1),
        (-time - math.sqrt(discriminant)) / (2 * -1),
    ]
    winning = [math.ceil(zeros[0]), math.floor(zeros[1])]
    print(winning[1] - winning[0] + 1)


def main():
    """Main"""

    day = "--- Day 6: Wait For It ---"
    print("-" * len(day))
    print(day)
    print("-" * len(day))

    print("--- Part One ---")
    part_one()

    print("--- Part Two ---")
    part_two()


if __name__ == "__main__":
    main()
