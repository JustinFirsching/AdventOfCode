#!/usr/bin/env python3

# Like yesterday's problem, the individual positions don't matter. Just the
# number of crab submarines at each position

import sys
from typing import List

from Part1 import read_data, brute_force_search


def calculate_cost(
    target_position: int,
    data_min: int,
    data: List[int]
) -> int:
    cost = 0
    for (pos, count) in enumerate(data):
        individual_cost = sum(
            [i + 1 for i in range(abs(pos + data_min - target_position))]
        )
        cost += individual_cost * count
    return cost


def main():
    min_crab_pos, crab_counts = read_data(sys.argv[1])
    # log_search won't work when the cost scales logarithmically
    optimal_pos, optimal_cost = brute_force_search(
        crab_counts,
        calculate_cost,
        min_crab_pos
    )
    print(f"The optimal position is {optimal_pos} with cost {optimal_cost}")


if __name__ == "__main__":
    main()
