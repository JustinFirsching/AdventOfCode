#!/usr/bin/env python3

import sys
from copy import deepcopy


data_file = "sample.txt" if len(sys.argv) == 1 else sys.argv[1]
with open(data_file) as f:
    paths = f.read().splitlines()

sand_source = (500, 0)

rocks = set()
max_y = 0
# sand moves down, then diag left, then diag right
for path in paths:
    coords = [list(map(int, p.split(","))) for p in path.split(" -> ")]
    for (x1, y1), (x2, y2) in zip(coords[:-1], coords[1:]):
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                rocks.add((x, y))
                max_y = max(max_y, y)


occupied = deepcopy(rocks)

# Part 1

sand_pos = sand_source
while True:
    x, y = sand_pos
    below = (x, y + 1)
    diag_left = (x - 1, y + 1)
    diag_right = (x + 1, y + 1)

    # We fell into the abyss
    if y > max_y:
        break

    if below not in occupied:
        sand_pos = below
    elif diag_left not in occupied:
        sand_pos = diag_left
    elif diag_right not in occupied:
        sand_pos = diag_right
    else:
        # Reset
        occupied.add(sand_pos)
        sand_pos = sand_source

print(len(occupied) - len(rocks))

# Part 2

floor_y = max_y + 2
occupied = deepcopy(rocks)

while True:
    x, y = sand_pos
    below = (x, y + 1)
    diag_left = (x - 1, y + 1)
    diag_right = (x + 1, y + 1)

    at_floor = below[1] == floor_y
    if below not in occupied and not at_floor:
        sand_pos = below
    elif diag_left not in occupied and not at_floor:
        sand_pos = diag_left
    elif diag_right not in occupied and not at_floor:
        sand_pos = diag_right
    else:
        # Reset
        occupied.add(sand_pos)
        # If we just occupied the sand source, break
        if sand_pos == sand_source:
            break
        sand_pos = sand_source

print(len(occupied) - len(rocks))
