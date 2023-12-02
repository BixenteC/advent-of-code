"""
--- Day 2: Cube Conundrum ---
"""

import re
from functools import reduce
from operator import mul

CONFIG = {
    "red": 12,
    "green": 13,
    "blue": 14 
}

"""
--- Part One ---
"""
def part_one():

    with open("day_02_input.txt") as f:
        lines = f.readlines()

    sum_IDs = 0
    for line in lines:
        game, substring = line.split(":")
        game_ID = game.split(" ")[1]
        splitted = re.split("; |,", substring)
        
        is_possible = True
        for grab in splitted:
            amount, color = grab.strip().split(" ")

            if int(amount) > CONFIG[color]:
                is_possible = False
                continue
        
        if is_possible:
            sum_IDs += int(game_ID)
        
    print(sum_IDs)


"""
--- Part Two ---
"""
def part_two():

    with open("day_02_input.txt") as f:
        lines = f.readlines()

    sum_powers = 0
    for line in lines:
        game, substring = line.split(":")
        game_ID = game.split(" ")[1]
        splitted = re.split("; |,", substring)

        current_game = {
            "red": 0,
            "green": 0,
            "blue": 0    
        }
        
        for grab in splitted:
            amount, color = grab.strip().split(" ")
            
            if int(amount) > current_game[color]:
                current_game[color] = int(amount)

        amounts = current_game.values()
        power = reduce(mul, amounts)
        sum_powers += power

    print(sum_powers)


def main():
    day = "--- Day 2: Cube Conundrum ---"
    print("-"*len(day))
    print(day)
    print("-"*len(day))

    print("--- Part One ---")
    part_one()

    print("--- Part Two ---")
    part_two()


if __name__ == "__main__":
    main()