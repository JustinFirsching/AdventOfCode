#!/usr/bin/env python3

import argparse
import re
from typing import Optional

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input")
    return parser.parse_args()

def read_input(input_file):
    with open(input_file, "r") as f:
        return f.read().splitlines()

def extract_instruction(line: str) -> Optional[int]:
    first = re.match(r".*?(?P<first>\d).*", line)
    if first is None:
        print(f"Unable to find first in: {line}")
        return None

    last = re.match(r".*(?P<last>\d).*", line)
    if last is None:
        print(f"Unable to find last in: {line}")
        return None

    return int(f"{first.group('first')}{last.group('last')}")

def part1(input_file):
    answer = 0
    for line in read_input(input_file):
        instruction = extract_instruction(line)
        if instruction is None:
            continue

        answer += instruction
    return answer

def part2(input_file):
    def re_func(match: Optional[re.Match]) -> str:
        print(match)
        return ""

    nums = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    answer = 0
    for line in read_input(input_file):
        orig_line = line
        # substitute all spelled out words with their numeric value
        line = re.sub("|".join(nums.keys()), re_func, line)

        instruction = extract_instruction(line)
        if instruction is None:
            continue

        print(f"{orig_line} -> {line} -> {instruction}")

        answer += instruction
    return answer



def main():
    args = parse_args()

    p1 = part1(args.input)
    print(f"Part 1: {p1}")

    p2 = part2(args.input)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
