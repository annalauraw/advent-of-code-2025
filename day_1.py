import re


def _get_dial_position(number, zero_crossings: int = 0):
    """
    Get a number between 0 and 99.
    """
    try:
        assert 0 <= number <= 99
        return number, zero_crossings
    except AssertionError:
        if number != 100:
            zero_crossings += 1
        if number > 99:
            number = number - 100
        elif number < 0:
            number = 100 + number
        return _get_dial_position(number, zero_crossings)


def _get_direction_and_amount(operation: str):
    matches = re.search(r"(R|L)(\d+)", operation)
    if matches:
        direction = matches.group(1)
        amount = int(matches.group(2))
        return direction, amount


def get_next_dial_position(start_position: int, operation: str):
    direction, amount = _get_direction_and_amount(operation)
    if direction == "L":
        amount = -amount
    new_number = start_position + amount

    new_position, zero_crossings = _get_dial_position(new_number)

    # prevent double-counting with L-operations
    if start_position == 0 and direction == "L":
        zero_crossings -= 1

    return new_position, zero_crossings


if __name__ == "__main__":

    start_position = 50
    zero_counter = 0

    with open("input/day_1_input.txt", mode="rt", encoding="utf-8") as inputfile:
        operations = inputfile.readlines()

    print(f"Input file contains {str(len(operations))} operations.")

    for op in operations:

        next_dial_position, zero_crossings = get_next_dial_position(start_position, op)
        print(f"Starting position: {str(start_position)}")
        print(f"Operation: {op}")
        print(f"New position: {str(next_dial_position)}")
        print(f"Zero crossings: {str(zero_crossings)}")
        # part 1
        if next_dial_position == 0:
            zero_counter += 1

        # part 2
        zero_counter += zero_crossings

        start_position = next_dial_position

    print(str(zero_counter))
