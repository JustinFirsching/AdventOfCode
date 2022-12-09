#!/usr/bin/env python3

import numpy as np

with open("input.txt") as f:
    arr = list(map(list, f.read().splitlines()))


arr = np.asarray(arr, dtype=int)
height, width = arr.shape
visible = np.ones((height, width))

print(arr)
for y in range(1, height - 1):
    for x in range(1, width - 1):
        val = arr[y, x]

        above = arr[:y, x]
        below = arr[y+1:, x]
        left = arr[y, :x]
        right = arr[y, x+1:]

        vis_above = val > (above.max() if above.size != 0 else -1)
        vis_below = val > (below.max() if below.size != 0 else -1)
        vis_left = val > (left.max() if left.size != 0 else -1)
        vis_right = val > (right.max() if right.size != 0 else -1)

        visible[y][x] = vis_above or vis_below or vis_left or vis_right

print(visible.flatten().sum())

scenic_score = np.zeros((height, width))
for y in range(1, height - 1):
    for x in range(1, width - 1):
        val = arr[y, x]

        # Count left
        for d_left in range(x - 1, -1, -1):
            if arr[y, d_left] >= val:
                break
        vis_left = x - d_left

        # Count right
        for d_right in range(x + 1, width):
            if arr[y, d_right] >= val:
                break
        vis_right = d_right - x

        # Count up
        for d_up in range(y - 1, -1, -1):
            if arr[d_up, x] >= val:
                break
        vis_above = y - d_up

        # Count down
        for d_down in range(y + 1, height):
            if arr[d_down, x] >= val:
                break
        vis_below = d_down - y

        scenic_score[y, x] = vis_above * vis_below * vis_left * vis_right

print(scenic_score.max())
