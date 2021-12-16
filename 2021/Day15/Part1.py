#!/usr/bin/env python3

import sys
from typing import Dict, List, Tuple


def read_data(filepath: str) -> Dict[Tuple[int, int], int]:
    with open(filepath, "r") as f:
        raw_data = f.read().splitlines()
    height = len(raw_data)
    width = len(raw_data[0])
    map = {}
    for y in range(height):
        for x in range(width):
            map[(int(x), int(y))] = int(raw_data[y][x])
    return map


def get_path_from_last_coords(
    endpoint: Tuple[int, int],
    last_coords: Dict[Tuple[int, int], Tuple[int, int]]
) -> List[Tuple[int, int]]:
    path = []
    while endpoint:
        path.insert(0, endpoint)
        endpoint = last_coords[endpoint]
    return path


def get_neighbor_coords(x: int, y: int) -> Tuple[int, int]:
    for xd, yd in ((1, 0), (-1, 0), (0, -1), (0, 1)):
        yield x + xd, y + yd


def find_path_cost(
    start: Tuple[int, int],
    end: Tuple[int, int],
    map: Dict[Tuple[int, int], int]
) -> Tuple[int, List[Tuple[int, int]]]:
    shortest = {start: 0}
    coord_todo = [start]
    last_coord = {start: None}
    while coord_todo:
        coord = coord_todo.pop(0)
        for neighbor in get_neighbor_coords(*coord):
            if neighbor not in map:
                continue
            this_dist = shortest[coord] + map[neighbor]
            neighbor_not_checked = neighbor not in coord_todo \
                + list(shortest.keys())
            if neighbor_not_checked or this_dist < shortest[neighbor]:
                coord_todo.append(neighbor)
                shortest[neighbor] = this_dist
                last_coord[neighbor] = coord
    return shortest[end], get_path_from_last_coords(end, last_coord)


def display(path: List[Tuple[int, int]], map: Dict[Tuple[int, int], int]):
    width, height = max(map)
    for y in range(height + 1):
        print("| ", end="")
        for x in range(width + 1):
            if (x, y) in path:
                printable = f"\033[01m\033[31m{map[(x, y)]}\033[0m"
            else:
                printable = str(map[(x, y)])
            print(printable, end="")
        print(" |")


def main():
    map = read_data(sys.argv[1])
    target = max(map.keys())
    cost, path = find_path_cost((0, 0), target, map)
    display(path, map)
    print(f"This path will cost: {cost}")


if __name__ == "__main__":
    main()
