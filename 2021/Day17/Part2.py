#!/usr/bin/env python3
from __future__ import annotations

import sys
from Part1 import read_data, sign, Target, Probe


def count_hits(target: Target) -> int:
    hits = set()
    x_vels = range(
            0,
            target.br_corner[0] + sign(target.br_corner[0]),
            sign(target.br_corner[0])
        )
    y_vels = range(*sorted((abs(target.br_corner[1]), target.br_corner[1])))
    for x_vel in x_vels:
        for y_vel in y_vels:
            probe = Probe((x_vel, y_vel))
            while(target.can_hit((probe.x, probe.y))):
                hit = target.is_hit((probe.x, probe.y))
                if hit:
                    hits.add((x_vel, y_vel))
                probe.step()
    return len(hits)


def main():
    target = read_data(sys.argv[1])
    hits = count_hits(target)
    print(hits)


if __name__ == "__main__":
    main()
