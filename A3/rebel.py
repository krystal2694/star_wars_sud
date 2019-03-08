"""Rebel character for Star Wars game."""
import sud
import json

line = "-------------------------------------------------------------------\n"

rebel_class_dict = {"1": ["Knowledge", "Jedi"], "2": ["Strength", "Rebel Fighter"], "3": ["Wit", "Smuggler"]}

rebel = {"Name": "", "Class": "", "HP": 10, "Dexterity": 5, "Position": [5, 5]}


def get_name()-> str:
    """Return rebel name.
    >>> get_name()
    ''
    """
    return rebel["Name"]


def choose_name():
    """Allow user to choose name for their rebel character."""
    global rebel
    rebel["Name"] = input("What is your name, young one? ").title()


def choose_rebel_class(name: str):
    """Return user's selection of their desired rebel class."""

    global rebel
    selection = input("\n" + line + "\nTell me, %s, what do you consider to be your most valuable trait?\n\n"
                                    "1 Knowledge\n2 Strength\n3 Wit\n\nEnter the corresponding number: " % name).strip()
    for number, rebel_class in rebel_class_dict.items():
        if selection == number:
            print("\n" + line + "\nAh! I think you would make a great.. %s!\n" % rebel_class[1] +
                  "\nNow, come with me %s.\n\nWe have a galaxy to save!\n\n" % name + line)
            rebel["Class"] = rebel_class[1]
            return None
    else:
        print("You must choose one from the list above.")
        return choose_rebel_class(get_name())


def get_hp()-> int:
    """Return HP of rebel.
    >>> get_hp()
    10
    """
    return rebel["HP"]


def set_hp(new_hp):
    """Modify HP of rebel."""
    global rebel
    rebel["HP"] = new_hp


def increment_hp():
    """Increment rebel HP by 1."""
    global rebel
    if rebel["HP"] < 10:
        rebel["HP"] += 1
        print("You're healing! Your HP is %d." % rebel["HP"])


def decrease_hp(damage: int):
    """Decrease rebel HP by the damage amount."""
    global rebel
    rebel["HP"] -= damage


def get_dexterity()-> int:
    """Return dexterity of rebel.
    >>> get_dexterity()
    5
    """
    return rebel["Dexterity"]


def get_position()-> list:
    """Return position of rebel.
    >>> get_position()set_hp()
    [5, 5]
    """
    return rebel["Position"]


def set_position(position: list):
    global rebel
    rebel["Position"] = position


def set_row(row: int):
    """Modify position of rebel by row."""
    global rebel
    rebel["Position"][0] = row


def set_column(column: int):
    """Modify position of rebel by row."""
    global rebel
    rebel["Position"][1] = column


def get_player_info()-> dict:
    """Return rebel dictionary.
    >>> get_player_info()
    {'Name': '', 'Class': '', 'HP': 10, 'Dexterity': 5, 'Position': [5, 5]}
    """
    return rebel


def save_character():
    filename = 'player_info.json'
    with open(filename, 'w') as file_object:
        json.dump(rebel, file_object)


def main():
    # choose_rebel_class("Krystal")
    sud.print_game_map()


if __name__ == '__main__':
    main()
