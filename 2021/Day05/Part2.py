#!/usr/bin/env python3

from __future__ import annotations

import sys

from typing import List

from Part1 import Point, Line, Diagram, read_data


class DiagonalSupportedLines(Line):
    def __init__(self, a: Point, b: Point):
        # This makes all lines go up and right
        # self.start, self.end = sorted([a, b], key=lambda p: (p.x, p.y))
        Line.__init__(self, a, b)

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
            dx = (self.end.x - self.start.x) // abs(self.end.x - self.start.x)
            dy = (self.end.y - self.start.y) // abs(self.end.y - self.start.y)
            # slope = dy/dx ;)
            x_coverage = range(self.start.x, self.end.x + dx, dx)
            y_coverage = range(self.start.y, self.end.y + dy, dy)
        return [Point(*coord) for coord in zip(x_coverage, y_coverage)]

    def __str__(self):
        return f"{self.start} -> {self.end}"


def main():
    filepath = sys.argv[1]
    max_count = int(sys.argv[2])
    lines = read_data(filepath)
    # Make them all diagonal supported lines
    lines = list(map(lambda l: DiagonalSupportedLines(l.start, l.end), lines))
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
