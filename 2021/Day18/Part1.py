#!/usr/bin/env python3
from __future__ import annotations

import sys
from typing import Any, List, Tuple, Union
from enum import Enum


class Target(Enum):
    Left = 0
    Right = 1


class Snailfish:
    def __init__(
        self,
        left: Union[int, Snailfish],
        right: Union[int, Snailfish]
    ):
        self.left = left
        self.right = right

    def __add__(self, other: Any) -> Snailfish:
        if not isinstance(other, Snailfish):
            raise TypeError("Snailfishes can only be added to Snailfishes")
        return Snailfish(self, Snailfish)

    def __iadd__(self, other: Any) -> Snailfish:
        if not isinstance(other, Snailfish):
            raise TypeError("Snailfishes can only be added to Snailfishes")
        self.left = Snailfish(self.left, self.right)
        self.right = other
        return self

    # Recursive __str__ say whaaaaaaaaaaat
    def __str__(self) -> str:
        return f"[{str(self.left)}, {str(self.right)}]"

    def explode(self, target: Target) -> Tuple[int, int]:
        print(f"Exploding {target} of {self}")
        # [[0, 8], 2] -> [0, 10]
        # [[0, 15], 2] -> [0, 17] and split on 0
        # [3, [0, 8]] -> [3, 0]
        # [3, [0, 15]] -> [3, 0] and split on 3
        # [[0, 15]] -> [0]

        left_data, right_data = 0, 0
        if target == Target.Left and isinstance(self.left, Snailfish):
            left_data = self.left.left
            right_data = self.left.right
            self.left = 0
        elif target == Target.Right and isinstance(self.right, Snailfish):
            left_data = self.right.left
            right_data = self.right.right
            self.right = 0
        else:
            raise AttributeError("Explosion target must be an immediate child")
        print(f"Exploded into {self} : {left_data} {right_data}")
        return left_data, right_data

    def split(self, target: Target):
        # 7 -> [3, 4]
        print(f"Splitting {target} of {self}")
        if target == Target.Left and isinstance(self.left, int):
            self.left = Snailfish(self.left // 2, (self.left + 1) // 2)
        elif target == Target.Right and isinstance(self.right, int):
            self.right = Snailfish(self.right // 2, (self.right + 1) // 2)
        else:
            raise AttributeError("Split target must be an immediate child")
        print(f"Split into {self}")

    def is_final_snailfish(self) -> bool:
        left_is_int = isinstance(self.left, int)
        right_is_int = isinstance(self.right, int)
        return left_is_int and right_is_int

    def add_constant(self, value: int, target: Target):
        print(self, value, target)
        if target == Target.Left:
            if isinstance(self.left, Snailfish):
                self.left.add_constant(value, target)
            else:
                print(f"Adding {value} to {self}")
                self.left += value
        else:
            if isinstance(self.right, Snailfish):
                self.right.add_constant(value, target)
            else:
                self.right += value

    @staticmethod
    def from_string(string: str) -> Snailfish:
        open_brackets = 0
        for i in range(1, len(string) - 1):
            char = string[i]
            if char == "[":
                open_brackets += 1
            elif char == "," and open_brackets == 0:
                split_idx = i
                break
            elif char == "]":
                open_brackets -= 1
        left, right = string[1:split_idx], string[split_idx + 1:-1]
        if "[" in left:
            left = Snailfish.from_string(left)
        else:
            left = int(left)

        if "[" in right:
            right = Snailfish.from_string(right)
        else:
            right = int(right)

        return Snailfish(left, right)

    def add_constant_nearest(
        self,
        value: int,
        side: Target
    ):
        print(f"Carrying into {self} - {side} : {value}")
        if side == Target.Left:
            if isinstance(self.left, Snailfish):
                self.left.add_constant(value, Target.Right)
            elif isinstance(self.left, int):
                self.left += value
        elif side == Target.Right:
            if isinstance(self.right, Snailfish):
                self.right.add_constant(value, Target.Left)
            elif isinstance(self.right, int):
                self.right += value


def reduce_snailfish(
    snailfish: Snailfish,
    depth: int = 0
):
    print(snailfish)
    left_is_int = isinstance(snailfish.left, int)
    left_can_explode = not left_is_int \
        and snailfish.left.is_final_snailfish() \
        and depth >= 3

    right_is_int = isinstance(snailfish.right, int)
    right_can_explode = not right_is_int \
        and snailfish.right.is_final_snailfish() \
        and depth >= 3

    left_carry, right_carry = 0, 0
    return_left_carry, return_right_carry = 0, 0
    if left_can_explode:
        left_carry, right_carry = snailfish.explode(Target.Left)
        snailfish.add_constant_nearest(right_carry, Target.Right)
        return_left_carry += left_carry

    if right_can_explode:
        left_carry, right_carry = snailfish.explode(Target.Right)
        snailfish.add_constant_nearest(left_carry, Target.Left)
        return_right_carry += right_carry

    left_is_int = isinstance(snailfish.left, int)
    left_spilt = left_is_int and snailfish.left > 10
    if left_spilt:
        snailfish.split(Target.Left)

    right_is_int = isinstance(snailfish.right, int)
    right_split = right_is_int and snailfish.right > 10
    if right_split:
        snailfish.split(Target.Right)

    if left_spilt or right_split:
        rereduction = reduce_snailfish(snailfish, depth)
        r_right_carry, r_left_carry = rereduction
        return_left_carry += r_left_carry
        return_right_carry += r_right_carry
        print(snailfish, r_left_carry, r_right_carry)

    left_is_int = isinstance(snailfish.left, int)
    if not left_is_int:
        left_reduction = reduce_snailfish(snailfish.left, depth + 1)
        lr_left_carry, lr_right_carry = left_reduction
        return_left_carry += lr_left_carry
        return_right_carry += lr_right_carry
        print(snailfish, lr_left_carry, lr_right_carry)

    right_is_int = isinstance(snailfish.right, int)
    if not right_is_int:
        right_reduction = reduce_snailfish(snailfish.right, depth + 1)
        rr_left_carry, rr_right_carry = right_reduction
        return_left_carry += rr_left_carry
        return_right_carry += rr_right_carry
        print(snailfish, rr_left_carry, rr_right_carry)

    return return_left_carry, return_right_carry


def check_magnitude(snailfish: Snailfish) -> int:
    # Pair: 3 * mag left + 2 * mag right
    # [9, 1] -> 3 * 9 + 2 * 1 = 29
    # Number: number
    # 4 -> 4
    if isinstance(snailfish.left, Snailfish):
        left = 3 * check_magnitude(snailfish.left)
    else:
        left = snailfish.left

    if isinstance(snailfish.right, Snailfish):
        right = 2 * check_magnitude(snailfish.right)
    else:
        right = snailfish.right

    return left + right


def read_data(filepath: str) -> List[Snailfish]:
    with open(filepath, "r") as f:
        raw_data = f.read().splitlines()
    problems = list(map(Snailfish.from_string, raw_data))
    return problems


def main():
    problems = read_data(sys.argv[1])
    total = problems[0]
    for problem in problems[1:2]:
        print(total)
        total += problem
        reduce_snailfish(total)
        print(total)


if __name__ == "__main__":
    main()
