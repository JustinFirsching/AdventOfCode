#!/usr/bin/env python3
import sys

datafile = sys.argv[1]

with open(datafile, "r") as f:
    lines = f.read().splitlines()

data = list(map(int, lines))

counter = 0
for last, current in zip(data[:-1], data[1:]):
    if current > last:
        counter += 1

print(counter)
