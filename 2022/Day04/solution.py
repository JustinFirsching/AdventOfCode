#!/usr/bin/env python3

with open("input.txt") as f:
    data = f.read().splitlines()

all_over = any_over = 0
for line in data:
    range_a, range_b = line.split(",")
    start_a, end_a = map(int, range_a.split("-"))
    start_b, end_b = map(int, range_b.split("-"))

    a_range = range(start_a, end_a + 1)
    b_range = range(start_b, end_b + 1)
    overlap_a = [o in b_range for o in a_range]
    overlap_b = [o in a_range for o in b_range]

    all_over += all(overlap_a) | all(overlap_b)
    any_over += any(overlap_a) | any(overlap_b)

# Part 1
print(all_over)

# Part 2
print(any_over)
