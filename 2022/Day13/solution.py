#!/usr/bin/env python3

import sys

data_file = sys.argv[1] if len(sys.argv) > 1 else "sample.txt"

with open(data_file) as f:
    data = list(map(str.splitlines, f.read().split("\n\n")))


def compare(left, right):
    if type(left) == int and type(right) == int:
        if left < right:
            return True
        elif right < left:
            return False

    elif type(left) == list and type(right) == list:
        for i, j in zip(left, right):
            ret = compare(i, j)
            if ret is not None:
                return ret

        if len(left) < len(right):
            return True
        elif len(right) < len(left):
            return False

    else:
        # One is an int, the other isn't
        left = left if type(left) is list else [left]
        right = right if type(right) is list else [right]
        return compare(left, right)

    # Return None if indecisive
    return None


# Part 1
p1 = 0
for i, (a, b) in enumerate(data, 1):
    a_list = eval(a)
    b_list = eval(b)
    is_ordered = compare(a_list, b_list)
    if is_ordered:
        p1 += i
print(p1)


# Part 2
from functools import cmp_to_key  # noqa: E402

new = []
for pair in data:
    new.extend(map(eval, pair))
data = new


def comparator(func):
    def comp(a, b):
        if func(a, b):
            return -1
        elif func(b, a):
            return 1
        else:
            return 0
    return comp


data.sort(key=cmp_to_key(comparator(compare)))

idx_2 = 1
idx_6 = 2
for packet in data:
    if compare(packet, [[2]]):
        idx_2 += 1
        idx_6 += 1
    elif compare(packet, [[6]]):
        idx_6 += 1

print(idx_2 * idx_6)
