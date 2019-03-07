"""Imperial forces that the player may encounter."""

imperial_forces = [{"Name": "Stormtrooper", "HP": 5, "Dexterity": 2},
                   {"Name": "Shocktrooper", "HP": 5, "Dexterity": 3},
                   {"Name": "Imperial Officer", "HP": 5, "Dexterity": 4},
                   {"Name": "Bounty Hunter",  "HP": 5, "Dexterity": 5},
                   {"Name": "Imperial Spy", "HP": 5, "Dexterity": 5},
                   {"Name": "Sith Lord", "HP": 5, "Dexterity": 6},
                   {"Name": "AT-AT Walker", "HP": 5, "Dexterity": 7}]


def get_name(index):
    return imperial_forces[index]["Name"]


def get_hp(index):
    return imperial_forces[index]["HP"]


def set_hp(index, new_hp):
    global imperial_forces
    imperial_forces[index]["HP"] = new_hp


def decrease_hp(index, damage):
    global imperial_forces
    imperial_forces[index]["HP"] -= damage


def get_dexterity(index):
    return imperial_forces[index]["Dexterity"]


