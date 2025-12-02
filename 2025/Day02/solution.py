# Tue Dec  2 01:02:15 EST 2025
with open(0) as f:
    products = f.read().split(",")

def is_invalid_p1(number: int) -> bool:
    str_number = str(number)
    half_length = len(str_number) // 2
    return str_number[:half_length] == str_number[half_length:]

def is_invalid_p2(number: int) -> bool:
    str_number = str(number)
    for end in range(1, len(str_number)):
        if len(str_number) % end != 0:
            continue

        potential_repeat = str_number[:end]
        occurances = str_number.count(potential_repeat)
        if occurances * end == len(str_number):
            return True

    return False

invalid_sum_p1 = 0
invalid_sum_p2 = 0
for product in products:
    start, end = product.split('-')
    start, end = int(start), int(end)
    for number in range(start, end + 1):
        if is_invalid_p1(number):
            invalid_sum_p1 += number
        if is_invalid_p2(number):
            invalid_sum_p2 += number

print(invalid_sum_p1)
# Tue Dec  2 01:12:01 EST 2025

print(invalid_sum_p2)
# Tue Dec  2 01:12:38 EST 2025
# Accidentally started with a part 2 implementation lol
