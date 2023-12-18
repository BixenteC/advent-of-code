"""
"""

import os


def part_one():
    """--- Part One ---"""

    # Import the input
    file_name = os.path.basename(__file__).split(".")[0]
    with open(f"{file_name}_input.txt", encoding="utf-8") as f:
        lines = f.readlines()
    lines = [line.rstrip("\n") for line in lines]


def part_two():
    """--- Part Two ---"""
    pass


def main():
    """Main"""

    day = ""
    print("-" * len(day))
    print(day)
    print("-" * len(day))

    print("--- Part One ---")
    part_one()

    print("--- Part Two ---")
    part_two()


if __name__ == "__main__":
    main()
