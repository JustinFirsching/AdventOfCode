# Started: 12/02/2024 09:17 PM
# Part 1 Submitted: 12/02/2024 09:26 PM
# Part 2 Submitted: 12/02/2024 09:42 PM
#
# Notes:
#   Before:
#     Done on laptop. Time may be worse
#   After:
#     I need to stop trying to be clever and let bruteforce run for these

import sys

input = open(sys.argv[1]).readlines()
reports = list(map(lambda report: list(map(int, report.split())), input))

# Part 1
count = 0
for report in reports:
    asc = report[1] < report[-1]
    last = report[0]
    safe = True
    for this in report[1:]:
        safe &= last < this if asc else last > this

        diff = abs(this - last)
        safe &= diff >= 1 and diff <= 3
        last = this
    count += int(safe)

print(count)

# Part 2
def is_safe(report):
    asc = report[1] < report[-1]
    last = report[0]
    safe = True
    for this in report[1:]:
        safe &= last < this if asc else last > this

        diff = abs(this - last)
        safe &= diff >= 1 and diff <= 3
        last = this
    return safe

count = 0
for report in reports:
    if is_safe(report):
        count += 1
    else:
        for i in range(len(report)):
            if is_safe(report[:i] + report[i + 1:]):
                count += 1
                break

print(count)
