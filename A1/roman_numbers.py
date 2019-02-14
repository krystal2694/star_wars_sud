"""This program converts a number into a roman numeral."""

# Krystal Wong
# A01089672
# 02/02/2019
import doctest


def convert_to_roman_numeral(positive_int):
    """Return the parameter in roman numeral form.

    PARAM: positive_int, an int
    PRECONDITION: positive_int must be a positive integer in the range [1, 10000]
    POSTCONDITION: translate the parameter into roman numeral form correctly
    RETURN:the roman numeral equivalent as a string

    >>> convert_to_roman_numeral(1)
    'I'
    >>> convert_to_roman_numeral(5000)
    'MMMMM'
    >>> convert_to_roman_numeral(10000)
    'MMMMMMMMMM'
    """

    roman_numeral = ""
    if positive_int//1000 > 0:
        roman_numeral += ((positive_int // 1000) * "M")
        positive_int %= 1000
    if positive_int//900 > 0:
        roman_numeral += "CM"
        positive_int %= 900
    if positive_int//500 > 0:
        roman_numeral += "D"
        positive_int %= 500
    if positive_int//400 > 0:
        roman_numeral += "CD"
        positive_int %= 400
    if positive_int//100 > 0:
        roman_numeral += ((positive_int // 100) * "C")
        positive_int %= 100
    if positive_int//90 > 0:
        roman_numeral += "XC"
        positive_int %= 90
    if positive_int//50 > 0:
        roman_numeral += "L"
        positive_int %= 50
    if positive_int//40 > 0:
        roman_numeral += "XL"
        positive_int %= 40
    if positive_int//10 > 0:
        roman_numeral += ((positive_int // 10) * "X")
        positive_int %= 10
    if positive_int//9 > 0:
        roman_numeral += "IX"
        positive_int %= 9
    if positive_int//5 > 0:
        roman_numeral += "V"
        positive_int %= 5
    if positive_int//4 > 0:
        roman_numeral += "IV"
        positive_int %= 4
    if positive_int//1 > 0:
        roman_numeral += ((positive_int // 1) * "I")
    return roman_numeral


def main():
    print(convert_to_roman_numeral(5000))
    doctest.testmod()


if __name__ == '__main__':
    main()
