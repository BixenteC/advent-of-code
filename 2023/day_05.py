"""
--- Day 5: If You Give A Seed A Fertilizer ---
"""

import os
from itertools import groupby


def create_mapping_dict(lines):
    """Gets the mappings from the part with the given name."""
    i = (list(g) for _, g in groupby(lines, key="".__ne__))
    splitted = [a + b for a, b in zip(i, i)]

    mappings = {}
    for i, current_mapping in enumerate(splitted[1:]):
        mappings[i] = current_mapping[1:-1]

    return mappings


def compute_map(seed, mapping_lines):
    """Computes the mapping"""
    seed = int(seed)
    for line in mapping_lines:
        numbers = line.split(" ")
        numbers = [int(number) for number in numbers]
        destination, source, nb_range = numbers

        if source <= seed <= source + nb_range:
            return destination + (seed - source)

    return int(seed)


def part_one():
    """--- Part Two ---"""
    file_name = os.path.basename(__file__).split(".")[0]
    with open(f"{file_name}_input.txt", encoding="utf-8") as f:
        lines = f.readlines()
    lines = [line.rstrip("\n") for line in lines]

    seeds = lines[0].split(":")[1].split(" ")
    seeds = [seed for seed in seeds if seed]
    mapping_dict = create_mapping_dict(lines)

    lowest = 1e10
    for seed in seeds:
        current = int(seed)
        for mapping in mapping_dict.values():
            current = compute_map(current, mapping)
        if current < lowest:
            lowest = current

    print(lowest)


def part_two():
    """--- Part Two ---"""
    file_name = os.path.basename(__file__).split(".")[0]
    with open(f"{file_name}_input.txt", encoding="utf-8") as f:
        lines = f.readlines()
    lines = [line.rstrip("\n") for line in lines]

    seed_ranges = lines[0].split(":")[1].split(" ")
    seed_ranges = [int(number) for number in seed_ranges if number]

    mapping_dict = create_mapping_dict(lines)

    lowest = 1e100
    lowest_seed = []
    for start, end in zip(seed_ranges[::2], seed_ranges[1::2]):
        for seed in (start, end):
            current = seed
            for mapping in mapping_dict.values():
                current = compute_map(current, mapping)
            if current < lowest:
                lowest = current
                lowest_seed = [start, end]

    lowest = 1e100

    for seed in range(lowest_seed[0], lowest_seed[0] + lowest_seed[1]):
        print(seed)
        current = seed
        for mapping in mapping_dict.values():
            current = compute_map(current, mapping)
        if current < lowest:
            lowest = current

    print(lowest_seed)
    print(lowest)


def main():
    """Main"""

    day = "--- Day 5: If You Give A Seed A Fertilizer ---"
    print("-" * len(day))
    print(day)
    print("-" * len(day))

    print("--- Part One ---")
    part_one()

    print("--- Part Two ---")
    part_two()


if __name__ == "__main__":
    main()
