# Started: 12/04/2024 10:06 AM
# Part 1 Submitted: 12/04/2024 10:31 AM
# Break: 12/04/2024 10:32 AM - 12:50 AM
# Part 2 Submitted: 12/04/2024 12:55 PM
#
# Notes:
#   The diagonals took too long to implement. I wanted to use recursion for
#   some reason, but that doesn't make sense because I'd have to track the
#   direction I was moving.

import sys

input = open(sys.argv[1]).readlines()

# Part 1
def count_diagonals(grid, word):
    def check(x, y, dx, dy):
        for i in range(len(word)):
            new_x = x + i * dx
            new_y = y + i * dy
            if new_x >= len(grid) or new_y >= len(grid[0]):
                return False
            elif new_x < 0 or new_y < 0:
                return False
            elif grid[new_x][new_y] != word[i]:
                return False
        return True

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            for mx, my in [(1, 1), (1, -1)]:
                if check(i, j, mx, my):
                    count += 1
    return count

horizontal = sum(map(lambda row: row.count("XMAS") + row.count("SAMX"), input))
vertical = sum(map(lambda col: "".join(col).count("XMAS") + "".join(col).count("SAMX"), zip(*input)))
# Find all diagonals
diagonals = count_diagonals(input, "XMAS") + count_diagonals(input, "SAMX")
print(horizontal + vertical + diagonals)

# Part 2
def check(grid, x: int, y: int) -> bool:
    if grid[x][y] != "A":
        return False
    p_diag = f"{grid[x - 1][y - 1]}A{grid[x + 1][y + 1]}"
    s_diag = f"{grid[x - 1][y + 1]}A{grid[x + 1][y - 1]}"
    p_valid = p_diag in ["MAS", "SAM"]
    s_valid = s_diag in ["MAS", "SAM"]
    return p_valid and s_valid

count = 0
for x in range(1, len(input) - 1):
    for y in range(1, len(input[0]) - 1):
        if check(input, x, y):
            count += 1
print(count)
