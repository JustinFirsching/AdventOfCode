#!/usr/bin/env python3

import math
import sys
from typing import Dict, List, Tuple


def read_lines(filepath: str) -> Dict[Tuple[int, int], int]:
    matrix = {}
    with open(filepath, "r") as f:
        rows = f.read().splitlines()
    for y, row in enumerate(rows):
        for x, energy in enumerate(row):
            matrix[(x, y)] = int(energy)
    return matrix


def find_flashes(
    data: Dict[Tuple[int, int], int]
) -> List[Tuple[int, int]]:
    return [coord for (coord, energy) in data.items() if energy > 9]


def get_neighbors(x: int, y: int) -> Tuple[int, int]:
    deltas = (
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    )
    for xd, yd in deltas:
        yield (x + xd, y + yd)


def display_data(data: Dict[Tuple[int, int], int]):
    width = height = int(math.sqrt(len(data)))
    for y in range(height):
        print("| ", end="")
        for x in range(width):
            energy = data[(x, y)]
            print(f"{energy:2d}", end=" ")
        print(" |")


def apply_flashes(
    data: Dict[Tuple[int, int], int],
    flashes: List[Tuple[int, int]]
) -> Tuple[Dict[Tuple[int, int], int], int]:
    flashes_done = []
    flashes_todo = flashes
    while flashes_todo:
        coord = flashes_todo.pop(0)
        neighbors = [neighbor for neighbor in get_neighbors(*coord)]
        for n_coord in neighbors:
            if n_coord not in data:
                continue
            data[n_coord] += 1
            energy = data[n_coord]
            if energy > 9 and n_coord not in flashes_todo + flashes_done:
                flashes_todo.append(n_coord)

        flashes_done.append(coord)

    return data, flashes_done


def reset_flashed(
    data: Dict[Tuple[int, int], int],
    reset_point: List[Tuple[int, int]]
) -> Dict[Tuple[int, int], int]:
    for reset in reset_point:
        data[reset] = 0
    return data


def main():
    data = read_lines(sys.argv[1])
    display_data(data)
    flash_count = 0
    for i in range(int(sys.argv[2])):
        data = dict(zip(
            data.keys(),
            list(map(lambda val: val + 1, data.values()))
        ))
        flashes = find_flashes(data)
        data, flashed_points = apply_flashes(data, flashes)
        flash_count += len(flashed_points)
        data = reset_flashed(data, flashed_points)
        print(f"After step {i + 1}:")
        display_data(data)

    print(flash_count)


if __name__ == "__main__":
    main()
