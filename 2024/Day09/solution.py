# Started: 12/09/2024 09:00 PM
# Part 1 Submitted: 12/09/2024 09:49 PM
# Part 2 Submitted: 12/10/2024 01:09 AM
#
# Notes:
#   I would've been so much better off separating into two files...
#   Slowest advent of code I've ever completed. This was awful.
#   The idea of a two digit "block" swapping with a one digit "block" was
#   painful to wrap my head around.

import sys

input = list(map(int, open(sys.argv[1]).read().strip()))
if len(input) % 2:
    input.append(0)

# Part 1
## Create blocks
## Going to try a different way
files_p2, spaces = input[:-1:2], input[1::2]
blocks_p1 = []
blocks_p2 = []
file_idx_pos_p2 = {}
s = 0
files_str = ""
file_id = 0
for f, s in zip(enumerate(files_p2), spaces):
    if f:
        file_id, num_blocks = f
        files_str += str(file_id) * num_blocks
        blocks_p1.extend([str(file_id)] * num_blocks)

        file_idx_pos_p2[file_id] = (len(blocks_p2), num_blocks)
        blocks_p2.append(str(file_id) * num_blocks)
    if s:
        blocks_p1.extend(['.'] * s)
        blocks_p2.append('.' * s)
# print("".join(blocks_p1))
#
# ## Order blocks
l, r = files_p2[0], len(blocks_p1) - 1
# Can't go character by character because of > single digit numbers
while l < r:
    blocks_p1[l], blocks_p1[r] = blocks_p1[r], blocks_p1[l]
    while blocks_p1[l] != ".":
        l += 1
    while blocks_p1[r] == ".":
        r -= 1
# print("".join(blocks_p1))

# Tried something else at 9:33 PM.
# Maybe the trick is to read it in differently
# Nope. Going back at 9:44
# avail_files = []
# for idx, block in enumerate(files):
#     avail_files.extend([str(idx)] * block)
#
# blocks = ""
# for i in range(len(files)):
#     if i % 2 == 0:
#         for _ in range(files[i // 2]):
#             blocks += avail_files.pop(0) if avail_files else "."
#     else:
#         for _ in range(spaces[i // 2]):
#             blocks += avail_files.pop() if avail_files else "."
# print(blocks)

## Compute checksum
def checksum(_list) -> int:
    s = 0
    for i, b in enumerate(_list):
        if b == ".":
            b = 0
        s += i * int(b)
    return s

print(checksum(blocks_p1))

## Swap blocks for p2
from collections import Counter

spaces_avail = Counter(spaces)

def find_leftmost_atleast(n: int) -> tuple[int, int]:
    m = 10 ** 100  # This better be enough...
    m_len = 10
    for size, count in sorted(spaces_avail.items(), reverse=True):
        if count == 0:
            continue

        if size < n:
            break

        if (idx := blocks_p2.index("." * size)) < m:
            m = idx
            m_len = size
    return m, m_len

# print(blocks_p2)
for file_id, num_blocks in reversed(list(enumerate(files_p2))):
    file = str(file_id) * num_blocks

    if num_blocks > max(spaces_avail.keys()):
        continue

    idx, l = find_leftmost_atleast(num_blocks)

    blocks_file_idx = blocks_p2.index(file)
    if idx > blocks_file_idx or idx == 10 ** 100:
        continue

    # Fill the space with the file
    blocks_p2[idx] = blocks_p2[blocks_file_idx]
    file_idx_pos_p2[file_id] = (idx, num_blocks)
    spaces_avail[l] -= 1

    # Replace the file with the space
    new_space = "." * num_blocks
    # If there are spaces in the slot before the new space index, merge them
    if "." in (this := blocks_p2[blocks_file_idx - 1]):
        new_space += this
        blocks_p2.pop(blocks_file_idx - 1)
        for k, (old_idx, v) in file_idx_pos_p2.items():
            if old_idx >= blocks_file_idx - 1:
                file_idx_pos_p2[k] = (old_idx - 1, v)
        blocks_file_idx -= 1
        spaces_avail[len(this)] -= 1

    # If there are spaces in the slot after the new space index, merge them
    if blocks_file_idx < (len(blocks_p2) - 1) and "." in (this := blocks_p2[blocks_file_idx + 1]):
        new_space += this
        blocks_p2.pop(blocks_file_idx + 1)
        for k, (old_idx, v) in file_idx_pos_p2.items():
            if old_idx > blocks_file_idx + 1:
                file_idx_pos_p2[k] = (old_idx - 1, v)
        spaces_avail[len(this)] -= 1

    assert sum(["." in b for b in blocks_p2[blocks_file_idx -1: blocks_file_idx + 2]]) <= 1, f"{blocks_p2[blocks_file_idx -1 : blocks_file_idx + 2]}"
    assert len(set(blocks_p2[blocks_file_idx])) == 1 if "." in blocks_p2[idx] else True
    blocks_p2[blocks_file_idx] = new_space
    spaces_avail[len(new_space)] += 1

    # If we couldn't fill the whole space with the number
    if l != num_blocks:
        # If there are already spaces in the slot to the right
        # New spaces to the right of the insert
        if "." in blocks_p2[idx + 1]:
            spaces_avail[len(blocks_p2[idx + 1])] -= 1
            blocks_p2[idx + 1] += "." * (l - num_blocks)
            spaces_avail[len(blocks_p2[idx + 1])] += 1
        else:
            blocks_p2.insert(idx + 1, "." * (l - num_blocks))
            spaces_avail[l - num_blocks] += 1
            for k, (old_idx, v) in file_idx_pos_p2.items():
                if old_idx >= idx + 1:
                    file_idx_pos_p2[k] = (old_idx + 1, v)

    # Make sure we don't have any weird freespace/reserved space combo blocks
    assert len(set(blocks_p2[idx])) == 1 if "." in blocks_p2[idx] else True


## I spent hours debugging the above only to realize the checksum is wrong...
## Now I need a new structure to track positions...

def checksum_p2() -> int:
    s = 0
    # block_pos = 0
    # for i, block in enumerate(blocks_p2):
    #     if "." in block:
    #         block_pos += len(block)
    #         continue
    #
    #     for file_id, (pos_in_blocks, num_blocks) in file_idx_pos_p2.items():
    #         # This means we found the right file
    #         if i == pos_in_blocks:
    #             for _ in range(num_blocks):
    #                 s += block_pos * file_id
    #                 block_pos += 1
    #             break

    file_blocks = 0
    space_blocks = 0

    blocks = 0

    last = 0
    file_id = 0
    for file_id, (start_idx, size) in sorted(file_idx_pos_p2.items(), key=lambda v: v[1][0]):
        # print(file_id, blocks, start_idx)
        # This makes sure we tracked indexes right
        assert blocks_p2[start_idx] == str(file_id) * size

        # Empty
        for idx in range(last + 1, start_idx):
            # print(blocks_p2[idx])
            b = len(blocks_p2[idx])
            space_blocks += b
            blocks += b

        # Filled
        for _ in range(size):
            s += blocks * file_id
            file_blocks += 1
            blocks += 1

        last = start_idx

    # Cleanup the last space blocks
    for block in reversed(blocks_p2):
        if "." not in block:
            break
        blocks += len(block)

    assert blocks == len(blocks_p1), (blocks, len(blocks_p1), space_blocks, file_blocks)

    return s

print(checksum_p2())
