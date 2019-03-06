"""Imperial forces that the player may encounter."""

imperial_forces = [{"Name": "Stormtrooper", "Type": "imperial", "HP": 5, "Dexterity": 5},
                   {"Name": "Shocktrooper", "Type": "imperial", "HP": 5, "Dexterity": 6},
                   {"Name": "Imperial Officer", "Type": "imperial", "HP": 5, "Dexterity": 7},
                   {"Name": "Bounty Hunter", "Type": "imperial", "HP": 5, "Dexterity": 7},
                   {"Name": "Imperial Spy", "Type": "imperial", "HP": 5, "Dexterity": 8},
                   {"Name": "Sith Lord", "Type": "imperial", "HP": 5, "Dexterity": 9},
                   {"Name": "AT-AT Walker", "Type": "imperial", "HP": 5, "Dexterity": 10}]


def get_name(imperial_index):
    return imperial_forces[imperial_index]["Name"]


def get_type():
    return "imperial"


def get_hp(imperial_index):
    return imperial_forces[imperial_index]["HP"]


def set_hp(imperial_index, new_hp):
    global imperial_forces
    imperial_forces[imperial_index]["HP"] = new_hp


def decrease_hp(imperial_index, damage):
    global imperial_forces
    imperial_forces[imperial_index]["HP"] -= damage


def get_dexterity(imperial_index):
    return imperial_forces[imperial_index]["Dexterity"]


