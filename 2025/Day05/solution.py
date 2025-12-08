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
    items = sorted(ranges.items(), key=lambda x: x[0])

    merged_ranges = {}
    cur_start, cur_end = items[0]

    for s, e in items[1:]:
        if s <= cur_end + 1:              # overlaps or touches
            cur_end = max(cur_end, e)     # extend
        else:
            merged_ranges[cur_start] = cur_end   # commit
            cur_start, cur_end = s, e     # restart

    merged_ranges[cur_start] = cur_end

    changed = len(ranges) != len(merged_ranges)
    ranges = merged_ranges

p2 = 0
for start, end in ranges.items():
    p2 += end - start + 1

print(p2)

# Sun Dec  7 09:56:10 PM EST 2025
