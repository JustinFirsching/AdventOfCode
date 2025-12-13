# Sat Dec 13 02:15:01 PM EST 2025

with open(0) as f:
    data = f.read().splitlines()

splits = 0
indexes = set()
for i, row in enumerate(data):
    if i == 0:
        indexes.add(row.index("S"))
        continue

    for j, val in enumerate(row):
        # Not a split if we never made it here
        if val == "^" and j in indexes:
            splits += 1
            indexes.add(j - 1)
            indexes.remove(j)
            indexes.add(j + 1)

print(f"{splits=}")

# Sat Dec 13 02:25:29 PM EST 2025
from collections import defaultdict
indexes = set()
ways_to_each_point = defaultdict(int)
for i, row in enumerate(data):
    if i == 0:
        start = row.index("S")
        indexes.add(start)
        ways_to_each_point[start] = 1
        continue

    new_indexes = indexes
    for j, val in enumerate(row):
        if val == "^" and j in indexes:
            # There are ways to get to j, so post-split there were ways to get to j-1 or j+1
            if j - 1 >= 0:
                ways_to_each_point[j - 1] += ways_to_each_point[j]
                new_indexes.add(j - 1)

            if j + 1 < len(data[0]):
                ways_to_each_point[j + 1] += ways_to_each_point[j]
                new_indexes.add(j + 1)

            del ways_to_each_point[j]
            new_indexes.remove(j)

    indexes = new_indexes

print(sum(ways_to_each_point.values()))

# Sat Dec 13 02:39:53 PM EST 2025
