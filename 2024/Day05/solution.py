# Started: 12/06/2024 08:03 PM
# Part 1 Submitted: 12/06/2024 08:11 PM
# Part 2 Submitted: 12/06/2024 08:55 PM
#
# Notes:
#   Glad I finally thought about reading the data in a convenient way.
#   I tried manually sorting on Part 2 for some reason...

import sys
from collections import defaultdict

rules, updates = open(sys.argv[1]).read().split('\n\n')
rules = rules.splitlines()
updates = updates.splitlines()

# Part 1
precedence = defaultdict(set)
for line in rules:
    a, b = map(int, line.split("|"))
    precedence[a].add(b)

middle_sum = 0
for update in updates:
    seen = set()
    update = list(map(int, update.split(",")))
    correct = True
    for u in update:
        required_before = precedence[u]
        if required_before & seen:
            correct = False
            break
        seen.add(u)
    if correct:
        middle_idx = len(update) // 2
        middle_item = update[middle_idx]
        middle_sum += middle_item
print(middle_sum)

# Part 2
from functools import cmp_to_key
from typing import Tuple

def _sort_func(_a: Tuple[int, int], _b: Tuple[int, int]):
    a, b = _a[1], _b[1]
    a_idx, b_idx = _a[0], _b[0]
    # If either is in the other's precedence set, then it should come first
    if b in precedence.get(a, set()):
        return -1
    elif a in precedence.get(b, set()):
        return 1
    # Otherwise, leave them where they are
    elif a_idx > b_idx:
        return -1
    return 1
sort_func = cmp_to_key(_sort_func)

middle_sum = 0
for update in updates:
    seen = {}
    update = list(map(int, update.split(",")))
    was_incorrect = False
    new_update = list(map(lambda pair: pair[1], sorted(enumerate(update), key=sort_func)))
    changed = False
    for i, u in enumerate(update):
        if u != new_update[i]:
            changed = True
            break
    if changed:
        middle_idx = len(update) // 2
        middle_item = new_update[middle_idx]
        middle_sum += middle_item
print(middle_sum)
