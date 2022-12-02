#!/usr/bin/env python3

with open("input.txt") as f:
    inputs = f.read().splitlines()

calories = []

current = 0
for line in inputs:
    if line == "":
        calories.append(current)
        current = 0
    else:
        current += int(line)
calories.append(current)

print(f"Maximum Carried: {max(calories)}")

calories.sort(reverse=True)
top3 = calories[:3]
print(f"Top 3: {top3}. Total: {sum(top3)}")
