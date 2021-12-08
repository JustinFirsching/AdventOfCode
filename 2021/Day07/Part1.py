#!/usr/bin/env python3

# Like yesterday's problem, the individual positions don't matter. Just the
# number of crab submarines at each position

import sys
from typing import Callable, List, Tuple


def read_data(filepath: str) -> Tuple[int, int, List[int]]:
    with open(filepath, "r") as f:
        positions = list(map(int, f.read().split(",")))
    min_pos = min(positions)
    max_pos = max(positions)
    pos_counts = [positions.count(x) for x in range(min_pos, max_pos + 1)]
    return min_pos, pos_counts


def calculate_cost(
    target_position: int,
    data_min: int,
    data: List[int]
) -> int:
    cost = 0
    for (pos, count) in enumerate(data):
        individual_cost = abs(pos + data_min - target_position)
        cost += individual_cost * count
    return cost


def log_search(
    data: List[int],
    eval_func: Callable[[int, int, int, List[int]], int],
    l_offset: int = 0
) -> Tuple[int, int]:
    left, right = l_offset, l_offset + len(data) - 1

    while left < right:
        l_val = eval_func(left, l_offset, data)
        r_val = eval_func(right, l_offset, data)
        middle = (right + left) // 2
        if l_val < r_val:
            right = middle - 1
        else:
            left = middle + 1
    return left, eval_func(left, l_offset, data)


def brute_force_search(
    data: List[int],
    eval_func: Callable[[int, int, int, List[int]], int],
    l_offset: int = 0
) -> Tuple[int, int]:
    min_pos, min_cost = 0, float('inf')
    for pos in range(l_offset, len(data) + l_offset):
        val = eval_func(pos, l_offset, data)
        if val < min_cost:
            min_pos = pos
            min_cost = val
    return min_pos, min_cost


def main():
    min_crab_pos, crab_counts = read_data(sys.argv[1])
    optimal_pos, optimal_cost = log_search(
        crab_counts,
        calculate_cost,
        min_crab_pos
    )
    print(f"The optimal position is {optimal_pos} with cost {optimal_cost}")


if __name__ == "__main__":
    main()
