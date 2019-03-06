"""Rebel character for Star Wars game."""
from random import randint

rebel = {"Name": "", "Class": "", "HP": 10, "Dexterity": randint(5, 10), "Coordinates": [5, 5]}


def get_name():
    return rebel["Name"]


def choose_name():
    name = input("What is your name, young one? ")
    rebel["Name"] = name


def get_hp():
    return rebel["HP"]


def increment_hp():
    rebel["HP"] += 1
    return rebel


def decrease_hp(damage):
    rebel["HP"] -= damage


def get_dexterity():
    return rebel["Dexterity"]


def get_coordinates():
    return rebel["Coordinates"]


def set_coordinates(direction):
    if direction == "n" and rebel["Coordinates"][0] != 0:
            rebel["Coordinates"][0] -= 1
    elif direction == "s" and rebel["Coordinates"][0] != 10:
            rebel["Coordinates"][0] += 1
    elif direction == "e" and rebel["Coordinates"][1] != 10:
            rebel["Coordinates"][1] += 1
    elif direction == "w" and rebel["Coordinates"][1] != 0:
            rebel["Coordinates"][1] -= 1
    else:
        print("Do not leave the galaxy %s, you cannot leave us in the hands of the Galactic Empire!" % rebel["Name"])
        return rebel





