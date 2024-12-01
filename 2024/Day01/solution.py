# Started: 12/01/2024 10:34 AM
# Part 1 Submitted: 12/01/2024 10:40 AM
# Part 2 Submitted: 12/01/2024 10:43 AM

import sys

input = open(sys.argv[1]).readlines()
left_nums = []
right_nums = []
for line in input:
    l, r = map(int, line.split())
    left_nums.append(l)
    right_nums.append(r)
left_nums.sort()
right_nums.sort()

## Part 1
dist_sum = 0
for a, b in zip(left_nums, right_nums):
    dist = abs(b - a)
    dist_sum += dist

print(dist_sum)

## Part 2
from collections import Counter
left_occur = Counter(left_nums)
right_occur = Counter(right_nums)

similarity_sum = 0
for num, occur in left_occur.items():
    similarity = num * right_occur[num]
    similarity_sum += occur * similarity
print(similarity_sum)
