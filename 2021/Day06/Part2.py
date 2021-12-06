#!/usr/bin/env python3
import sys

COOLDOWN = 6
NEW_SPAWN_DELAY = 2


class School:
    def __init__(self):
        self.fish = [0 for _ in range(COOLDOWN + NEW_SPAWN_DELAY + 1)]

    def __next__(self):
        spawns = self.fish.pop(0)
        self.fish.append(spawns)
        self.fish[COOLDOWN] += spawns
        return self

    def add_fish(self, state: int):
        self.fish[state] += 1

    def count_fish(self) -> int:
        return sum(self.fish)


def read_data(filepath: str) -> School:
    with open(filepath, "r") as f:
        lines = f.read()
    fish_states = map(int, lines.split(","))
    school = School()
    for fish in fish_states:
        school.add_fish(fish)
    return school


def main():
    school = read_data(sys.argv[1])
    num_days = int(sys.argv[2])
    for days in range(num_days):
        next(school)
    print(school.count_fish())


if __name__ == "__main__":
    main()
