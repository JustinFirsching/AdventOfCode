# Sat Dec  6 07:29:40 PM EST 2025

with open(0) as f:
    banks = list(map(list, f.read().splitlines()))

total = 0
for bank in banks:
    bank = list(map(int, bank))
    largest = 0
    l = 0
    for r, n in enumerate(bank[1:], 1):
        if (jolts := int(f"{bank[l]}{n}")) > largest:
            largest = jolts

        if n > bank[l]:
            l = r
    # print(largest)

    total += largest

print(total)

# Sat Dec  6 07:37:07 PM EST 2025
# Idk what we can do other than greedy. I'm sure there's some good memo/DP
# solution to this, but it isn't immediately coming to mind.

from typing import List

def dfs(bank: List[int], idx: int = 0, running: int = 0) -> int:
    if idx == len(bank):
        return running

    if len(str(running)) == 12:
        return running

    take = dfs(bank, idx + 1, running * 10 + bank[idx])
    skip = dfs(bank, idx + 1, running)
    return max(take, skip)


total = 0
for bank in banks:
    bank = list(map(int, bank))
    largest = 0
    total += dfs(bank)

print(total)

# Finished writing
# Sat Dec  6 07:44:54 PM EST 2025
# Finished running
# Never. Found another approach based on HyperNeutrino's submission

total = 0
num_to_select = 12
for bank in banks:
    bank = list(map(int, bank))
    jolts = 0
    for selecting_idx in range(num_to_select):
        # Find the largest selectable digit
        # A selectable digit is a digit that allows for enough remaining digits
        # to fill the `num_to_select` digit requirement.
        # We can't use wrap-around (ex. [:-1]) references as [:0] would be the
        # last selection, and that is an empty list.
        num_to_pad = num_to_select - (selecting_idx + 1) # + 1 because selecting_idx is 0-indexed
        end_idx = len(bank) - num_to_pad
        digit = max(bank[:end_idx])
        # Find the earliest occurance of it
        bank = bank[bank.index(digit) + 1:]
        # Use that instance
        jolts = jolts * 10 + digit
    total += jolts
print(total)


# Sat Dec  6 07:53:22 PM EST 2025

# Why does this work?
# The number must have selected the local maxima for its position, but we
# cannot overrun the end of the bank or we won't have all 12 digits. If this
# problem stated to flip _up to_ 12 digits, that may be acceptable, but even
# in that case, a 12 digit answer would always be greater than anything less.
# As such, we can restrict which digits are valid for selection to only those
# that would leave enough digits for all remaining positions. This allows a
# worst case scenario of the last digit in the bank being the last digit in the
# jolts while guaranteeing that we have selected enough indexes to flip.

# Refactored to ensure understanding
# Sat Dec  6 08:22:03 PM EST 2025
