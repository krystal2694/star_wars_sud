"""This program allows the user to create a new character and play a single round of Dungeons and Dragons"""
# Krystal Wong
# A01089672
# 08/02/2019
import random


def roll_die(number_of_rolls, number_of_sides):
    """Calculate the result of rolling a multi-sided die a specified number of times.

    PARAM: number_of_rolls, an integer
    PARAM: number_of_sides, an integer
    PRECONDITION: number_of_rolls must be a positive integer
    PRECONDITION: number_of_sides must be a positive integer
    POSTCONDITION: correctly calculate the sum of the dice rolls
    RETURN: the sum of the dice rolls

    >>> random.seed(9)
    >>> roll_die(1, 20)
    15
    >>> random.seed(78)
    >>> roll_die(3, 6)
    6
    >>> random.seed()
    """

    if number_of_sides <= 0 or number_of_rolls <= 0:
        return 0
    else:
        roll = random.randint(1, number_of_sides)
        dice_rolls = [roll for _ in range(number_of_rolls)]
        total = sum(dice_rolls)
        return total


def choose_inventory(inventory, selection):
    """Create new list with a specified number of random elements taken from the list provided.

    PARAM: inventory, a list
    PARAM: selection, an integer
    PRECONDITION: inventory must be a list
    PRECONDITION: selection must be a positive integer
    POSTCONDITION: generate a sorted list of the specified number of randomly selected elements
    RETURN: a sorted list with specified number of elements

    >>> my_list = ['c', 'b', 'a', 'f', 'd', 'e']
    >>> choose_inventory(my_list, 0)
    []
    >>> choose_inventory(my_list, 6)
    ['a', 'b', 'c', 'd', 'e', 'f']
    >>> random.seed(25)
    >>> choose_inventory(my_list, 3)
    ['b', 'c', 'f']
    >>> random.seed()
    """

    if len(inventory) == 0 and selection == 0:
        return []
    elif selection < 0:
        print("Selection must be a positive integer!")
        return None
    elif selection > len(inventory):
        print("Selection is greater than the total number of your inventory!")
        return None
    elif selection == len(inventory):
        new_list = inventory[:]
        return sorted(new_list)
    else:
        new_list = sorted(random.sample(inventory, selection))
        return new_list


def generate_vowel():
    """Generate a random vowel.

    >>> random.seed(36)
    >>> generate_vowel()
    'i'
    >>> random.seed()
    """

    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    random_vowel = random.choice(vowels)
    return random_vowel


def generate_consonant():
    """Generate a random consonant.

    >>> random.seed(54)
    >>> generate_consonant()
    'g'
    >>> random.seed()
    """

    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                  'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    random_consonant = random.choice(consonants)
    return random_consonant


def generate_syllable():
    """Concatenate a randomly generated consonant with a randomly generated vowel.

    >>> random.seed(33)
    >>> generate_syllable()
    'xe'
    >>> random.seed()

    """

    random_syllable = generate_consonant() + generate_vowel()
    return random_syllable


def generate_name(num_syllables):
    """Generate a random name consisting of the number of syllables specified by the parameter.

    PARAM: num_syllables, an integer
    PRECONDITION: num_syllables must be a positive integer
    POSTCONDITION: generate a random name with the specified number of syllables
    RETURN: a randomized string in title case

    >>> random.seed(64)
    >>> generate_name(3)
    'Tazuqu'
    >>> random.seed(11)
    >>> generate_name(1)
    'Su'
    >>> random.seed(53)
    >>> generate_name(10)
    'Yesutyvisybahigiceci'
    >>> random.seed()
    """

    num_syllables = [generate_syllable() for _ in range(num_syllables)]
    name = "".join(num_syllables)
    name = name.title()
    return name


def select_class():
    """Return user's selection of their desired class."""

    classes = {1: "barbarian", 2: "bard", 3: "cleric", 4: "druid", 5: "fighter", 6: "monk",
               7: "paladin", 8: "ranger", 9: "rogue", 10: "sorcerer", 11: "warlock", 12: "wizard"}
    print("------------------------------------------------")
    print("Choose your new character's class by entering the class's corresponding number.")
    for key, value in classes.items():
        print(key, value)

    print("------------------------------------------------")
    selection = int(input("Enter your selection here: ").strip())
    for number, char_class in classes.items():
        if selection == number:
            return char_class
    else:
        print("You must choose a class from the list above.")
        return select_class()


class_initial_hd = {"barbarian": 12, "bard": 8, "cleric": 8, "druid": 8, "fighter": 10, "monk": 8,
                    "paladin": 10, "ranger": 10, "rogue": 8, "sorcerer": 6, "warlock": 8, "wizard": 6}


def create_character(syllables):
    """Create a Dungeons and Dragons character.

    PARAM: syllables, an integer
    PRECONDITION: syllables must be a positive integer
    POSTCONDITION: generate a Dungeons and Dragons character complete with name, class, HP,
    attributes and their corresponding values, XP, and inventory
    RETURN: a dictionary consisting of all information required for a new Dungeons and Dragons character
    """
    if syllables <= 0:
        print("syllables must be a positive integer!")
        return None

    character_class = select_class()

    character = {"Name": generate_name(syllables),
                 "Class": character_class,
                 "HP": 0,
                 "Strength": roll_die(3, 6),
                 "Dexterity": roll_die(3, 6),
                 "Constitution": roll_die(3, 6),
                 "Intelligence": roll_die(3, 6),
                 "Wisdom": roll_die(3, 6),
                 "Charisma": roll_die(3, 6),
                 "XP": 0,
                 "Inventory": []}

    for ch_class, initial_hd in class_initial_hd.items():
        if character_class == ch_class:
            character["HP"] = roll_die(1, initial_hd)

    return character


def determine_order():
    """Determine which character attacks first by rolling a 20 sided die once each.

    >>> random.seed(27)
    >>> determine_order()
    True
    >>> random.seed(8)
    >>> determine_order()
    False
    """

    opponent_one_roll = roll_die(1, 20)
    opponent_two_roll = roll_die(1, 20)
    if opponent_one_roll > opponent_two_roll:
        return True
    elif opponent_two_roll > opponent_one_roll:
        return False
    elif opponent_one_roll == opponent_two_roll:
        return determine_order()


def combat_round(opponent_one, opponent_two):
    """ Allow user to play one single round of combat.

    PARAM: opponent_one, a dictionary
    PARAM: opponent_two, a dictionary
    PRECONDITION: opponent_one must be a dictionary containing a complete character
    PRECONDITION: opponent_two must be a dictionary containing a complete character
    """

    first_attack = determine_order()

    if first_attack is True:
        attacker = opponent_one
        defender = opponent_two

    else:
        attacker = opponent_two
        defender = opponent_one

    print(attacker["Name"] + " goes first:")
    defender = attack(attacker, defender)
    if defender["HP"] > 0:
            print(defender["Name"] + "'s turn:")
            attacker = attack(defender, attacker)
            if attacker["HP"] > 0:
                print("End of round -->",
                      attacker["Name"] + "'s HP is " + str(attacker["HP"]) + ".",
                      defender["Name"] + "'s HP is " + str(defender["HP"]) + ".")


def attack(offence_char, defence_char):
    """Simulate the attack of the character on offence on the character on defense.

    PARAM: offence_char, a dictionary
    PARAM: defence_chr, a dictionary
    PRECONDITION: offence_char must be a dictionary containing a complete character
    PRECONDITION: defence_char must be a dictionary containing a complete character
    POSTCONDITION: determine if the attack was successful, modify defence_char's HP if it was
    RETURN: defence_char as a dictionary """

    print(offence_char["Name"] + " strikes!")
    damage = 0
    for ch_class, initial_hd in class_initial_hd.items():
        if offence_char["Class"] == ch_class:
            damage = roll_die(1, initial_hd)

    offence_attack = roll_die(1, 20)
    if offence_attack > defence_char["Dexterity"]:
        defence_char["HP"] -= damage
        print(defence_char["Name"] + " has taken a " + str(damage) + " point hit!")
        if defence_char["HP"] <= 0:
            print(defence_char["Name"] + " has perished.")
            print("End of round --> " + offence_char["Name"] + " is the winner!")
        else:
            print(defence_char["Name"] + "'s HP has dropped to " + str(defence_char["HP"]) + ".")
    else:
        print(offence_char["Name"] + " missed!")
    return defence_char


def print_character(character):
    """Print the parameter.

    PARAM: character, a dictionary
    PRECONDITION: character must be a dictionary
    POSTCONDITION: print contents of parameter in a nice format
    RETURN: a nicely formatted string
    """

    print("Here is your new character!")
    for key, value in character.items():
        print(key + ": " + str(value))


def main():
    """One round of combat in Dungeons and Dragons, Woo!"""
    print("------------------------------------------------\n"
          "Welcome to Dungeons and Dragons!\n" 
          "------------------------------------------------")
    print("Let's create two characters for combat.")
    store = ["The Philosopher's Stone", "The Unicorn Horn", "The Elder Wand", "The Ring of Winter",
             "The Rod of Seven Parts", "The Sphere of Annihilation", "The Deck of Many Things",
             "The Staff of Magi", "The Black Rose", "The Belmont Whip"]

    char_1 = create_character(int(input("How many syllables would you like you first character's name to be? ")))
    print("------------------------------------------------")
    char_1_items = int(input("There are 10 items in the store, how many would you like to select? "))
    char_1_inventory = choose_inventory(store, char_1_items)
    if len(char_1_inventory) > 0:
            char_1["Inventory"] = char_1_inventory
    print("------------------------------------------------")
    print_character(char_1)

    print("------------------------------------------------")
    char_2 = create_character(int(input("How many syllables would you like you second character's name to be? ")))
    print("------------------------------------------------")
    char_2_items = int(input("There are 10 items in the store, how many would you like to select? "))
    char_2_inventory = choose_inventory(store, char_2_items)
    if len(char_2_inventory) > 0:
            char_2["Inventory"] = char_2_inventory
    print("------------------------------------------------")
    print_character(char_2)

    print("------------------------------------------------")
    print("Time for combat!")
    print("------------------------------------------------")
    combat_round(char_1, char_2)


if __name__ == '__main__':
    main()
