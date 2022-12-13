#!/usr/bin/env python3

import sys
from typing import List

input = "sample.txt" if len(sys.argv) == 1 else sys.argv[1]

with open(input) as f:
    grid = list(map(list, f.read().splitlines()))


def find_letter(arr: List[List[str]], letter: str):
    h, w = len(arr), len(arr[0])
    for y in range(h):
        for x in range(w):
            if letter == arr[y][x]:
                return (x, y)
    return None


def find_all_letters(arr: List[List[str]], letter: str):
    h, w = len(arr), len(arr[0])
    for y in range(h):
        for x in range(w):
            if letter == arr[y][x]:
                yield (x, y)


height, width = len(grid), len(grid[0])
start = find_letter(grid, 'S')
end = find_letter(grid, 'E')
print(f"{start} -> {end}")

DIR = ((0, 1), (0, -1), (1, 0), (-1, 0))

# Part 1

seen = set(start)
visit = [(start, 0)]

while visit:
    coord, steps = visit.pop(0)
    cx, cy = coord

    val = grid[cy][cx]
    val = val if val != "S" else "a"

    if val == "E":
        print(steps)
        break

    for dx, dy in DIR:
        nx, ny = cx + dx, cy + dy
        if nx not in range(width) or ny not in range(height):
            continue
        if (nx, ny) in seen:
            continue

        n_val = grid[ny][nx]
        n_val = n_val if n_val != "E" else "z"
        within_one = ord(n_val) - ord(val) <= 1
        if within_one:
            visit.append(((nx, ny), steps + 1))
            seen.add((nx, ny))


# Part 2

shortest = float("inf")
grid[start[1]][start[0]] = "a"

for start in find_all_letters(grid, "a"):
    seen = set(start)
    visit = [(start, 0)]
    while visit:
        coord, steps = visit.pop(0)
        cx, cy = coord

        val = grid[cy][cx]
        val = val if val != "S" else "a"

        if val == "E":
            print(start, steps)
            shortest = min(steps, shortest)
            break

        for dx, dy in DIR:
            nx, ny = cx + dx, cy + dy
            if nx not in range(width) or ny not in range(height):
                continue
            if (nx, ny) in seen:
                continue

            n_val = grid[ny][nx]
            n_val = n_val if n_val != "E" else "z"
            within_one = ord(n_val) - ord(val) <= 1
            if within_one:
                visit.append(((nx, ny), steps + 1))
                seen.add((nx, ny))

print(shortest)


# This finds the shortest path to the end for _every_ spot
# seen = set()
# visit = [(end, 0)]
# shortest = [[float("inf")] * width for _ in range(height)]
# while(visit):
#     coord, steps = visit.pop(0)
#     cx, cy = coord
#     shortest[cy][cx] = steps
#
#     e = grid[cy][cx]
#     if e == "E":
#         e = "z"
#     elif e == "S":
#         e = "a"
#
#     for (dx, dy) in DIR:
#         nx, ny = cx + dx, cy + dy
#         if nx not in range(width) or ny not in range(height):
#             continue
#         if (nx, ny) in seen:
#             continue
#
#         potential = grid[cy + dy][cx + dx]
#         if potential == "E":
#             potential = "z"
#         elif potential == "S":
#             potential = "a"
#
#         within_one = ord(n_val) - ord(val) <= 1
#         if within_one:
#             visit.append(((cx + dx, cy + dy), steps + 1))
#             seen.add((nx, ny))
#
# for y in range(height):
#     for x in range(width):
#         val = shortest[y][x]
#         print("{:02d}".format(val), end=" ")
#     print()
#
# print(shortest[start[1]][start[0]])
