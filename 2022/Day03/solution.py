with open('input.txt') as f:
    data = f.read().splitlines()

sum = 0
for row in data:
    items = list(row)
    half = len(items) // 2
    comp1, comp2 = items[:half], items[half:]
    shared = [x for x in comp1 if x in comp2][0]
    if shared.isupper():
        value = ord(shared) - ord('A') + 27
    else:
        value = ord(shared) - ord('a') + 1
    sum += value
print(sum)


sum = 0
for i in range(0, len(data), 3):
    p1, p2, p3 = data[i:i + 3]
    badge = [x for x in list(p1) if x in p2 and x in p3][0]
    if badge.isupper():
        value = ord(badge) - ord('A') + 27
    else:
        value = ord(badge) - ord('a') + 1
    sum += value
print(sum)
