# Krystal Wong
# A01089672
# Theoren Leveille
# A01070327
# 05/04/2019
import doctest


def is_all_strings(my_list):
    """Determine if all items in the list are strings.

    >>> is_all_strings(["a", "bee", "car", "d", "r"])
    True
    >>> is_all_strings(["a", "bee", 3, "d", 10])
    False

    """
    if all(isinstance(item, str) for item in my_list):
        return True
    else:
        return False


def is_all_numbers(my_list):
    """Determine if all items in the list are integers or floats.

     >>> is_all_numbers([2, 8, 1, 2.3, 8.9, 100])
    True
    >>> is_all_numbers(["a", "bee", 3, "d", 10])
    False

    """
    if all((isinstance(item, int) or isinstance(item, float)) for item in my_list):
        return True
    else:
        return False


def main():
    # my_list = [9, 1, 6, 3, 10, 3, 3, 6]
    my_list = ['a', 'the', 'bee', 'zoo', 'a', 'the']
    print(selection_sort(my_list))
    # print(is_all_numbers(my_list))
    # print(sort_items(index, my_list))
    doctest.testmod()


if __name__ == '__main__':
    main()
