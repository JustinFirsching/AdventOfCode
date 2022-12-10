#!/usr/bin/env python3

with open("input.txt") as f:
    data = f.read().splitlines()


deltas = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1)
}

num_knots = 10
knots = [(0, 0) for _ in range(num_knots)]
seen = {i: set() for i in range(num_knots)}
for line in data:
    direction, magnitude = line.split()
    magnitude = int(magnitude)

    dx, dy = deltas[direction]
    for i in range(magnitude):
        # The head moves consistent
        knots[0] = (knots[0][0] + dx, knots[0][1] + dy)
        for i, T in enumerate(knots[1:], 1):
            H = knots[i - 1]
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

            knots[i] = T
            seen[i].add(T)

for knot, visits in seen.items():
    print(f"Knot {knot}: {len(visits)} visits")
