#!/usr/bin/env python3

import math
import sys
from typing import Dict, List, Tuple

from Part1 import *


def did_all_flash(data: Dict[Tuple[int, int], int]) -> bool:
    return all(val == 0 for val in data.values())


def main():
    data = read_lines(sys.argv[1])
    display_data(data)
    flash_count = 0
    step_count = 0
    while not did_all_flash(data):
        data = dict(zip(
            data.keys(),
            list(map(lambda val: val + 1, data.values()))
        ))
        flashes = find_flashes(data)
        data, flashed_points = apply_flashes(data, flashes)
        flash_count += len(flashed_points)
        data = reset_flashed(data, flashed_points)

        step_count += 1
        print(f"After step {step_count}:")
        display_data(data)

    print(step_count)


if __name__ == "__main__":
    main()
