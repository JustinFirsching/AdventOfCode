#!/usr/bin/env python3

import sys
from typing import Tuple, List

from Part1 import read_data, find_minimums


# A function that can be called recursively that builds a list of coords
def backtrack(
    x: int,
    y: int,
    width: int,
    height: int,
    data: List[List[int]],
    last_val: int = None,
    basin: List[int] = []
) -> List[int]:
    left_x = max(0, x - 1)
    right_x = min(width - 1, x + 1)

    up_y = max(0, y - 1)
    down_y = min(height - 1, y + 1)

    new_val = data[y][x]
    coord_str = f"{x}, {y}"

    is_valid_height = last_val is None or last_val < new_val < 9
    is_not_duplicate = coord_str not in basin
    if is_valid_height and is_not_duplicate:
        # Center
        basin.append(coord_str)
        # Left
        basin = backtrack(left_x, y, width, height, data, new_val, basin)
        # Right
        basin = backtrack(right_x, y, width, height, data, new_val, basin)
        # Up
        basin = backtrack(x, up_y, width, height, data, new_val, basin)
        # Down
        basin = backtrack(x, down_y, width, height, data, new_val, basin)
    return basin


def find_basins(
    data: List[List[int]],
    minimums: List[Tuple[int, int]]
) -> List[List[Tuple[int, int]]]:
    basins = []
    height = len(data)
    width = len(data[0])
    for x, y in minimums:
        basin = backtrack(x, y, width, height, data, None, [])
        basins.append(basin)
    return basins


def main():
    data = read_data(sys.argv[1])
    minimums = find_minimums(data)
    basins = find_basins(data, minimums)

    top_3_basins = sorted(list(map(len, basins)), reverse=True)[:3]
    print(top_3_basins)
    print(top_3_basins[0] * top_3_basins[1] * top_3_basins[2])


if __name__ == "__main__":
    main()
