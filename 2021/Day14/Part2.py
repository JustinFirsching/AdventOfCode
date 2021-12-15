#!/usr/bin/env python3

from __future__ import annotations

import sys
from collections import defaultdict
from typing import Dict, List

from Part1 import InsertionRule, read_data


def count_chars_after_rules(
    template: str,
    rules: List[InsertionRule],
    iterations: int
) -> Dict[str, int]:
    init_pairs = list(map("".join, zip(template[:-1], template[1:])))
    pair_counts = defaultdict(
        int,
        **{p: init_pairs.count(p) for p in set(init_pairs)}
    )
    char_counts = defaultdict(
        int,
        **{char: template.count(char) for char in set(template)}
    )
    for _ in range(iterations):
        new_pair_counts = defaultdict(int)
        for pair, count in pair_counts.items():
            last_letter, this_letter = pair
            rule = next(
                filter(
                    lambda rule: rule.should_insert(last_letter, this_letter),
                    rules
                ),
                None
            )
            if rule:
                insert_letter = rule.insertion
                # We have to use += here incase the new pairs are the same
                new_pair_counts[f"{last_letter}{insert_letter}"] += count
                new_pair_counts[f"{insert_letter}{this_letter}"] += count
                char_counts[insert_letter] += count
            else:
                new_pair_counts[pair] = count
        pair_counts = new_pair_counts

    return char_counts


def main():
    template, rules = read_data(sys.argv[1])
    num_steps = int(sys.argv[2])
    char_counts = count_chars_after_rules(template, rules, num_steps)
    most_common_count = max(char_counts.values())
    least_common_count = min(char_counts.values())
    print(most_common_count - least_common_count)


if __name__ == "__main__":
    main()
