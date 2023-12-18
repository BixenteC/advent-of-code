"""
--- Day 8: Haunted Wasteland ---
"""

import os
from math import gcd


def part_one():
    """--- Part One ---"""

    # Import the input
    file_name = os.path.basename(__file__).split(".")[0]
    with open(f"{file_name}_input.txt", encoding="utf-8") as f:
        lines = f.readlines()
    lines = [line.rstrip("\n") for line in lines]

    instructions = lines[0]

    nodes = {}
    for line in lines[2:]:
        start, ends = [el.strip() for el in line.split("=")]
        ends = ends.replace("(", "")
        ends = ends.replace(")", "")
        ends = ends.replace(" ", "")
        ends = tuple(ends.split(","))
        nodes[start] = ends

    current = "AAA"
    count = 0
    while current != "ZZZ":
        for instruction in instructions:
            if instruction == "R":
                current = nodes[current][1]
            else:
                current = nodes[current][0]

            count += 1

    print(count)


def part_two():
    """--- Part Two ---"""

    # Import the input
    file_name = os.path.basename(__file__).split(".")[0]
    with open(f"{file_name}_input.txt", encoding="utf-8") as f:
        lines = f.readlines()
    lines = [line.rstrip("\n") for line in lines]

    instructions = lines[0]

    nodes = {}
    for line in lines[2:]:
        start, ends = [el.strip() for el in line.split("=")]
        ends = ends.replace("(", "")
        ends = ends.replace(")", "")
        ends = ends.replace(" ", "")
        ends = tuple(ends.split(","))
        nodes[start] = ends

    starts = []
    for node in nodes:
        if node[-1] == "A":
            starts.append(node)

    cycles = []
    for current in starts:
        count = 0
        while current[-1] != "Z":
            for instruction in instructions:
                if instruction == "R":
                    current = nodes[current][1]
                else:
                    current = nodes[current][0]

                count += 1
        cycles.append(count)

    lcm = 1
    for i in cycles:
        lcm = lcm * i // gcd(lcm, i)

    print(lcm)


def main():
    """Main"""

    day = "--- Day 8: Haunted Wasteland ---"
    print("-" * len(day))
    print(day)
    print("-" * len(day))

    print("--- Part One ---")
    part_one()

    print("--- Part Two ---")
    part_two()


if __name__ == "__main__":
    main()
