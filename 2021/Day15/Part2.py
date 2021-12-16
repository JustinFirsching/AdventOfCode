#!/usr/bin/env python3

import sys
from typing import Dict, List, Tuple

from heapq import heappop, heappush

from Part1 import display, get_neighbor_coords, get_path_from_last_coords


def get_repeat_offsets(
    repeats: int
) -> Tuple[int, int]:
    for i in range(repeats):
        for j in range(repeats):
            yield i, j


def read_data(filepath: str, repeat: int) -> Dict[Tuple[int, int], int]:
    with open(filepath, "r") as f:
        raw_data = f.read().splitlines()
    height = len(raw_data)
    width = len(raw_data[0])
    map = {}
    for y in range(height):
        for x in range(width):
            risk = int(raw_data[y][x])
            for x_o, y_o in get_repeat_offsets(repeat):
                new_risk = (risk + x_o + y_o - 1) % 9 + 1
                map[(x + (x_o * width), y + (y_o * height))] = new_risk
    return map


def find_path_cost(
    start: Tuple[int, int],
    end: Tuple[int, int],
    map: Dict[Tuple[int, int], int]
) -> Tuple[int, List[Tuple[int, int]]]:
    shortest = {start: 0}
    coord_heap = [start]
    last_coord = {start: None}
    while coord_heap:
        coord = heappop(coord_heap)
        for neighbor in get_neighbor_coords(*coord):
            if neighbor not in map:
                continue
            this_dist = shortest[coord] + map[neighbor]
            neighbor_not_checked = neighbor not in shortest.keys()
            if neighbor_not_checked or this_dist < shortest[neighbor]:
                heappush(coord_heap, neighbor)
                shortest[neighbor] = this_dist
                last_coord[neighbor] = coord

    return shortest[end], get_path_from_last_coords(end, last_coord)


def main():
    map = read_data(sys.argv[1], int(sys.argv[2]))
    target = max(map.keys())
    cost, path = find_path_cost((0, 0), target, map)
    display(path, map)
    print(f"This path will cost: {cost}")


if __name__ == "__main__":
    main()
