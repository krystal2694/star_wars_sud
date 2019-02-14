"""This program helps the user translate their fun phone number into a numerical phone number."""

# Krystal Wong
# A01089672
# 02/02/2019
import doctest


def clean_input_upper(user_input):
    """Return user input stripped of white space, in upper case.

    PARAM: user_input, a string
    PRECONDITION: user_input must be a string
    POSTCONDITION: effectively strip white space from parameter and convert to upper case
    RETURN: user_input stripped, in upper case as a string

    >>> clean_input_upper('food')
    'FOOD'
    >>> clean_input_upper(' pizza ')
    'PIZZA'
    >>> clean_input_upper('  FaSt')
    'FAST'
    """

    clean_input = user_input.strip().upper()
    return clean_input


def letter_translator(x):
    """Convert letter to corresponding phone number digit.

    PARAM: x, a string
    PRECONDITION: x must be a string
    POSTCONDITION: string will be converted to corresponding phone number digit if necessary
    RETURN: digit as a string

    >>>
    letter_translator("A")
    2
    >>>
    letter_translator("Z")
    9
    >>>
    letter_translator("-")
    -
    >>>
    letter_translator("6")
    6
    """

    digit = x
    if x == "A" or x == "B" or x == "C":
        digit = "2"
    elif x == "D" or x == "E" or x == "F":
        digit = "3"
    elif x == "G" or x == "H" or x == "I":
        digit = "4"
    elif x == "J" or x == "K" or x == "L":
        digit = "5"
    elif x == "M" or x == "N" or x == "O":
        digit = "6"
    elif x == "P" or x == "Q" or x == "R" or x == "S":
        digit = "7"
    elif x == "T" or x == "U" or x == "V":
        digit = "8"
    elif x == "W" or x == "X" or x == "Y" or x == "Z":
        digit = "9"
    elif x == "-":
        digit = "-"
    return digit


def number_translator(clean_user_input):
    """Concatenate the converted indices of parameter into one string.

    PARAM:clean_user_input, a string
    PRECONDITION:clean_user_input must be a string in the format 'XXX-XXX-XXXX'
    POSTCONDITION:convert each index of the parameter
    RETURN: final_number as a string"""

    final_number = ""
    final_number += str(letter_translator(clean_user_input[0]))
    final_number += str(letter_translator(clean_user_input[1]))
    final_number += str(letter_translator(clean_user_input[2]))
    final_number += str(letter_translator(clean_user_input[3]))
    final_number += str(letter_translator(clean_user_input[4]))
    final_number += str(letter_translator(clean_user_input[5]))
    final_number += str(letter_translator(clean_user_input[6]))
    final_number += str(letter_translator(clean_user_input[7]))
    final_number += str(letter_translator(clean_user_input[8]))
    final_number += str(letter_translator(clean_user_input[9]))
    final_number += str(letter_translator(clean_user_input[10]))
    final_number += str(letter_translator(clean_user_input[11]))
    return final_number


def main():
    user_number = clean_input_upper(input("Enter your fun phone number in the format XXX-XXX-XXXX: "))
    print(number_translator(user_number))
    doctest.testmod()


if __name__ == '__main__':
    main()
