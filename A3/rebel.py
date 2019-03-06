"""Rebel character for Star Wars game."""
from random import randint

rebel = {"Name": "", "Class": "", "HP": 10, "Dexterity": randint(5, 10), "Coordinates": [5, 5]}


def get_name():
    return rebel["Name"]


def set_name():
    name = input("What is your name, young one? ")
    rebel["Name"] = name


def get_hp():
    return rebel["HP"]


def increment_hp(integer):
    rebel["HP"] += 1
    return rebel


def get_dexterity():
    return rebel["Dexterity"]





