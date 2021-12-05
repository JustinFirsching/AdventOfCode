#!/usr/bin/env python3

import sys

input_file = sys.argv[1]

with open(input_file, "r") as f:
    diagnostic_data = f.read().splitlines()

columns = zip(*diagnostic_data)
# set(r) should only ever be {0, 1}
column_modes = map(lambda r: max(set(r), key=r.count), columns)
bit_string = "".join(list(column_modes))

gamma = int(bit_string, base=2)
print(f"The gamma rate is: {gamma}")

bit_mask = 2 ** len(bit_string) - 1
epsilon = ~gamma & bit_mask
print(f"The epsilon rate is: {epsilon}")

print(f"Epsilon * Gamma = {epsilon * gamma}")
