#!/usr/bin/env python3

import sys
from typing import Dict, Tuple, List

"""
SIGNALS = [
    "cf",       # 1

    "acf",      # 7

    "bcdf",     # 4

    "abdfg",    # 5
    "acdeg",    # 2
    "acdfg",    # 3

    "abcefg",   # 0
    "abdefg",   # 6
    "abcdfg"    # 9

    "abcdefg",  # 8
]
"""

SIGNALS = [
    "abcefg",   # 0
    "cf",       # 1
    "acdeg",    # 2
    "acdfg",    # 3
    "bcdf",     # 4
    "abdfg",    # 5
    "abdefg",   # 6
    "acf",      # 7
    "abcdefg",  # 8
    "abcdfg"    # 9
]


def read_input(filepath: str) -> Tuple[List[str], List[str]]:
    with open(filepath, "r") as f:
        lines = f.read().splitlines()
    signals, ans = [], []
    for line in lines:
        s, a = line.split("|")
        signals.extend(s.split())
        ans.extend(a.split())
    return signals, ans


def count_1478(data: List[int]) -> Dict[str, str]:
    lengths = list(map(len, data))
    one_appears = lengths.count(len(SIGNALS[1]))
    four_appears = lengths.count(len(SIGNALS[4]))
    seven_appears = lengths.count(len(SIGNALS[7]))
    eight_appears = lengths.count(len(SIGNALS[8]))
    return {
        1: one_appears,
        4: four_appears,
        7: seven_appears,
        8: eight_appears
    }


def main():
    signals, output = read_input(sys.argv[1])
    print(sum(count_1478(output).values()))


if __name__ == "__main__":
    main()
