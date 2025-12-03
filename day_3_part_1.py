from contextlib import suppress
from itertools import islice

total_joltage = 0


def iter_index(iterable, value, start=0, stop=None):
    "Return indices where a value occurs in a sequence or iterable."
    # iter_index('AABCADEAF', 'A') → 0 1 4 7
    seq_index = getattr(iterable, "index", None)
    if seq_index is None:
        iterator = islice(iterable, start, stop)
        for i, element in enumerate(iterator, start):
            if element is value or element == value:
                yield i
    else:
        stop = len(iterable) if stop is None else stop
        i = start
        with suppress(ValueError):
            while True:
                yield (i := seq_index(value, i, stop))
                i += 1


def get_highest_joltage(bank: str):
    digit_indexes = []

    digits = [int(digit) for digit in list(bank)]
    for n in range(9, 0, -1):
        if n in digits:
            # get index positions of digit in bank
            indexes = iter_index(digits, n)
            for i in indexes:
                if i not in digit_indexes:
                    digit_indexes.append(
                        i
                    )  # get index and check which digits come after
                    if len(digit_indexes) == 2:
                        break
                    # check digits to the right of the first battery
                    if not len(digits) == i + 1:
                        digits_remainder = digits[i + 1 :]
                        remaining_max = max(digits_remainder)
                        remaining_indexes = iter_index(digits, remaining_max)
                        for j in remaining_indexes:
                            if j > i:
                                digit_indexes.append(j)
                                if len(digit_indexes) == 2:
                                    break
                    if len(digit_indexes) == 2:
                        break

            if len(digit_indexes) == 2:
                break

        if len(digit_indexes) == 2:
            break

    # sort indexes
    sorted_indexes = sorted(digit_indexes)
    # print("Sorted indexes:\n", sorted_indexes)
    # concatenate number
    joltage = ""
    for di in sorted_indexes:
        joltage += str(digits[di])

    return int(joltage)


with open("input/day_3_input.txt", mode="rt", encoding="utf-8") as inputfile:
    banks = inputfile.readlines()

for bank in banks:
    highest_joltage = get_highest_joltage(bank.strip("\n"))
    total_joltage += highest_joltage

    # print("Bank:\n", bank)
    # print("Joltage:\n", highest_joltage)

print("Totel joltage:\n", total_joltage)
