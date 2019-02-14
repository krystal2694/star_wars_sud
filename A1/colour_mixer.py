"""This program allows the user to determine the secondary colour produced by two primary colours of their choice."""

# Krystal Wong
# A01089672
# 02/02/2019
import doctest


def clean_input(user_input):
    """Return user input stripped of white space, in title case.

    PARAM: user_input, a string
    PRECONDITION: user_input must be a string
    POSTCONDITION: effectively strip white space from parameter and convert to title case
    RETURN: user_input stripped, in title case as a string

    >>> clean_input('RED')
    'Red'
    >>> clean_input(' blue ')
    'Blue'
    >>> clean_input('  CaNdY')
    'Candy'
    """

    user_input_clean = user_input.strip().title()
    return user_input_clean


def colour_mixer():
    """Print the secondary colour produced by two primary colours entered by the user.

    PARAM: prim_colour_1, prim_colour_2
    PRECONDITION: parameters must be 2 different primary colours
    POST-CONDITION: generate correct secondary colour produced by the 2 parameters
    RETURN: secondary colour as a string"""

    prim_colour_1 = clean_input(input("Enter your first primary colour: "))
    prim_colour_2 = clean_input(input("Enter a different primary colour: "))

    if prim_colour_1 == 'Red' and prim_colour_2 == 'Blue' or prim_colour_1 == 'Blue' and prim_colour_2 == 'Red':
        print('Your primary colours make the colour purple!')
    elif prim_colour_1 == 'Red' and prim_colour_2 == 'Yellow' or prim_colour_1 == 'Yellow' and prim_colour_2 == 'Red':
        print('Your primary colours make the colour orange!')
    elif prim_colour_1 == 'Yellow' and prim_colour_2 == 'Blue' or prim_colour_1 == 'Blue' and prim_colour_2 == 'Yellow':
        print('Your primary colours make the colour green!')
    else:
        print('You did not enter two different primary colours. Try again!')


def main():
    colour_mixer()
    doctest.testmod()


if __name__ == '__main__':
    main()
