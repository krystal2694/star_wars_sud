# Krystal Wong
# A01089672
# Theoren Leveille
# A01070327
# 03/04/2019
import doctest


def gcd(a: int, b: int)-> int:
    """Determine the greatest common divisor of two integers.

    PRECONDITION: both parameters must be non-zero integers.
    POSTCONDITION: determine the greatest common divisor of the two parameters
    >>> gcd(-25, 5)
    5
    >>> gcd(270, 192)
    6
    """
    try:
        remainder = a % b
    except ZeroDivisionError:
        print('a and b have to be non-zero integers.')
    else:
        if remainder == 0:
            return b
        else:
            return gcd(b, remainder)


def main():
    print(gcd(-25, -5))
    doctest.testmod()


if __name__ == '__main__':
    main()
