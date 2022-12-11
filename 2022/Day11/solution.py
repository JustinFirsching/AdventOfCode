#!/usr/bin/env python3

import re
import sys

from copy import deepcopy

input_file = "sample.txt" if len(sys.argv) != 2 else sys.argv[1]

with open(input_file) as f:
    data = f.read().splitlines()


class Monkey:
    items = None
    op = None
    op_factor = None
    test_factor = None
    test_true_target = None
    test_false_target = None
    hist = 0

    def operate(self, worry: int) -> int:
        self.hist += 1
        factor = int(self.op_factor) if self.op_factor != "old" else worry
        if self.op == "*":
            return worry * factor
        else:
            return worry + factor

    def test_worry(self, worry: int) -> int:
        return self.test_true_target \
                if worry % self.test_factor == 0 \
                else self.test_false_target

    def __str__(self) -> str:
        return f"{self.items} - {self.test_factor} - {self.op} {self.op_factor}"


monkey_re = re.compile(r"Monkey \d+:\s*")
items_re = re.compile(r"\s*Starting items: ([\d, ]+)")
op_re = re.compile(r"\s*Operation: new = old (.) (\d+|old)")
test_re = re.compile(r"\s*Test: divisible by (\d+)")
test_true_re = re.compile(r"\s*If true: throw to monkey (\d+)")
test_false_re = re.compile(r"\s*If false: throw to monkey (\d+)")

monkey = Monkey()
monkeys = []
for line in data:
    if monkey_re.match(line):
        continue
    elif items_re.match(line):
        monkey.items = list(map(int, items_re.findall(line)[0].split(", ")))
    elif op_re.match(line):
        monkey.op, monkey.op_factor = op_re.findall(line)[0]
    elif test_re.match(line):
        monkey.test_factor = int(test_re.match(line).group(1))
    elif test_true_re.match(line):
        monkey.test_true_target = int(test_true_re.match(line).group(1))
    elif test_false_re.match(line):
        monkey.test_false_target = int(test_false_re.match(line).group(1))
    elif line == "":
        monkeys.append(monkey)
        monkey = Monkey()
monkeys.append(monkey)

print(list(map(str, monkeys)))

# Part 1
p1_monkeys = deepcopy(monkeys)
rounds = 20
for round in range(rounds):
    print(f"==Round {round}==", file=sys.stderr)
    for i, monkey in enumerate(p1_monkeys):
        print(f"=Monkey {i}=", file=sys.stderr)
        for worry in monkey.items:
            new_worry = monkey.operate(worry)
            new_worry = new_worry // 3  # Int divide 3 after each op
            target = monkey.test_worry(new_worry)
            p1_monkeys[target].items.append(new_worry)
            print(f"Taking worry from {worry} to {new_worry} and giving it to Monkey {target}", file=sys.stderr)
        monkey.items = []

for i, monkey in enumerate(p1_monkeys):
    print(f"Monkey {i} inspected items {monkey.hist} times.", file=sys.stderr)

most_interactive = sorted(p1_monkeys, key=lambda monkey: monkey.hist, reverse=True)
print(most_interactive[0].hist * most_interactive[1].hist)

# Part 2
p2_monkeys = deepcopy(monkeys)

mod = 1
for monkey in monkeys:
    mod *= monkey.test_factor

rounds = 10000
for round in range(rounds):
    print(f"==Round {round}==", file=sys.stderr)
    for i, monkey in enumerate(p2_monkeys):
        print(f"=Monkey {i}=", file=sys.stderr)
        for worry in monkey.items:
            new_worry = monkey.operate(worry)
            new_worry = new_worry % mod  # Int divide 3 after each op
            target = monkey.test_worry(new_worry)
            p2_monkeys[target].items.append(new_worry)
            print(f"Taking worry from {worry} to {new_worry} and giving it to Monkey {target}", file=sys.stderr)
        monkey.items = []

most_interactive = sorted(p2_monkeys, key=lambda monkey: monkey.hist, reverse=True)
print(most_interactive[0].hist * most_interactive[1].hist)
