import re

counter = 0


def get_sequence_as_strs(sequence: list[int]):
    return [str(n) for n in sequence]


def get_double_patterns(number: str):
    return re.match(r"^(\d+)\1$", number)


def get_multiple_patterns(number: str):
    return re.match(r"^(\d+)\1+$", number)


with open("input/day_2_input.txt", mode="rt", encoding="utf-8") as inputfile:
    ranges = inputfile.read().split(",")

for r in ranges:
    match_obj = re.search(r"(\d+)-(\d+)", r)
    start = match_obj.group(1)
    end = match_obj.group(2)
    sequence = range(int(start), int(end) + 1)
    sequence_as_strs = get_sequence_as_strs(sequence)
    wrong_ids = filter(get_multiple_patterns, sequence_as_strs)
    for id in wrong_ids:
        print(id)
        counter += int(id)

print(counter)
