#!/usr/bin/env python3

import re

from copy import deepcopy
from collections import defaultdict
from typing import Tuple, List, DefaultDict


def read_data(path: str) -> Tuple[
    DefaultDict[int, List[int]],
    List[Tuple[int, int, int]]
]:
    with open(path) as f:
        data = f.read().splitlines()

    # Read the stacks first
    input_stack = []
    while data:
        # Do this so we only need to iterate through the input once
        line = data.pop(0)
        if re.match(r"(?: \d+ )+", line):
            break
        points = re.findall(r"[ \[]([ A-Z])[ \]] ?", line)
        input_stack.append(points)
    # Pop away the blank line
    data.pop(0)

    # Organize the data so it is usable
    stack = defaultdict(list)
    for s in input_stack:
        for i, cargo in enumerate(s, 1):
            if cargo != " ":
                stack[i].insert(0, cargo)

    # Parse the instructions
    instructions = []
    for instruction in data:
        pat = re.compile(r"^move (\d+) from (\d+) to (\d+)$")
        m, s, t = pat.findall(instruction)[0]
        instructions.append((
            int(m),
            int(s),
            int(t)
        ))

    return (stack, instructions)


def part1(stacks, instructions):
    for cnt, src, tgt in instructions:
        for i in range(cnt):
            # Take from the source
            to_move = stacks[src].pop()
            # Move to the target
            stacks[tgt].append(to_move)

    return stacks


def part2(stacks, instructions):
    for cnt, src, tgt in instructions:
        # Take from the source
        to_move = stacks[src][-cnt:]
        stacks[src] = stacks[src][:-cnt]

        # Add to the target
        stacks[tgt].extend(to_move)

    return stacks


def display_top(stacks):
    for i in range(1, max(stacks.keys()) + 1):
        top = stacks[i][-1]
        if top:
            print(top, end="")
    print()


def main():
    stacks, instructions = read_data("input.txt")

    p1_stacks = part1(deepcopy(stacks), instructions)
    display_top(p1_stacks)

    p2_stacks = part2(deepcopy(stacks), instructions)
    display_top(p2_stacks)


if __name__ == "__main__":
    main()
