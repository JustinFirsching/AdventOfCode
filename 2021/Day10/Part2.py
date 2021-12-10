#!/usr/bin/env python3
import sys
from typing import Tuple, List

from Part1 import pairs, read_data

scores = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}


def find_line_completions(data: List[str]) -> List[Tuple[str, str]]:
    completions = []
    for line in data:
        last_open = []
        is_corrupt = False
        for char in line:
            if char in pairs.keys():
                last_open.append(char)
            else:
                expected = last_open.pop()
                expected_match = pairs[expected]
                if expected_match != char:
                    is_corrupt = True
                    break

        if not is_corrupt:
            completion = ""
            while last_open:
                completion += pairs[last_open.pop()]
            completions.append(completion)
    return completions


def main():
    lines = read_data(sys.argv[1])
    completions = find_line_completions(lines)

    completion_scores = []
    for completion in completions:
        score = 0
        for char in completion:
            score *= 5
            score += scores[char]
        completion_scores.append(score)
    completion_scores.sort()
    print(completion_scores[len(completion_scores) // 2])


if __name__ == "__main__":
    main()
