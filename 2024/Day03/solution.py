# Started: 12/03/2024 09:23 AM
# Part 1 Submitted: 12/03/2024 09:27 PM
# Part 2 Submitted: 12/03/2024 09:33 PM
#
# Notes:
#   After:
#     regex problems are never super interesting, but I like that this was
#     another 10 minute problem.
#     I didn't realize the sample input changed for a couple minutes doing
#     part 2, leading me to debug a "0" answer for a bit. Once I fixed the
#     input the implementation was correct.

import sys
import re

input = open(sys.argv[1]).read()

# Part 1
mul = re.compile(r"mul\((\d+),(\d+)\)")
answer = 0
for match in mul.findall(input):
    answer += int(match[0]) * int(match[1])
print(answer)

# Part 2
answer = 0
include = True
mul = re.compile(r"(do(?:n't)?\(\)|mul\((\d+),(\d+)\))")
for match in mul.findall(input):
    if match[0] == "don't()":
        include = False
    elif match[0] == "do()":
        include = True
    elif include:
        answer += int(match[1]) * int(match[2])
print(answer)
