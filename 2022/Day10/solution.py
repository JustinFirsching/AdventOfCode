#!/usr/bin/env python3

with open("input.txt") as f:
    data = f.read().splitlines()

X = 1
cycles = 0


signal_strengths = {}


def cycle(n):
    global cycles
    for _ in range(n):
        # Draw the sprite on CRT
        print("#" if (cycles % 40) in range(X - 1, X + 2) else ".", end="")

        # Count the cycle before determining signal strength
        cycles += 1

        # Calc signal strength
        if cycles == 20 or (cycles - 20) % 40 == 0:
            signal_strength = X * cycles
            signal_strengths[cycles] = signal_strength

        # Go to the next CRT line
        if cycles % 40 == 0:
            print()


for line in data:
    op, *args = line.split()
    if op == "addx":
        cycle(2)
        X += int(args[0])
    elif op == "noop":
        cycle(1)


print(sum(signal_strengths.values()))
