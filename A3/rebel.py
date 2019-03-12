"""Rebel character for Star Wars game."""
# A01089672
# Krystal Wong
# 28/02/2019
import sud
import json

line = "-------------------------------------------------------------------\n"

rebel = {"Name": "", "Class": "", "HP": 10, "Dexterity": 5, "Row": 5, "Column": 5}


def get_name()-> str:
    """Return character name."""
    return rebel["Name"]


def set_name()-> None:
    """Set character name."""
    global rebel
    rebel["Name"] = sud.user_quit(input("What is your name, young one? ")).title()


def set_class(rebel_class: str)-> None:
    rebel["Class"] = rebel_class


def get_hp()-> int:
    """Return character HP."""
    return rebel["HP"]


def set_hp(new_hp)-> None:
    """Modify character HP."""
    global rebel
    rebel["HP"] = new_hp


def get_dexterity()-> int:
    """Return character dexterity."""
    return rebel["Dexterity"]


def set_row(row: int)-> None:
    """Modify position of character by row."""
    global rebel
    rebel["Row"] = row


def get_row()-> int:
    """Return character's position by row."""
    return rebel["Row"]


def set_column(column: int)-> None:
    """Modify position of character by column."""
    global rebel
    rebel["Column"] = column


def get_column()-> int:
    """Return character's position by column."""
    return rebel["Column"]


def save_character()-> None:
    """Save character information."""
    filename = 'player_info.json'
    with open(filename, 'w') as file_object:
        json.dump(rebel, file_object)
