"""Rebel character for Star Wars game."""
import sud

line = "-------------------------------------------------------------------\n"

rebel_class_dict = {"1": ["Knowledge", "Jedi"], "2": ["Strength", "Rebel Fighter"], "3": ["Wit", "Smuggler"]}

rebel = {"Name": "", "Type": "rebel", "Class": "", "HP": 10, "Dexterity": 8, "Coordinates": [5, 5]}


def get_name():
    return rebel["Name"]


def choose_name():
    global rebel
    rebel["Name"] = input("What is your name, young one? ").title()


def get_type():
    return "rebel"


def choose_rebel_class(name):
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
        return choose_rebel_class(rebel["Name"])


def get_hp():
    return rebel["HP"]


def set_hp(new_hp):
    global rebel
    rebel["HP"] = new_hp


def increment_hp():
    global rebel
    rebel["HP"] += 1


def decrease_hp(damage):
    global rebel
    rebel["HP"] -= damage


def get_dexterity():
    return rebel["Dexterity"]


def get_coordinates():
    return rebel["Coordinates"]


def set_coordinates(coordinates):
    global rebel
    rebel["Coordinates"] = coordinates


def move_character(direction):
    global rebel
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
    sud.print_game_map()


def get_player_info():
    return rebel


def main():
    print(get_hp())
    increment_hp()
    print(get_hp())


if __name__ == '__main__':
    main()
