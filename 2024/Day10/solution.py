# Started: 12/10/2024 09:08 PM
# Part 1 Submitted: 12/10/2024 09:27 PM
# Part 2 Submitted: 12/10/2024 09:30 PM
#
# Notes:
#   After:
#     Pretty happy with this one. I had an issue with double counting on part 1
#     that held me up a little bit and a variable issue when I named the grid
#     height `height` and the height at a coordinate in the grid `height`.
#
#     I could optimize this a little with one return and casting to set() for
#     only the unique peaks, but again, happy with this.

import sys

input = open(sys.argv[1]).read().splitlines()

grid_w, grid_h = len(input[0]), len(input)

grid = {}
starts = []
for y, line in enumerate(input):
    for x, c in enumerate(line):
        grid[x, y] = int(c)
        if c == "0":
            starts.append((x, y))

# Search from each start point to as many 9s as we can reach
def search(pos) -> tuple[set, list]:
    x, y = pos
    height = grid[(x, y)]

    if grid[(x, y)] == 9:
        return set([(x, y)]), [(x, y)]

    peaks_p1 = set()
    peaks_p2 = []
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_x, new_y = x + dx, y + dy
        in_bounds_x = 0 <= new_x < grid_w
        in_bounds_y = 0 <= new_y < grid_h
        if in_bounds_x and in_bounds_y:
            new_height = grid[(new_x, new_y)]
            if new_height == height + 1:
                found_peaks = search((new_x, new_y))
                peaks_p1.update(found_peaks[0])
                peaks_p2.extend(found_peaks[1])

    return peaks_p1, peaks_p2

scores_p1 = 0
scores_p2 = 0
for start in starts:
    scores = search(start)
    scores_p1 += len(scores[0])
    scores_p2 += len(scores[1])

print(scores_p1)
print(scores_p2)
