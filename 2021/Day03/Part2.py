#!/usr/bin/env python3

import sys
from typing import Callable, List


def get_rating(bits: List[str], default_val: str, comparator: Callable) -> int:
    rating = ""
    remaining_data = bits

    bit_len = len(bits[0])
    for i in range(bit_len):
        remaining_data = list(filter(
            lambda data: data.startswith(rating),
            remaining_data
        ))

        if(len(set(remaining_data)) == 1):
            # Break early if we find the answer
            rating = remaining_data[0]
            break

        col_bits = list(zip(*remaining_data))[i]
        column_counts = {bit: col_bits.count(bit) for bit in set(col_bits)}
        next_bit = comparator(column_counts.keys(), key=column_counts.get) \
            if len(set(column_counts.values())) > 1 else default_val
        rating += next_bit

    return int(rating, base=2)


def main():
    input_file = sys.argv[1]

    with open(input_file, "r") as f:
        diagnostic_data = f.read().splitlines()

    o2_rating = get_rating(diagnostic_data, "1", max)
    print(f"The oxygen generator rating is: {o2_rating}")

    co2_rating = get_rating(diagnostic_data, "0", min)
    print(f"The CO2 scrubber rating is: {co2_rating}")

    print("The product of the oxygen generator rating and CO2 scrubber rating "
          f"{o2_rating * co2_rating}")


if __name__ == "__main__":
    main()
