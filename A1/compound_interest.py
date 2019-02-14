"""This program calculates the user's account balance with compound interest after a specified number of years."""

# Krystal Wong
# A01089672
# 02/02/2019
import doctest


def compound_interest(principal, annual_interest, compound, years):
    """Calculate the balance of bank account with compound interest after a specific number of years.

    PARAM: principal, a float
    PARAM: annual_interest, a float
    PARAM: compound, an int
    PARAM: years, an int or float
    PRECONDITION: principal must be a positive floating point number
    PRECONDITION: annual_interest must be a positive floating point number
    PRECONDITION: compound must be a positive integer
    PRECONDITION: years must be a positive integer or floating point number
    POSTCONDITION: correctly calculate the balance of the account
    RETURN: correctly calculated account balance as a floating point number

    >>> compound_interest(0.01, 0.1, 2, 5)
    0.01628894626777442
    >>> compound_interest(1000.0, 0.5, 5, 25)
    149308882.421805
    >>> compound_interest(5000.0, 1.2, 15, 50)
    5.845028317662855e+28
    """

    account_balance = principal * ((1 + (annual_interest / compound)) ** (years * compound))
    return account_balance


def main():
    print(compound_interest(1000.00, 0.10, 2, 5))
    doctest.testmod()


if __name__ == '__main__':
    main()
