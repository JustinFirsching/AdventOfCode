#!/usr/bin/env python3

import sys
from math import prod
from typing import List, Tuple


def type_4_parse(data: str) -> Tuple[int, int]:
    i = 0
    bitstring = ""
    do_next = True
    while do_next:
        do_next = (i + 5 < len(data) and data[i] == "1")
        i += 1
        bitstring += data[i: i + 4]
        i += 4
    return i, int(bitstring, 2)


def operator_parse(data: str) -> Tuple[int, int, str]:
    length_type_id = int(data[0])
    if(length_type_id == 0 and len(data) > 16):
        len_bits = data[1:16]
        length = int(len_bits, base=2)
        remaining_data = data[16:]
    elif(len(data) > 12):
        len_bits = data[1:12]
        length = int(len_bits, base=2)
        remaining_data = data[12:]
    else:
        length = 0
        remaining_data = ""
    return (length_type_id, length, remaining_data)


def read_packet(bits: str) -> Tuple[int, int, str]:
    version = int(bits[0:3], base=2)
    type_id = int(bits[3:6], base=2)
    remaining_data = bits[6:]
    return (version, type_id, remaining_data)


def parse(bits: str) -> Tuple[str, int]:
    version, type_id, bits = read_packet(bits)
    if type_id == 4:
        endpoint, _ = type_4_parse(bits)
        bits = bits[endpoint:]
        return bits, version
    else:
        len_id, length, bits = operator_parse(bits)
        subpackets = []
        if len_id == 0:
            subbits, bits = bits[:length], bits[length:]
            while subbits:
                subbits, value = parse(subbits)
                subpackets.append(value)
        else:
            for _ in range(length):
                bits, value = parse(bits)
                subpackets.append(value)
        ans = sum(subpackets) + version
        return bits, ans


def read_data(filepath: str) -> List[str]:
    with open(filepath, "r") as f:
        data = f.read().splitlines()
    bit_transmissions = []
    for hex_data in data:
        bits = bin(int(hex_data, base=16))[2:]
        # Need to pad appropriately
        bits_short = 4 - len(bits) % 4
        if bits_short != 4:
            bits = "0" * bits_short + bits
        bit_transmissions.append(bits)
    return bit_transmissions


def main():
    data = read_data(sys.argv[1])
    for transmission in data:
        print("-" * 80)
        print(transmission)
        _, answer = parse(transmission)
        print(answer)


if __name__ == "__main__":
    main()
