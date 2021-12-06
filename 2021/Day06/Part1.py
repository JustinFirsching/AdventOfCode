#!/usr/bin/env python3
import sys
from typing import List


# This is bad, but I wanted something that would get me the visual in the
# example from the problem to start
class LanternFish:
    cooldown = 6

    def __init__(self, state: int):
        self.state = state

    def __next__(self):
        self.state = self.state - 1 if self.state != 0 \
            else LanternFish.cooldown
        return self

    def __str__(self):
        return f"Fish({self.state})"

    def can_spawn(self):
        return self.state == 0


def read_data(filepath: str) -> List[LanternFish]:
    with open(filepath, "r") as f:
        lines = f.read()
    states = map(int, lines.split(","))
    return list(map(lambda state: LanternFish(state), states))


def main():
    fish = read_data(sys.argv[1])
    num_days = int(sys.argv[2])
    num_to_spawn = 0
    for days in range(num_days):
        fish = list(map(lambda f: next(f), fish))
        fish += [LanternFish(8) for _ in range(num_to_spawn)]
        num_to_spawn = len(list(filter(lambda f: f.can_spawn(), fish)))
        print(f"After {days + 1:2d} days: " +
              ",".join(map(lambda f: str(f.state), fish)))
    print(len(fish))


if __name__ == "__main__":
    main()
