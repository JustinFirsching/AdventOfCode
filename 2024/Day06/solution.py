# Started: 12/06/2024 09:05 PM
# Part 1 Submitted: 12/06/2024 09:26 PM
# Part 2 Submitted: 12/06/2024 10:10 PM
#
# Notes:
#   Part 2 was a disaster. I wanted to try to triangulate, but then I realized
#   I could triangulate to something that isn't traversed or isn't traversed in
#   the right direction. Then I figured I'd go just on what I had seen before,
#   but that obviously doesn't work since some tiles are already used twice.
#   Then I figured I could try assuming that the next thing was a tile in my
#   initial traverse loop, and if I already visited the tile in that same
#   direction, then it loops. This is true, but it doesn't account for paths
#   that would eventually lead to a re-visit in the same direction. I was about
#   to try brute-forcing with every available tile, but obviously that would
#   take forever to run with Advent of Code input size. Finally, I checked some
#   high submission on GitHub, specifically evanphoward's solution below.
#   https://github.com/evanphoward/AdventOfCode/blob/main/AOC_24/Day6/main.py
#   At first I didn't understand how he was able to use only the coordinates
#   that were visited rather than every coordinate in the grid. Eventually I
#   realized that it is because the obstacle would need to be placed in front
#   of the guard, which means that in the initial state, it was not in front
#   of the guard. If it was not in front of the guard, and in the path of
#   the guard, then we **must** have visited it before. With the reduced space
#   I was able to implement the correct solution by just simulating a traversal
#   of the grid with an obstacle in the position that would've otherwise been
#   traveled. If we hit a coordinate that we already traveled to, then we know
#   we have a loop.

import sys

input = open(sys.argv[1]).readlines()

# Part 1
grid = list(map(lambda x: list(x.strip()), input))
guard_coords = None
for i, row in enumerate(grid):
    for j, val in enumerate(row):
        if val == "^":
            guard_coords = (i, j)

assert(guard_coords)

gy, gx = guard_coords
direction = 0 # Use 0 for up
while gy >= 0 and gy < len(grid) and gx >= 0 and gx < len(grid[0]):
    grid[gy][gx] = "X"

    next_gx = gx + [0, 1, 0, -1][direction]
    next_gy = gy + [-1, 0, 1, 0][direction]
    if next_gy < 0 or next_gy >= len(grid) or next_gx < 0 or next_gx >= len(grid[0]):
        break

    if grid[next_gy][next_gx] == "#":
        direction = (direction + 1) % 4
    else:
        gx, gy = next_gx, next_gy

for row in grid:
    print("".join(row))
print("".join(["".join(row) for row in grid]).count("X"))

# Part 2

visits = set()
for i, row in enumerate(grid):
    for j, val in enumerate(row):
        if val == "X":
            visits.add((i, j))

def check_loops(grid) -> bool:
    assert(guard_coords)
    gy, gx = guard_coords

    seen = set()

    direction = 0
    while gy >= 0 and gy < len(grid) and gx >= 0 and gx < len(grid[0]):
        grid[gy][gx] = "X"
        if (gy, gx, direction) in seen:
            return True
        seen.add((gy, gx, direction))

        next_gx = gx + [0, 1, 0, -1][direction]
        next_gy = gy + [-1, 0, 1, 0][direction]
        if next_gy < 0 or next_gy >= len(grid) or next_gx < 0 or next_gx >= len(grid[0]):
            break

        if grid[next_gy][next_gx] == "#":
            direction = (direction + 1) % 4
        else:
            gx, gy = next_gx, next_gy
    return False

for i, row in enumerate(grid):
    for j, val in enumerate(row):
        if val == "X":
            visits.add((i, j))

obs = 0
for v in visits:
    if v == guard_coords:
        continue
    vy, vx = v
    grid[vy][vx] = "#"
    obs += check_loops(grid)
    grid[vy][vx] = "X"


print(obs)
