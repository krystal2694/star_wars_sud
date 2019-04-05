# Krystal Wong
# A01089672
# Theoren Leveille
# A01070327
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
    if num > 0:
        for i in range(1, num + 1):
            if num % i == 0:
                counter += 1
        if counter == 2:
            return True
    return False


def remove_multiples(num: int, num_list: list)-> list:
    """Return a new list excluding multiples of num, but including num itself.

    PRECONDITION: num must not be 0

    >>> list_1 = [1, 2, 3, 4, 5, 6]
    >>> remove_multiples(2, list_1 )
    [1, 2, 3, 5]
    >>> list_2 = [3, 5, 6, 12, 14, 15, 20, 21, 42, 30, 31]
    >>> remove_multiples(3, list_2)
    [3, 5, 14, 20, 31]
    """
    new_list = num_list[:]
    for i in num_list:
        if i != num and i % num == 0:
            new_list.remove(i)
    return new_list


def sum_of_primes(upper_bound: int)-> int:
    """Return the sum of all prime numbers in the range 0 to upper_bound.

    >>> sum_of_primes(11)
    28
    >>> sum_of_primes(5)
    10
    """

    if upper_bound <= 0:
        raise ValueError("upper_bound must be a positive integer!")

    num_list = list(range(0, upper_bound + 1))
    prime_list = num_list[:]

    for i in range(0, int(sqrt(upper_bound)) + 1):
        if num_list[i] == 0 or num_list[i] == 1:
            prime_list.remove(num_list[i])
        elif is_prime_number(num_list[i]):
            prime_list = remove_multiples(num_list[i], prime_list)

    return sum(prime_list)


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
