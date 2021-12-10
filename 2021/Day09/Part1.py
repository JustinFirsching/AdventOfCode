#!/usr/bin/env python3

import sys
from typing import Tuple, List


def read_data(filepath: str) -> List[List[int]]:
    with open(filepath, "r") as f:
        rows = f.read().splitlines()
    str_matrix = list(map(list, rows))
    return [list(map(int, row)) for row in str_matrix]


# Diagonals don't count
def find_minimums(data: List[List[int]]) -> List[Tuple[int, int]]:
    height = len(data)
    width = len(data[0])
    data_t = list(map(list, zip(*data)))
    minimums = []
    for y in range(height):
        for x in range(width):
            this_val = data[y][x]

            row_start = max(0, y - 1)
            row_end = min(height - 1, y + 1)
            row = data_t[x][row_start: row_end + 1]

            col_start = max(0, x - 1)
            col_end = min(width - 1, x + 1)
            col = data[y][col_start: col_end + 1]

            considered_data = row + col
            this_is_min = this_val == min(considered_data)
            this_exists_once = considered_data.count(this_val) == 2
            if this_is_min and this_exists_once:
                minimums.append((x, y))

    return minimums


def calculate_score(data: List[List[int]], minimums: List[Tuple[int, int]]):
    score = 0
    for x, y in minimums:
        score += data[y][x] + 1
    return score


def main():
    data = read_data(sys.argv[1])
    minimums = find_minimums(data)
    risk_levels = calculate_score(data, minimums)
    print(risk_levels)


if __name__ == "__main__":
    main()
