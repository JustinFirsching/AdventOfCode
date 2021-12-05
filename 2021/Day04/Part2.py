#!/usr/bin/env python3

import sys
from Part1 import load_data


def main():
    data_file = sys.argv[1]
    numbers, boards = load_data(data_file)

    called_numbers = []
    last_board = None
    # Just change this loop to "Until there are no more boards" and track the
    # last removed board
    while numbers and boards:
        number = numbers.pop(0)
        called_numbers.append(number)

        winners = list(filter(
            lambda board: board.is_winner(called_numbers),
            boards
        ))
        for winner in winners:
            last_board = winner
            boards.remove(winner)

    print(last_board.calculate_score(called_numbers))


if __name__ == "__main__":
    main()
