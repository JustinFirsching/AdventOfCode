#!/usr/bin/env python3

from __future__ import annotations

import enum
import math
import sys
from typing import List, Tuple


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.coords = (x, y)

    def distance(self) -> int:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __gt__(self, other: Point) -> bool:
        return self.distance() > other.distance()

    def __eq__(self, other: Point) -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return self.x < 0xF | self.y & 0xFFFF

    def __str__(self) -> str:
        return f"{self.x}, {self.y}"

    @staticmethod
    def from_string(string: str) -> Point:
        x_str, y_str = string.split(",")
        x = int(x_str.strip())
        y = int(y_str.strip())
        return Point(x, y)


class Axis(enum.Enum):
    X = 1
    Y = 2


class Instruction:
    def __init__(self, axis: Axis, value: int):
        self.axis = axis
        self.value = value

    def from_string(string: str) -> Instruction:
        axis_str, value_str = string.split()[-1].split("=")
        if axis_str.lower() == "x":
            axis = Axis.X
        else:
            axis = Axis.Y
        return Instruction(axis, int(value_str))


def read_data(filepath: str) -> Tuple[List[Point], List[Instruction]]:
    with open(filepath) as f:
        lines = f.read().splitlines()
    idx = lines.index("")
    coord_strings = lines[:idx]
    instruction_strings = lines[idx + 1:]
    points = list(map(Point.from_string, coord_strings))
    instructions = list(map(Instruction.from_string, instruction_strings))
    return points, instructions


def display(points: List[Point]):
    width = max(list(map(lambda p: p.x, points)))
    height = max(list(map(lambda p: p.y, points)))
    coords = list(map(lambda p: (p.x, p.y), points))

    print("-" * (width + 5))
    for y in range(height + 1):
        print("| ", end="")
        for x in range(width + 1):
            if (x, y) in coords:
                print("#", end="")
            else:
                print(".", end="")
        print(" |")
    print("-" * (width + 5))


def fold(points: List[Point], instruction: Instruction):
    points_to_remove = []
    for i in range(len(points)):
        x, y = points[i].coords
        if instruction.axis == Axis.X:
            if x == instruction.value:
                points_to_remove.append(points[i])
            elif x > instruction.value:
                points[i] = Point(2 * instruction.value - x, y)
        else:
            if y == instruction.value:
                points_to_remove.append(points[i])
            elif y > instruction.value:
                points[i] = Point(x, 2 * instruction.value - y)

    for point in points_to_remove:
        points.remove(point)


def main():
    points, instructions = read_data(sys.argv[1])
    if len(sys.argv) > 2:
        num_folds_to_complete = int(sys.argv[2])
    else:
        num_folds_to_complete = len(instructions)

    for instruction in instructions[:num_folds_to_complete]:
        fold(points, instruction)
    display(points)
    points = list(set(points))
    print(f"There are {len(points)} unique points")


if __name__ == "__main__":
    main()
