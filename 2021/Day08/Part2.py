#!/usr/bin/env python3

import sys

from typing import Dict, List

from Part1 import SIGNALS

SIGNALS_BIN = [
    "0b1110111",  # 0
    "0b0010010",  # 1
    "0b1011101",  # 2
    "0b1011011",  # 3
    "0b0111010",  # 4
    "0b1101011",  # 5
    "0b1101111",  # 6
    "0b1010010",  # 7
    "0b1111111",  # 8
    "0b1111011",  # 9
]

LETTERS = ["a", "b", "c", "d", "e", "f", "g"]


def identify_signals_by_length(signals: List[str], length: int):
    return list(filter(lambda signal: len(signal) == length, signals))


def to_bits(signal: List[str]):
    return [0 if letter not in signal else 1 for letter in LETTERS]


def to_bit_string(signal: List[str]):
    return "".join(map(str, to_bits(signal)))


def to_letters(string: List[str], letter_order: List[str] = LETTERS):
    letters = [l for (i, l) in enumerate(letter_order) if string[i] == "1"]
    return "".join(letters)


def find_key(
    signals: List[str],
    outputs: List[str]
) -> Dict[str, str]:
    all_signals = sorted(
        list(set(signals + outputs)), key=lambda sig: (len(sig), sig)
    )

    nums_to_signals = {}
    easy_targets = [1, 4, 7, 8]
    for target in easy_targets:
        signals = identify_signals_by_length(all_signals, len(SIGNALS[target]))
        nums_to_signals[target] = signals[0]

    key = {}

    cf = list(nums_to_signals[1])

    a = [l for l in nums_to_signals[7] if l not in cf]
    key['a'] = a[0]

    bd = [l for l in nums_to_signals[4] if l not in cf]

    eg = []
    len_5 = identify_signals_by_length(all_signals, 5)
    for sig in len_5:
        solved = [l for l in sig if l in bd]
        missing = [l for l in sig if l not in cf + bd + a]
        if len(solved) == 1 and len(missing) == 2:
            key['d'] = solved[0]
            key['b'] = [l for l in bd if l != key['d']][0]
            eg = missing
            break

    for sig in identify_signals_by_length(all_signals, 6):
        # No length 6 signals have only b or only e
        eg_solved = [l for l in sig if l in eg]
        if len(eg_solved) == 1:
            key['g'] = eg_solved[0]
            key['e'] = [l for l in eg if l != key['g']][0]

    for sig in len_5:
        missing = [l for l in sig if l in cf]
        if len(missing) == 1:
            if key['b'] in sig:
                not_found = 'c'
                found = 'f'
            else:
                not_found = 'f'
                found = 'c'
            key[found] = missing[0]
            key[not_found] = [l for l in cf if l != key[found]][0]

    return key


def print_key(key: Dict[str, str]):
    print()
    print(f" {key['a'] * 4} ")
    print(f"{key['b']}    {key['c']}")
    print(f"{key['b']}    {key['c']}")
    print(f" {key['d'] * 4} ")
    print(f"{key['e']}    {key['f']}")
    print(f"{key['e']}    {key['f']}")
    print(f" {key['g'] * 4} ")
    print()


def read_input(filepath: str):
    with open(filepath, "r") as f:
        lines = f.read().splitlines()
    split_lines = list(map(lambda l: l.split("|"), lines))
    return list(map(lambda line: (line[0].split(), line[1].split()), split_lines))


def main():
    data = read_input(sys.argv[1])
    total = 0
    for signal, output in data:
        key = find_key(signal, output)
        inverse_key = {v: k for (k, v) in key.items()}
        print_key(key)

        translated_output = ""
        for num in output:
            translated_letters = "".join(sorted(list(map(inverse_key.get, num))))
            translated_digit = SIGNALS.index(translated_letters)
            translated_output += str(translated_digit)
        total += int(translated_output)
    print(total)


if __name__ == "__main__":
    main()
