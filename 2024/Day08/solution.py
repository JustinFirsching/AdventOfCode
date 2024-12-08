# Started: 12/08/2024 12:00 AM
# Part 1 Submitted: 12/08/2024 12:34 AM
# Part 2 Submitted: 12/08/2024 12:41 AM
#
# Notes:
#   Before:
#     Already up. May as well try this. Need to apply notes from pervious
#     problems. Think first. Then solve. Adjust base problem.
#   After:
#     Small hangup when I found out that "\n" is not stripped out by
#     `readlines()`. Switched to `.read().splitlines()` instead.
#
#     Got hung up checking for colinearity... any two points are colinear...
#
#     Part 2 went really smoothly once I figured out the colinearity bit. I did
#     lose a little time not including the second node itself, but a reread of
#     the instructions cleared that up.
#
#     When looking over [hyperneutrino](https://github.com/hyperneutrino)'s
#     solution I realized that that doing the math in both directions was
#     pointless. The iterators would hit the same point pair in the opposite
#     direction anyway.

import sys

input = open(sys.argv[1]).read().splitlines()

# Part 1

## Had a feeling this would be a grid problem. Going to try the grid
## implementation I saw by the better solvers. Calculating the antinodes seems
## like it will probably be brute force, which is insane. I should track the
## coordinates of each antenna node to make this easier.
##
## So the plan is:
##   1. Read the grid into a dictionary of coordinates.
##      1a. Track the locations of the antenna nodes
##   2. Find nodes that are in line with each other.
##   3. For each antenna of a given frequency in line with each other, we can
##      calculate the antinodes.

# Part 2

## Plan is to just build upon Part 1, but loop the distances from the point
## rather than just one step in each direction.

from typing import Tuple

antennas = {}
grid = {}
height, width = len(input), len(input[0])
for i, row in enumerate(input):
    for j, char in enumerate(row):
        grid[(i, j)] = char
        if char != '.':
            antennas[char] = antennas.get(char, set())
            antennas[char].add((i, j))

def dist(p1: Tuple[int, int], p2: Tuple[int, int]) -> Tuple[int, int]:
    return p2[0] - p1[0], p2[1] - p1[1]

antinode_coords_p1 = set()
antinode_coords_p2 = set()
for freq, nodes in antennas.items():
    nodes = list(nodes)
    for node1 in nodes:
        for node2 in nodes:
            if node1 == node2:
                continue
            # Inherently colinear and must be an antinode
            antinode_coords_p2.add(node2)

            # There is an antinode in the same direction, of the same distance
            # from the antenna as the antenna are from each other
            y_dist, x_dist = dist(node1, node2)

            # Part 1
            anti_a = (node1[0] - y_dist, node1[1] - x_dist)  # Move away from node 1
            anti_b = (node2[0] + y_dist, node2[1] + x_dist)  # Move away from node 2
            if 0 <= anti_a[0] < height and 0 <= anti_a[1] < width:
                antinode_coords_p1.add(anti_a)
            if 0 <= anti_b[0] < height and 0 <= anti_b[1] < width:
                antinode_coords_p1.add(anti_b)

            # Part 2
            ## Iterate away from the antenna until we hit the grid edge
            while 0 <= anti_a[0] < height and 0 <= anti_a[1] < width:
                antinode_coords_p2.add(anti_a)
                anti_a = (anti_a[0] - y_dist, anti_a[1] - x_dist)

            while 0 <= anti_b[0] < height and 0 <= anti_b[1] < width:
                antinode_coords_p2.add(anti_b)
                anti_b = (anti_b[0] + y_dist, anti_b[1] + x_dist)

for i, coord_dict in enumerate((antinode_coords_p1, antinode_coords_p2), 1):
    print(f"Part {i}")
    for i in range(height):
        for j in range(width):
            if (i, j) in coord_dict:
                print('#', end='')
            else:
                print(grid[(i, j)], end='')
        print()
    print()
    print()

print(f"Part 1: {len(antinode_coords_p1)}")
print(f"Part 2: {len(antinode_coords_p2)}")
