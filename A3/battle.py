"""Battle between two Pokemon."""
from random import randint


def determine_order():
    """Determine which character attacks first by rolling a 20 sided die once each.

    >>> random.seed(27)
    >>> determine_order()
    True
    >>> random.seed(8)
    >>> determine_order()
    False
    >>> random.seed()
    """

    opponent_one_roll = randint(1, 20)
    opponent_two_roll = randint(1, 20)
    if opponent_one_roll > opponent_two_roll:
        return True
    elif opponent_two_roll > opponent_one_roll:
        return False
    elif opponent_one_roll == opponent_two_roll:
        return determine_order()


def attack(offence_char, defence_char):
    """Simulate the attack of the character on offence on the character on defense.

    PARAM: offence_char, a dictionary
    PARAM: defence_chr, a dictionary
    PRECONDITION: offence_char must be a dictionary containing a complete character
    PRECONDITION: defence_char must be a dictionary containing a complete character
    POSTCONDITION: determine if the attack was successful, modify defence_char's HP accordingly
    RETURN: defence_char as a dictionary """

    print(offence_char["Name"] + " strikes!")
    damage = randint(1, 6)

    offence_attack = randint(1, 10)
    if offence_attack > defence_char["Dexterity"]:
        defence_char["HP"] -= damage
        print(defence_char["Name"] + " has taken a " + str(damage) + " point hit!")
        if defence_char["HP"] <= 0:
            print(defence_char["Name"] + " has perished.")
            print(offence_char["Name"] + " is the winner!")
        else:
            print(defence_char["Name"] + "'s HP has dropped to " + str(defence_char["HP"]) + ".")
    else:
        print(offence_char["Name"] + " missed!")
    return defence_char


