#!/usr/bin/env python3

with open("input.txt") as f:
    data = f.read().splitlines()


deltas = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1)
}

H = (0, 0)
T = (0, 0)

tail_seen = set()
for line in data:
    direction, magnitude = line.split()
    magnitude = int(magnitude)

    dx, dy = deltas[direction]
    for i in range(magnitude):
        H = (H[0] + dx, H[1] + dy)
        # If not diagonal
        x_dist = H[0] - T[0]
        y_dist = H[1] - T[1]

        x_trail_sign = 1 if x_dist > 0 else -1
        y_trail_sign = 1 if y_dist > 0 else -1

        # Same row, directly left or right
        if abs(x_dist) > 1 and y_dist == 0:
            T = (T[0] + x_trail_sign, T[1])
        # Same column, directly above or below
        elif abs(y_dist) > 1 and x_dist == 0:
            T = (T[0], T[1] + y_trail_sign)
        # Diagonal
        elif abs(y_dist) > 1 or abs(x_dist) > 1:
            T = (T[0] + x_trail_sign, T[1] + y_trail_sign)

        tail_seen.add(T)

print(len(tail_seen))
