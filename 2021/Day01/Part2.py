#!/usr/bin/env python3
import sys

datafile = sys.argv[1]
window_len = int(sys.argv[2])

with open(datafile, "r") as f:
    lines = f.read().splitlines()

data = list(map(int, lines))
data_points = len(data)

# NO WINDOWS
## There is no use in knowing the sum at all. We just need to know if the new
## number is greater than the old one.
counter = 0
for out_num, in_num in zip(data[:window_len * -1], data[window_len:]):
    if out_num < in_num:
        counter += 1
print(counter)

# Window Approach #1
## Fetch two windows and calculate their sums each time
counter = 0
for i in range(window_len, data_points):
    last_range = data[i - window_len: i]
    this_range = data[i - window_len + 1: i + 1]
    if sum(last_range) < sum(this_range):
        counter += 1
print(counter)

# Window Approach #2
## Track one window and calculate its sum twice each time
counter = 0
window = data[:window_len]
for num in data[window_len:]:
    last_sum = sum(window)
    window.pop(0)
    window.append(num)
    this_sum = sum(window)
    if last_sum < this_sum:
        counter += 1
print(counter)

# Window Approach #3
## Calculate the sum of the initial window. Continue subtracting the number
## heading out and adding the number heading in each time
counter = 0
last_sum = sum(data[:window_len])
for out_num, in_num in zip(data[:window_len * -1], data[window_len:]):
    this_sum = last_sum - out_num + in_num
    if last_sum < this_sum:
        counter += 1
    last_sum = this_sum
print(counter)
