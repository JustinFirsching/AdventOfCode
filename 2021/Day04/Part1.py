#!/usr/bin/env python3

from __future__ import annotations

import sys
from typing import List, Tuple


class Board:
    def __init__(self, rows):
        self.rows = rows
        self.cols = list(zip(*rows))
        self.values = []

        for row in rows:
            self.values.extend(row)

    @staticmethod
    def from_strings(rows: List[str]) -> Board:
        return Board([list(map(int, r.strip().split())) for r in rows])

    def is_winner(self, called_numbers: List[int]) -> bool:
        return len(self.get_winning_numbers(called_numbers)) > 0

    def get_winning_numbers(self, called_numbers: List[int]) -> List[int]:
        potential_wins = self.rows + self.cols
        return list(filter(
            lambda win: all([n in called_numbers for n in win]),
            potential_wins
        ))

    def calculate_score(self, called_numbers: List[int]) -> int:
        uncalled = [n for n in self.values if n not in called_numbers]
        return sum(uncalled) * called_numbers[-1]


def load_data(data_file: str) -> Tuple[List[int], List[Board]]:
    with open(data_file, "r") as f:
        data = f.read().splitlines()

    numbers = list(map(int, data.pop(0).split(",")))
    boards = [data[i:i + 5] for i in range(1, len(data) - 1, 6)]

    boards = []
    for i in range(1, len(data) - 1, 6):
        rows = data[i:i + 5]
        boards.append(Board.from_strings(rows))

    return (numbers, boards)


def main():
    data_file = sys.argv[1]
    numbers, boards = load_data(data_file)

    called_numbers = []
    winner = None
    while numbers and winner is None:
        number = numbers.pop(0)
        called_numbers.append(number)

        winners = list(filter(
            lambda board: board.is_winner(called_numbers),
            boards
        ))
        if winners:
            # In this problem we can safely assume one person wins
            winner = winners[0]

    print(winner.calculate_score(called_numbers))


if __name__ == "__main__":
    main()
