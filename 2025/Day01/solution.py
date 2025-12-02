# Part 1
# Mon Dec  1 23:46:20 EST 2025

with open(0) as f:
    instructions = f.read().splitlines()

count_zero = 0
pos = 50
for instruction in instructions:
    direction, steps = instruction[:1], int(instruction[1:])
    mod = 1 if direction == 'R' else -1
    pos = (pos + (mod * steps)) % 100
    if pos == 0:
        count_zero += 1

print(f"{count_zero=}")


# Part 2
# Mon Dec  1 23:50:16 EST 2025

count_zero = 0
pos = 50
for instruction in instructions:
    direction, steps = instruction[:1], int(instruction[1:])
    mod = 1 if direction == 'R' else -1
    for _ in range(steps):
        pos = (pos + mod) % 100
        if pos == 0:
            count_zero += 1


print(f"{count_zero=}")
