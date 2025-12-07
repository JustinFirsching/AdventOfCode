# Sat Dec  6 08:36:27 PM EST 2025

# read a grid
from typing import Dict, Tuple


with open(0) as f:
    data = f.read().splitlines()

MAX_SURROUNDING = 4

COLS = len(data[0])
ROWS = len(data)

grid = {}
for y, row in enumerate(data):
    for x, val in enumerate(row):
        grid[(x, y)] = val


ALL_DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

p1 = 0
for x in range(COLS):
    for y in range(ROWS):
        if grid[(x, y)] != "@":
            continue

        surrounding = 0
        for dx, dy in ALL_DIRECTIONS:
            _x = x + dx
            _y = y + dy
            if 0 <= _x < COLS and 0 <= _y < ROWS:
                surrounding += grid[(_x, _y)] == "@"
        if surrounding < MAX_SURROUNDING:
            p1 += 1

print(p1)

# Sat Dec  6 08:44:11 PM EST 2025
# Refactored P1 into a count() method

def count():
    removed = []
    for x in range(COLS):
        for y in range(ROWS):
            if grid[(x, y)] != "@":
                continue

            surrounding = 0
            for dx, dy in ALL_DIRECTIONS:
                _x = x + dx
                _y = y + dy
                if 0 <= _x < COLS and 0 <= _y < ROWS:
                    surrounding += grid[(_x, _y)] == "@"
            if surrounding < MAX_SURROUNDING:
                removed.append((x, y))
    for pos in removed:
        grid[pos] = "x"

    return len(removed)

p2 = 0
while (removed := count()) > 0:
    p2 += removed
print(p2)

# Sat Dec  6 08:49:08 PM EST 2025
