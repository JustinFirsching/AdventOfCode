#!/usr/bin/env python3
from collections import defaultdict

with open("input.txt") as f:
    data = f.read().splitlines()

contents = defaultdict(int)
dir_stack = ["/"]
for line in data:
    if line.startswith("$ "):
        cmd = line[2:].split()
        if cmd[0] == "cd":
            if cmd[1] == "..":
                dir_stack.pop()
            elif cmd[1] == "/":
                dir_stack = ["/"]
            else:
                dir_stack.append(cmd[1])
    elif line.startswith("dir"):
        pass
    else:
        size = int(line.split()[0])
        for i in range(1, len(dir_stack) + 1):
            contents["/".join(dir_stack[1:i]) or "/"] += size

# Part 1
print(sum(filter(lambda v: v <= 100000, contents.values())))

# Part 2
total_space = 70000000
available = total_space - contents["/"]

needed = 30000000
to_free = needed - available

to_delete = ("/", contents["/"])
for dir_data in contents.items():
    _, dir_size = dir_data
    if to_free > dir_size:
        continue

    if dir_size < to_delete[1]:
        to_delete = dir_data

print(to_delete)
