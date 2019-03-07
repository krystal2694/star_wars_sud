"""Imperial forces that the player may encounter."""

imperial_forces = [{"Name": "Stormtrooper", "Type": "imperial", "HP": 5, "Dexterity": 2},
                   {"Name": "Shocktrooper", "Type": "imperial", "HP": 5, "Dexterity": 3},
                   {"Name": "Imperial Officer", "Type": "imperial", "HP": 5, "Dexterity": 4},
                   {"Name": "Bounty Hunter", "Type": "imperial", "HP": 5, "Dexterity": 5},
                   {"Name": "Imperial Spy", "Type": "imperial", "HP": 5, "Dexterity": 5},
                   {"Name": "Sith Lord", "Type": "imperial", "HP": 5, "Dexterity": 6},
                   {"Name": "AT-AT Walker", "Type": "imperial", "HP": 5, "Dexterity": 7}]


def get_name(imperial_index):
    return imperial_forces[imperial_index]["Name"]


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


