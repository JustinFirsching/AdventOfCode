# Started: 12/07/2024 10:38 PM
# Part 1 Submitted: 12/07/2024 10:57 PM
# Part 2 Submitted: 12/07/2024 11:33 PM
#
# Notes:
#   Before:
#     I need to start finding my solution before I start coding. Spam-coding
#     never got anybody anywhere.
#   After:
#     CARTESIAN PRODUCT! THAT'S WHAT I WAS LOOKING FOR! Kept thinking
#     permutations or combinations, but I couldn't get them working.
#
#     I should start doing what the good solvers do and just modify the
#     original case to handle both parts.

import sys

input = open(sys.argv[1]).readlines()

# Part 1

## Brute force every combination of * and +
## Use a bit mask to represent the operations

result = 0
for calibration in input:
    target, numbers = calibration.split(": ")

    target = int(target)
    numbers = [int(n) for n in numbers.split(" ")]

    max_op_mask = 1 << (len(numbers) - 1)
    for mask in range(max_op_mask):
        current = numbers[0]
        for i, number in enumerate(numbers[1:]):
            op = 1 << i & mask
            if op == 0: # Add
                current += number
            else: # Multiply
                current *= number
            if current > target: # Time save
                break
        if current == target:
            result += target
            break

print(result)

# Part 2

## Third operator... saw that coming
##
## Let's just generate the permutations of the operators and iterate through that
## We could use base 3, but I think this is more readable
##
## Of course I get an index error on a ridiculously large test case, back to
## base 3 instead of debugging this.

def ternary(n):
    if n == 0:
        return "0"
    nums = []
    while n > 0:
        nums.append(str(n % 3))
        n //= 3
    return "".join(nums[::-1])

result = 0
for calibration in input:
    target, numbers = calibration.split(": ")

    target = int(target)
    numbers = [int(n) for n in numbers.split(" ")]
    num_operations = len(numbers) - 1

    max_op_mask = 3 ** num_operations
    for mask in range(max_op_mask):
        current = numbers[0]
        mask = ternary(mask)
        mask = f"{mask:0>{num_operations}}"
        for number, op in zip(numbers[1:], mask):
            op = int(op)
            if op == 0: # Add
                current += number
            elif op == 1: # Multiply
                current *= number
            else: # Concat
                current = int(f"{current}{number}")

            if current > target: # Time save
                break

        if current == target:
            result += target
            break

print(result)
