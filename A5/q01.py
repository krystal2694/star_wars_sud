# Krystal Wong
# A01089672
# 03/04/2019
from math import sqrt
import doctest


def is_prime_number(num: int)-> bool:
    """Return True if number is a prime number.

    >>> is_prime_number(5)
    True
    >>> is_prime_number(10)
    False
    """
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1
    if counter == 2:
        return True
    else:
        return False


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
