# Sun Dec  7 09:37:46 PM EST 2025

with open(0) as f:
    data = f.read()
    fresh_ranges, available = map(str.split, data.split("\n\n"))

# Linked List is probably ideal

p1 = 0
for ingredient in available:
    ingredient = int(ingredient)
    for _range in fresh_ranges:
        start, end = map(int, _range.split("-"))
        if start <= ingredient <= end:
            p1 += 1
            break

print(p1)

# Sun Dec  7 09:41:02 PM EST 2025

# Brute force probably won't work for p2...
# unique = set()
# for _range in ranges:
#     start, end = map(int, _range.split("-"))
#     for i in range(start, end + 1):
#         unique.add(i)
# print(len(unique))

# Shocking... doesn't work
# New approach: Reduce ranges

ranges = {}
for _range in fresh_ranges:
    start, end = map(int, _range.split("-"))
    ranges[start] = max(ranges.get(start, end), end)


changed = True
while changed:
    # Shoutout to ChatGPT for this code... I couldn't figure it out in the
    # moment and didn't want to spend any more time on it.
    ranges = dict(sorted(ranges.items()))
    merged_ranges = {}
    for start, end in ranges.items():
        if not merged_ranges:
            merged_ranges[start] = end
            continue
        last_start = list(merged_ranges.keys())[-1]
        last_end = merged_ranges[last_start]
        if start <= last_end + 1:
            merged_ranges[last_start] = max(last_end, end)
        else:
            merged_ranges[start] = end
    changed = len(ranges) != len(merged_ranges)
    ranges = merged_ranges

p2 = 0
for start, end in ranges.items():
    p2 += end - start + 1

print(p2)

# Sun Dec  7 09:56:10 PM EST 2025
