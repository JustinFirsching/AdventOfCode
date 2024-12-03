#!/usr/bin/env python3

import sys
import re

from typing import Tuple

data_file = "sample.txt" if len(sys.argv) == 1 else sys.argv[1]
with open(data_file) as f:
    data = f.read().splitlines()

min_x = min_y = float('inf')
max_x = max_y = float('-inf')

beacons = []
sensors = []
for line in data:
    sensor, beacon = [tuple(map(int, coord))
                      for coord in re.findall(r"x=(-?\d+), y=(-?\d+)", line)]
    sensors.append(sensor)
    beacons.append(beacon)

    min_x = min(min_x, sensor[0], beacon[0])
    min_y = min(min_y, sensor[1], beacon[1])

    max_x = max(max_x, sensor[0], beacon[0])
    max_y = max(max_y, sensor[1], beacon[1])

"""
Visualization works, but man does it lag

width = max_x - min_x + 1
height = max_y - min_y + 1

grid = [["."] * width for _ in range(height)]

for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
        if (x, y) in beacons:
            grid[y - min_y][x - min_x] = "B"
        elif (x, y) in sensors:
            grid[y - min_y][x - min_x] = "S"
"""

"""
This is all in the input if I read the problem...

def dist(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    # Wrong distance...
    import math
    return int(math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2))


def nearest_beacon(coord: Tuple[int, int]) -> Tuple[int, int]:
    min_dist = float("inf")
    nearest_beacon = None
    for beacon in beacons:
        d = dist(coord, beacon)
        if min(min_dist, d) == d:
            min_dist = d
            nearest_beacon = beacon
    return nearest_beacon


for sensor in sensors:
    sx, sy = sensor
    b = nearest_beacon(sensor)
    d = dist(sensor, b)
    for dy in range(-d, d + 1):
        x_offset = d - abs(dy)
        for dx in range(-x_offset, x_offset + 1):
            target_x = sx + dx - min_x
            target_y = sy + dy - min_y

            invalid_x = target_x not in range(width)
            invalid_y = target_y not in range(height)
            if invalid_x or invalid_y:
                continue

            # Don't overwrite the sensors or beacons
            if grid[target_y][target_x] != ".":
                continue

            grid[target_y][target_x] = "#"

print()
for i, y in enumerate(range(height), min_y):
    print(f"{i}:\t", end="")

    for x in range(width):
        print(grid[y][x], end="")
    print()
print()
"""

print("".join(map(str, grid[10 - min_y])).count("#"))
