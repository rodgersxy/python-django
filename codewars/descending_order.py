def descending_order(num):
    """
    rearange the digits of an integer in descending order
    returns digits in descending order
    """
    return int("".join(sorted(str(num), reverse=True)))

print(descending_order(123456789))