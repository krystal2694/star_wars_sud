# Krystal Wong
# A01089672
# Theoren Leveille
# A01070327
# 05/04/2019
import doctest


def selection_sort(my_list: list)-> list:
    """Return a sorted copy of list.

    PRECONDITION: my_list must be a non-empty list of sortable items.
    POSTCONDITION: sort the list provided
    >>> selection_sort(['a', 'the', 'bee', 'zoo', 'a', 'the'])
    ['a', 'a', 'bee', 'the', 'the', 'zoo']
    >>> selection_sort([10, 3, 7, 9, 3, 9, 1])
    [1, 3, 3, 7, 9, 9, 10]
    """

    list_copy = my_list[:]
    if len(list_copy) == 0:
        raise ValueError('List cannot be empty')
    if is_all_numbers(list_copy) or is_all_strings(list_copy) or is_valid_data_structure(list_copy):
        return sort_items(0, list_copy)
    else:
        raise ValueError('list not sortable.')


def sort_items(position: int, item_list: list):
    """Sort a list of sortable items.

    PRECONDITION: my_list must be a non-empty list of sortable items.
    POSTCONDITION: sort the list provided
    >>> sort_items(0, ['a', 'the', 'bee', 'zoo', 'a', 'the'])
    ['a', 'a', 'bee', 'the', 'the', 'zoo']
    >>> sort_items(0, [10, 3, 7, 9, 3, 9, 1])
    [1, 3, 3, 7, 9, 9, 10]
    """
    if position == len(item_list) - 1:
        return item_list
    else:
        beginning_value = item_list[position]  # captures item at starting position
        for item in item_list[position:]:
            if item == min(item_list[position:]):
                min_value_index = item_list[position:].index(item) + position  # captures index of smallest value
                item_list[position] = item
                item_list[min_value_index] = beginning_value
                return sort_items(position + 1, item_list)


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


def is_valid_data_structure(my_list: list)-> bool:
    data_structure_type = type(my_list[0])
    for item in my_list:
        if type(item) == data_structure_type:
            continue
        else:
            raise ValueError("Elements of list must be the same type!")
    inner_item_type = type(my_list[0][0])
    for item in my_list:
        if type(item[0]) == inner_item_type:
            continue
        else:
            raise ValueError("First element of each inner data structure must be of the same type!")
    return True


def main():
    # my_list = [9, 1, 6, 3, 10, 3, 3, 6]
    my_list = [['a'], ['the', 2, []], ['bee', 3], ['sdha', 3]]
    # check_data_structure(my_list)
    print(selection_sort(my_list))
    # print(sort_items(0, my_list))
    # print(is_all_numbers(my_list))
    # print(sort_items(index, my_list))
    doctest.testmod()


if __name__ == '__main__':
    main()
