#!/usr/bin/env python3


def load_data(path: str) -> str:
    with open(path) as f:
        return f.read()


# start of packet = sequence of 4 unique characters
# subroutine needs to identify the first position where the four most recently
# received characters were unique
def find_start(input: str, seq_len: int = 4) -> int:
    for i in range(seq_len, len(input)):
        letters = input[i-seq_len: i]
        if len(set(letters)) == seq_len:
            return i
    return -1


def main():
    data = load_data("input.txt")
    p1_ans = find_start(data)
    print(p1_ans)
    p2_ans = find_start(data, 14)
    print(p2_ans)


if __name__ == "__main__":
    main()
