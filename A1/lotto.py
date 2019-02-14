"""This program generates 6 random unique numbers for the lottery."""

# Krystal Wong
# A01089672
# 02/02/2019
import random


def number_generator():
    """Return 6 random unique numbers in the range [1,49]."""

    lucky_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                  19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
                  35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
    lottery_numbers = (random.sample(lucky_list, 6))
    lottery_numbers.sort()
    return lottery_numbers


def main():
    print(number_generator())


if __name__ == '__main__':
    main()

# Unit tests - length, type, range, sorted
