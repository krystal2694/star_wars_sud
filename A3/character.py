"""Create a Star Wars Character."""
from random import randint
# A01089672
# Krystal Wong


line = "-------------------------------------------------------------------\n"


def choose_name():
    name = input("What is your name, young one? ")
    return name.title()


rebel_class_dict = {"1": ["Knowledge", "Jedi"], "2": ["Strength", "Rebel Fighter"], "3": ["Wit", "Smuggler"]}


def choose_rebel_class(name):
    """Return user's selection of their desired rebel class."""

    selection = input("\n" + line + "\nTell me, %s, what do you consider to be your most valuable trait?\n\n"
                                    "1 Knowledge\n2 Strength\n3 Wit\n\nEnter the corresponding number: " % name).strip()

    for number, rebel_class in rebel_class_dict.items():
        if selection == number:
            print("\n" + line + "\nAh! You would make a great.. %s!\n" % rebel_class[1] +
                  "\nNow, come with me %s.\n\nWe have a galaxy to save!\n\n" % name + line)
            return rebel_class[1]
    else:
        print("You must choose one from the list above.")
        return choose_rebel_class(name)


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


def main():
    choose_rebel_class("Kylo")


if __name__ == '__main__':
    main()
