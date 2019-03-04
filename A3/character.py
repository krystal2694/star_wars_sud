"""Create a Star Wars Character."""
from random import randint
# A01089672
# Krystal Wong


line = "-------------------------------------------------------------------\n"


def choose_name():
    name = input("What is your name, young one? ")
    return name.title()


rebel_class_dict = {1: ["Knowledge", "Jedi"], 2: ["Strength", "Rebel Fighter"], 3: ["Wit", "Smuggler"]}


def choose_rebel_class():
    """Return user's selection of their desired rebel class."""

    for key, value in rebel_class_dict.items():
        print(key, value[0])

    selection = int(input("\n" + "Enter the corresponding number: ").strip())
    print("\n" + line)
    for number, rebel_class in rebel_class_dict.items():
        if selection == number:
            return rebel_class[1]
    else:
        print("You must choose one from the list above.")
        return choose_rebel_class()


def create_rebel(name, rebel_class):
    """Create a member of the Rebellion.

    PARAM: name, a string
    PARAM: rebel class, a string
    PRECONDITION: name must be a string
    PRECONDITION: rebel class must be a string
    POSTCONDITION: create a rebel complete with name, Type, HP, Dexterity
    RETURN: a dictionary consisting of all information required for a new member of the Rebellion
    """

    rebel = {"Name": name,
             "Class": rebel_class,
             "HP": 10,
             "Dexterity": randint(1, 10),
             "Coordinates": [5, 5]}

    return rebel


def print_rebel(rebel):
    """Print the parameter.

    PARAM: character, a dictionary
    PRECONDITION: character must be a dictionary
    POSTCONDITION: print contents of parameter in a nice format
    RETURN: a nicely formatted string
    """

    for key, value in rebel.items():
        print(key + ": " + str(value))


def main():
    print(choose_rebel_class())


if __name__ == '__main__':
    main()
