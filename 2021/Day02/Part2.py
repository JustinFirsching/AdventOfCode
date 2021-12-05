#!/usr/bin/env python3
import re
import sys

input_file = sys.argv[1]


def match_regex(string: str):
    match = re.match(r"(?P<direction>\w+) (?P<magnitude>\d+)", string)
    return (match.group("direction"), int(match.group("magnitude")))


with open(input_file, "r") as f:
    directions = f.read().splitlines()

horizontal_pos, depth, aim = 0, 0, 0

for (direction, num) in map(match_regex, directions):
    if direction == "forward":
        horizontal_pos += num
        depth += aim * num
    elif direction == "down":
        aim += num
    elif direction == "up":
        aim -= num

print(horizontal_pos * depth)
