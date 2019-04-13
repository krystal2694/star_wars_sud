# Krystal Wong
# A01089672
# Theoren Leveille
# A01070327
# 08/04/2019
import doctest


def base_conversion(original_base: int, original_number: int, destination_base: int) -> int:
    """Convert a number in base 'n' to a number in base 'n', where 2 <= n <= 10.

    PRECONDITION: original base and destination base must be between 2 and 10
    POSTCONDITION: original number is converted to number in specified base

    >>> base_conversion(6, 12452, 2)
    11101110000
    >>> base_conversion(10, 3581, 9)
    4818
    >>> base_conversion(8, -76, 2)
    -111110"""

    if 2 <= original_base and destination_base <= 10:
        decimal_number = int(str(original_number), original_base)  # converts number in base 'n' to a decimal

        if decimal_number < 0:
            num_str = decimal_to_base_n(decimal_number * -1, destination_base)  # converts
            return int(num_str) * -1
        else:
            num_str = decimal_to_base_n(decimal_number, destination_base)  # converts
            return int(num_str)
    else:
        raise ValueError('Cannot calculate: both bases must be within 2 and 10.')


def decimal_to_base_n(decimal_number: int, destination_base: int):
    """Convert a base 10 number to a number in base 'n'.

    PRECONDITION: decimal number and destination base must be integers
    POSTCONDITION: Number is converted from base 10 to base n
    >>> decimal_to_base_n(1389, 2)
    '10101101101'
    >>> decimal_to_base_n(873, 9)
    '1170'"""
    quotient = decimal_number // destination_base
    remainder = decimal_number % destination_base
    if quotient == 0:
        return remainder
    else:
        return str(decimal_to_base_n(quotient, destination_base)) + str(decimal_number % destination_base)


def main():
    print(decimal_to_base_n(12, 2))
    # original_base = 10
    # original_number = 5
    # destination_base = 5
    # print(base_conversion(original_base, original_number, destination_base))
    doctest.testmod()


if __name__ == '__main__':
    main()
