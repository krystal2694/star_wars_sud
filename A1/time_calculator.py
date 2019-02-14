"""This program takes the time in seconds and convert it in the following format: days, hours, minutes, seconds."""

# Krystal Wong
# A01089672
# 02/02/2019
import doctest


def time_calculator(seconds):
    """Convert time from seconds to days, hours, minutes, and seconds.

    PARAM: seconds, a positive integer
    PRECONDITION: parameter must be a positive integer
    POSTCONDITION: correctly convert time from seconds to days, hours, minutes, and seconds
    RETURN: time in the format of days, hours, minutes, and seconds

    >>> time_calculator(1)
    [0, 0, 0, 1]
    >>> time_calculator(50000000)
    [578, 16, 53, 20]
    >>> time_calculator(100000000)
    [1157, 9, 46, 40]
    """

    days = seconds // 86400
    remainder_1 = seconds % 86400
    hours = remainder_1 // 3600
    remainder_2 = remainder_1 % 3600
    minutes = remainder_2 // 60
    seconds_final = remainder_2 % 60

    result = [days, hours, minutes, seconds_final]
    return result


def main():
    print(time_calculator(1000000))
    doctest.testmod()


if __name__ == '__main__':
    main()
