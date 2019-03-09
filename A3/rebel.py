"""Rebel character for Star Wars game."""
import sud
import json

line = "-------------------------------------------------------------------\n"

rebel = {"Name": "", "Class": "", "HP": 10, "Dexterity": 5, "Row": 5, "Column": 5}


def get_name()-> str:
    """Return character name.
    >>> get_name()
    ''
    """
    return rebel["Name"]


def set_name():
    """Set character name."""
    global rebel
    rebel["Name"] = sud.user_quit(input("What is your name, young one? ")).title()


def set_class(rebel_class: str):
    rebel["Class"] = rebel_class


def get_hp()-> int:
    """Return character HP.
    >>> get_hp()
    10
    """
    return rebel["HP"]


def set_hp(new_hp):
    """Modify character HP."""
    global rebel
    rebel["HP"] = new_hp


def get_dexterity()-> int:
    """Return character dexterity.
    >>> get_dexterity()
    5
    """
    return rebel["Dexterity"]


def set_row(row: int):
    """Modify position of character by row."""
    global rebel
    rebel["Row"] = row


def get_row():
    """Return character's position by row.
    >>> get_row()
    5
    """
    return rebel["Row"]


def set_column(column: int):
    """Modify position of character by column."""
    global rebel
    rebel["Column"] = column


def get_column():
    """Return character's position by column.
    >>> get_column()
    5
    """
    return rebel["Column"]


def save_character():
    """Save character information."""
    filename = 'player_info.json'
    with open(filename, 'w') as file_object:
        json.dump(rebel, file_object)


def main():
    pass


if __name__ == '__main__':
    main()
