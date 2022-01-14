#!/usr/bin/env python3
from __future__ import annotations

import sys
import re
from typing import List, Tuple


def sign(number: int) -> int:
    return ((number > 0) - (number < 0))


class Target:
    def __init__(self, tl_corner: Tuple[int, int], br_corner: Tuple[int, int]):
        self.tl_corner = tl_corner
        self.br_corner = br_corner
        self.x_range = range(
            self.tl_corner[0],
            self.br_corner[0] + sign(self.br_corner[0]),
            sign(self.br_corner[0] - self.tl_corner[0])
        )
        self.y_range = range(
            self.tl_corner[1],
            self.br_corner[1] + sign(self.br_corner[1]),
            sign(self.br_corner[1] - self.tl_corner[1])
        )

    def __str__(self):
        return f"{self.tl_corner} to {self.br_corner}"

    def is_hit(self, coord: Tuple[int, int]) -> bool:
        return coord[0] in self.x_range and coord[1] in self.y_range

    def can_hit(self, coord: Tuple[int, int]) -> bool:
        return coord[0] <= self.br_corner[0] and \
                coord[1] >= self.br_corner[1]


class Probe:
    def __init__(self, velocity: Tuple[int, int]):
        self.x = 0
        self.y = 0
        self.dx, self.dy = velocity

    def __next__(self) -> Probe:
        self.step()
        return self

    def step(self):
        self.x += self.dx
        self.y += self.dy
        self.dx = (abs(self.dx) - 1) * sign(self.dx)
        self.dy -= 1


def find_x_velocities_that_drop(
    target_x_start: int,
    target_x_end: int
) -> List[int]:
    vel = 0
    x_at_vel = 0
    while x_at_vel < target_x_start:
        vel += 1
        x_at_vel += vel
    vels = [vel]
    while x_at_vel + (vel + 1) < target_x_end:
        vel += 1
        vels.append(vel)
    return vels


def read_data(filepath: str) -> Target:
    coord_pattern = r"(?P<dim>.)=(?P<start>-?\d+)..(?P<end>-?\d+)"
    with open(filepath, "r") as f:
        raw_data = f.read()
    matches = re.finditer(coord_pattern, raw_data)
    data = {}
    for match in matches:
        dim = match.group("dim")
        start = int(match.group("start"))
        end = int(match.group("end"))
        data[dim] = tuple(sorted((start, end), key=abs))
    return Target(*list(zip(data['x'], data['y'])))


def main():
    target = read_data(sys.argv[1])
    x_vels = find_x_velocities_that_drop(
        target.tl_corner[0],
        target.br_corner[0]
    )
    # Any x works as long as the drop is in range
    max_x_vel = min(x_vels)
    # Maximum y  position can be found based on how low on the board we hit
    max_y_vel = abs(target.br_corner[1]) - 1
    print(f"Initial velocity: ({max_x_vel}, {max_y_vel})")
    print(f"Maximum height: {sum(range(max_y_vel + 1))}")


if __name__ == "__main__":
    main()
