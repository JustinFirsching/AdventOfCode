#!/usr/bin/env python3
import sys
from typing import List


pairs = {
    "[": "]",
    "{": "}",
    "(": ")",
    "<": ">"
}

scores = {
    "]": 57,
    "}": 1197,
    ")": 3,
    ">": 25137
}


def read_data(filepath: str) -> List[str]:
    with open(filepath, "r") as f:
        return f.read().splitlines()


def find_first_corruptions(data: List[str]) -> List[str]:
    corruptions = []
    for line in data:
        last_open = []
        for char in line:
            if char in pairs.keys():
                last_open.append(char)
            else:
                expected = last_open.pop()
                expected_match = pairs[expected]
                if expected_match != char:
                    corruptions.append(char)
                    break
    return corruptions


def main():
    lines = read_data(sys.argv[1])
    first_corruptions = find_first_corruptions(lines)
    print(sum(map(scores.get, first_corruptions)))


if __name__ == "__main__":
    main()
