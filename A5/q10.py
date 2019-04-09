scientists = {'jgoodall':
              {'surname': 'Goodall',
               'name': 'Jane',
               'born': 1934,
               'died': None,
               'notes': 'Primate research',
               'author': ['In the Shadow of Man', 'The Chimps of Gombe']},
              'rfranklin':
              {'surname': 'Franklin',
               'name': 'Rosalind',
               'born': 1920,
               'died': 1957,
               'notes': 'DNA research'},
              'aturing':
              {'surname': 'Turing',
               'name': 'Alan',
               'born': 1912,
               'died': 1954,
               'notes': 'polymath',
               'author': ['Systems of Logic based on Ordinals']}}


def database_shared_headings(dictionary):
    """Return a set containing all common keys in the inner dictionary."""
    headings_list = [{key for key in inner_dict.keys()} for inner_dict in dictionary.values()]

    shared_headings = set()
    for i in range(1, len(headings_list)):
        shared_headings = headings_list[i].intersection(headings_list[i-1])

    return shared_headings


def main():
    database_shared_headings(scientists)


if __name__ == '__main__':
    main()
