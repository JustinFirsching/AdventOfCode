#!/usr/bin/env python3

from __future__ import annotations

import sys
from typing import List, Tuple


class InsertionRule:
    def __init__(self, lhs: str, rhs: str, insertion: str):
        self.lhs = lhs
        self.rhs = rhs
        self.insertion = insertion

    @staticmethod
    def parse_from_string(string: str) -> InsertionRule:
        pair, insertion = string.split(" -> ")
        lhs, rhs = pair[:len(pair) // 2], pair[len(pair) // 2:]
        return InsertionRule(lhs, rhs, insertion)

    def should_insert(self, lhs: str, rhs: str) -> bool:
        return lhs == self.lhs and rhs == self.rhs


def read_data(filepath: str) -> Tuple[str, List[str]]:
    with open(filepath, "r") as f:
        raw_data = f.read().splitlines()
    template = raw_data[0]
    rule_strings = raw_data[2:]
    rules = list(map(InsertionRule.parse_from_string, rule_strings))
    return template, rules


def apply_rules(
    template: str,
    rules: List[InsertionRule],
    iterations: int
) -> str:
    for _ in range(iterations):
        new_template = ""
        for last_letter, this_letter in zip(template[:-1], template[1:]):
            new_template += last_letter
            rule = next(
                filter(
                    lambda rule: rule.should_insert(last_letter, this_letter),
                    rules
                ),
                None
            )
            if rule:
                new_template += rule.insertion
        # The last letter is not added in the loop
        new_template += template[-1]

        template = new_template
    return template


def main():
    template, rules = read_data(sys.argv[1])
    num_steps = int(sys.argv[2])
    template = apply_rules(template, rules, num_steps)
    char_counts = [template.count(char) for char in set(template)]
    most_common_count = max(char_counts)
    least_common_count = min(char_counts)
    print(most_common_count - least_common_count)


if __name__ == "__main__":
    main()
