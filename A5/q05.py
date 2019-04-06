# Krystal Wong
# A01089672
# Theoren Leveille
# A01070327
# 03/04/2019
import doctest


def cashmoney(amount: float)-> dict:
    """Determine the most effective cash representation of the amount of money entered.

    PRECONDITION: amount must be a positive floating point number
    POSTCONDITION: determine the fewest number of each bill and coin to represent amount
    >>> cashmoney(56.23)
    {100: 0, 50: 1, 20: 0, 10: 0, 5: 1, 2: 0, 1: 1, 0.25: 0, 0.1: 2, 0.05: 0, 0.01: 2}
    >>> cashmoney(478.14)
    {100: 4, 50: 1, 20: 1, 10: 0, 5: 1, 2: 1, 1: 1, 0.25: 0, 0.1: 1, 0.05: 0, 0.01: 3}
    """
    denominations = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.25: 0, 0.10: 0, 0.05: 0, 0.01: 0}
    if isinstance(amount, float) is False or amount <= 0:
        raise TypeError('money must be a positive floating point number.')
    else:
        for key in denominations.keys():
            denominations[key] = int(amount // key)
            amount %= key

        return denominations


def main():
    breakdown = cashmoney(478.14)
    print(breakdown)
    doctest.testmod()


if __name__ == '__main__':
    main()
