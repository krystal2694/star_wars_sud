"""Rebel character for Star Wars game."""
import sud
import json

line = "-------------------------------------------------------------------\n"

rebel = {"Name": "", "Class": "", "HP": 10, "Dexterity": 5, "Row": 5, "Column": 5}


def get_name()-> str:
    """Return rebel name.
    >>> get_name()
    ''
    """
    return rebel["Name"]


def set_name():
    """Allow user to choose name for their rebel character."""
    global rebel
    rebel["Name"] = input("What is your name, young one? ").title()


def set_class(rebel_class: str):
    rebel["Class"] = rebel_class


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


def set_row(row: int):
    """Modify position of rebel by row."""
    global rebel
    rebel["Row"] = row


def get_row():
    """Return row position of rebel."""
    return rebel["Row"]


def set_column(column: int):
    """Modify position of rebel by row."""
    global rebel
    rebel["Column"] = column


def get_column():
    """Return column position of rebel."""
    return rebel["Column"]


def save_character():
    filename = 'player_info.json'
    with open(filename, 'w') as file_object:
        json.dump(rebel, file_object)


def main():
    # choose_rebel_class("Krystal")
    sud.print_game_map()


if __name__ == '__main__':
    main()
