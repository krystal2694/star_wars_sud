# Krystal Wong
# A01089672
# Theoren Leveille
# A01070327
# 09/04/2019
import re
import doctest


def is_strong_password(password: str)-> bool:
        """Return True if password is strong.

        >>> is_strong_password("Peanut1234")
        True
        >>> is_strong_password("disneyland")
        False
        """
        password_length_regex = re.compile(r'\w{8,}')
        password_uppercase_regex = re.compile(r'[A-Z]+')
        password_lowercase_regex = re.compile(r'[a-z]+')
        password_digit_regex = re.compile(r'\d+')

        match_object_length = password_length_regex.search(password)
        match_object_uppercase = password_uppercase_regex.search(password)
        match_object_lowercase = password_lowercase_regex.search(password)
        match_object_digit = password_digit_regex.search(password)

        if match_object_length and match_object_uppercase and match_object_lowercase and match_object_digit:
            return True
        else:
            return False


def main():
    password = "Peanut1234"
    print(is_strong_password(password))
    doctest.testmod()


if __name__ == '__main__':
    main()
