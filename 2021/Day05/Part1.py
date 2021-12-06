#!/usr/bin/env python3

from __future__ import annotations

import re
import sys

from typing import List


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @staticmethod
    def parse_coordinates(coords: str) -> Point:
        point = None
        match = re.match(r"\s*(\d+),\s*(\d+)\s*", coords)
        if match:
            x, y = match.groups()
            point = Point(int(x), int(y))
        return point

    def __str__(self):
        return f"{self.x}, {self.y}"


class Line:
    def __init__(self, a: Point, b: Point):
        # This makes all lines go up and right
        # self.start, self.end = sorted([a, b], key=lambda p: (p.x, p.y))
        self.start = a
        self.end = b

    @staticmethod
    def parse_line(line: str) -> Line:
        start_coords, end_coords = line.split("->")
        start = Point.parse_coordinates(start_coords)
        end = Point.parse_coordinates(end_coords)
        return Line(start, end)

    def get_covered_points(self) -> List[Point]:
        """
        y_range = range(self.start.y, self.end.y + 1, self.slope)
        x_range = range(self.start.x, self.end.x + 1, self.slope)
        return list(zip(x_range, y_range))
        """
        if self.start.x == self.end.x:
            dy = (self.end.y - self.start.y) // abs(self.end.y - self.start.y)
            y_coverage = range(self.start.y, self.end.y + dy, dy)
            x_coverage = [self.start.x] * (abs(self.start.y - self.end.y) + 1)
        elif self.start.y == self.end.y:
            dx = (self.end.x - self.start.x) // abs(self.end.x - self.start.x)
            x_coverage = range(self.start.x, self.end.x + dx, dx)
            y_coverage = [self.start.y] * (abs(self.start.x - self.end.x) + 1)
        else:
            # Not covered in Part 1
            return []
        return [Point(*coord) for coord in zip(x_coverage, y_coverage)]


class Diagram:
    def __init__(self, width: int, height: int):
        self.rows = [[0] * width for _ in range(height)]

    def cover_lines(self, *lines: Line):
        for line in lines:
            points = line.get_covered_points()
            for point in points:
                self.rows[point.y][point.x] += 1

    def print(self):
        for row in self.rows:
            print("| ", end="")
            for num in row:
                print(f"{num:2d} ", end="")
            print(" |")

    def count_n_intersects(self, n: int):
        count = 0
        for row in self.rows:
            for num in row:
                if num >= n:
                    count += 1
        return count


def read_data(filepath: str) -> List[Line]:
    with open(filepath, "r") as f:
        lines = f.read().splitlines()

    return [Line.parse_line(line) for line in lines]


def main():
    filepath = sys.argv[1]
    max_count = int(sys.argv[2])
    lines = read_data(filepath)
    diagram_width = max(map(lambda l: max(l.start.x, l.end.x), lines)) + 1
    diagram_height = max(map(lambda l: max(l.start.y, l.end.y), lines)) + 1
    diagram = Diagram(diagram_width, diagram_height)
    diagram.cover_lines(*lines)
    diagram.print()
    num_intersects = diagram.count_n_intersects(max_count)
    print(f"There are {num_intersects} points that are on at least "
          f"{max_count} lines.")


if __name__ == "__main__":
    main()
