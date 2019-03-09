"""Imperial forces that the player may encounter."""
import doctest

imperial_forces = [{"Name": "Stormtrooper", "HP": 5, "Dexterity": 2},
                   {"Name": "Shocktrooper", "HP": 5, "Dexterity": 3},
                   {"Name": "Imperial Officer", "HP": 5, "Dexterity": 4},
                   {"Name": "Bounty Hunter",  "HP": 5, "Dexterity": 5},
                   {"Name": "Imperial Spy", "HP": 5, "Dexterity": 5},
                   {"Name": "Sith Lord", "HP": 5, "Dexterity": 6},
                   {"Name": "AT-AT Walker", "HP": 5, "Dexterity": 7}]


def get_name(index: int)-> str:
    """Return imperial force name.
    >>> get_name(3)
    'Bounty Hunter'
    >>> get_name(6)
    'AT-AT Walker'
    """
    return imperial_forces[index]["Name"]


def get_hp(index: int)-> int:
    """Return imperial force HP.
    >>> get_hp(5)
    5
    >>> get_hp(0)
    5
    """
    return imperial_forces[index]["HP"]


def set_hp(index: int, new_hp: int):
    """Modify imperial force HP."""
    global imperial_forces
    imperial_forces[index]["HP"] = new_hp


def decrease_hp(index: int, damage: int):
    """Decrease imperial force HP by the damage amount."""
    global imperial_forces
    imperial_forces[index]["HP"] -= damage


def get_dexterity(index: int)-> int:
    """Return imperial force dexterity.
    >>> get_dexterity(0)
    2
    >>> get_dexterity(4)
    5
    """
    return imperial_forces[index]["Dexterity"]


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
