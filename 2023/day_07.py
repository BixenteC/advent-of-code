"""
--- Day 7: Camel Cards ---
"""

import os

CARDS = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
CARDS = CARDS[::-1]

CARDS_2 = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
CARDS_2 = CARDS[::-1]


def part_one():
    """--- Part Two ---"""

    def str_to_number(s):
        return [CARDS.index(card) for card in s]

    file_name = os.path.basename(__file__).split(".")[0]
    with open(f"{file_name}_input.txt", encoding="utf-8") as f:
        lines = f.readlines()
    lines = [line.rstrip("\n") for line in lines]

    sorted_types = {
        "high_card": [],
        "one_pair": [],
        "two_pair": [],
        "three_of_kind": [],
        "full_house": [],
        "four_of_kind": [],
        "five_of_kind": [],
    }
    for line in lines:
        hand, bid = line.split()
        bid = int(bid)

        hand_dict = {}
        for card in hand:
            hand_dict[card] = hand_dict.get(card, 0) + 1

        # Five of a kind
        if 5 in hand_dict.values():
            sorted_types["five_of_kind"].append((hand, bid))

        elif 4 in hand_dict.values():
            sorted_types["four_of_kind"].append((hand, bid))

        elif 3 in hand_dict.values() and 2 in hand_dict.values():
            sorted_types["full_house"].append((hand, bid))

        elif 3 in hand_dict.values():
            sorted_types["three_of_kind"].append((hand, bid))

        elif list(hand_dict.values()).count(2) == 2:
            sorted_types["two_pair"].append((hand, bid))

        elif 2 in hand_dict.values():
            sorted_types["one_pair"].append((hand, bid))

        else:
            sorted_types["high_card"].append((hand, bid))

    sorted_bids = []
    for type_bucket in sorted_types.values():
        if len(type_bucket) == 0:
            continue

        if len(type_bucket) == 1:
            sorted_bids.append(type_bucket[0][1])
        else:
            sorted_bucket = sorted(type_bucket, key=lambda x: str_to_number(x[0]))
            _, bids = zip(*sorted_bucket)
            sorted_bids.extend(bids)

    print(sum((bid * (i + 1) for i, bid in enumerate(sorted_bids))))


def part_two():
    """--- Part Two ---"""

    def str_to_number(s):
        return [CARDS_2.index(card) for card in s]

    file_name = os.path.basename(__file__).split(".")[0]
    with open(f"{file_name}_input.txt", encoding="utf-8") as f:
        lines = f.readlines()
    lines = [line.rstrip("\n") for line in lines]

    sorted_types = {
        "high_card": [],
        "one_pair": [],
        "two_pair": [],
        "three_of_kind": [],
        "full_house": [],
        "four_of_kind": [],
        "five_of_kind": [],
    }
    for line in lines:
        hand, bid = line.split()
        bid = int(bid)

        hand_dict = {}
        for card in hand:
            hand_dict[card] = hand_dict.get(card, 0) + 1

        copy = hand_dict.copy()
        if "J" in copy:
            copy["J"] = 0
            most_common = max(copy, key=copy.get)
            hand_dict[most_common] += hand_dict["J"]

        for card in hand_dict:
            if card != "J":
                hand_dict[card] += hand_dict.get("J", 0)

        if 5 in hand_dict.values():
            sorted_types["five_of_kind"].append((hand, bid))

        elif 4 in hand_dict.values():
            sorted_types["four_of_kind"].append((hand, bid))

        elif 3 in hand_dict.values() and 2 in hand_dict.values():
            sorted_types["full_house"].append((hand, bid))

        elif 3 in hand_dict.values():
            sorted_types["three_of_kind"].append((hand, bid))

        elif list(hand_dict.values()).count(2) == 2:
            sorted_types["two_pair"].append((hand, bid))

        elif 2 in hand_dict.values():
            sorted_types["one_pair"].append((hand, bid))

        else:
            sorted_types["high_card"].append((hand, bid))

    sorted_bids = []
    for type_bucket in sorted_types.values():
        if len(type_bucket) == 0:
            continue

        if len(type_bucket) == 1:
            sorted_bids.append(type_bucket[0][1])
        else:
            sorted_bucket = sorted(type_bucket, key=lambda x: str_to_number(x[0]))
            _, bids = zip(*sorted_bucket)
            sorted_bids.extend(bids)

    print(sum((bid * (i + 1) for i, bid in enumerate(sorted_bids))))


def main():
    """Main"""

    day = "--- Day 7: Camel Cards ---"
    print("-" * len(day))
    print(day)
    print("-" * len(day))

    print("--- Part One ---")
    part_one()

    print("--- Part Two ---")
    part_two()


if __name__ == "__main__":
    main()
