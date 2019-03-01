"""Battle between two Pokemon."""
from random import randint


def determine_order():
    """Determine which character attacks first by rolling a 20 sided die once each.

    >>> random.seed(27)
    >>> determine_order()
    True
    >>> random.seed(8)
    >>> determine_order()
    False
    >>> random.seed()
    """

    opponent_one_roll = randint(1, 20)
    opponent_two_roll = randint(1, 20)
    if opponent_one_roll > opponent_two_roll:
        return True
    elif opponent_two_roll > opponent_one_roll:
        return False
    elif opponent_one_roll == opponent_two_roll:
        return determine_order()
