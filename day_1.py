import re


def _get_dial_position(number, zero_crossings: int = 0):
    """
    Get a number between 0 and 99.
    """
    try:
        assert 0 <= number <= 99
        return number, zero_crossings
    except AssertionError:
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
    if direction == "R":
        new_number = start_position + amount
    elif direction == "L":
        new_number = start_position - amount

    new_position, zero_crossings = _get_dial_position(new_number)
    return new_position, zero_crossings


# def get_number_of_zero_crossings(start_position: int, operation: str):
#     zero_crossings = 0

#     direction, amount = _get_direction_and_amount(operation)
#     roughly = amount // 100
#     zero_crossings += roughly
#     modulo = amount % 100
#     if direction == "R":
#         modulo_addition = start_position + modulo
#     elif direction == "L":
#         modulo_addition = start_position - modulo

#     if not 0 <= modulo_addition <= 99:
#         zero_crossings += 1

#     print(f"Start position: {str(start_position)}")
#     print(f"Operation: {operation}")
#     print(f"Zero crossings: {str(zero_crossings)}")

#     return zero_crossings


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
        if next_dial_position == 0:
            zero_counter += 1

        # optionally: get all zero crossings
        # zero_crossings = get_number_of_zero_crossings(start_position, op)
        zero_counter += zero_crossings

        start_position = next_dial_position

    print(str(zero_counter))
