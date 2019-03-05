"""Battle between two Star Wars characters."""
from random import randint
import sud

line = "-------------------------------------------------------------------\n"


def attack(offence_char, defence_char):
    """Simulate the attack of the character on offence on the character on defense.

    PARAM: offence_char, a dictionary
    PARAM: defence_chr, a dictionary
    PRECONDITION: offence_char must be a dictionary containing a complete character
    PRECONDITION: defence_char must be a dictionary containing a complete character
    POSTCONDITION: determine if the attack was successful, modify defence_char's HP accordingly
    RETURN: defence_char as a dictionary """

    print(offence_char["Name"] + " strikes!")
    damage = randint(1, 6)

    offence_attack = randint(1, 20)
    if offence_attack > defence_char["Dexterity"]:
        defence_char["HP"] -= damage
        print("%s has taken a %d point hit!" % (defence_char["Name"], damage))
        if defence_char["HP"] <= 0:
            print("%s has been defeated.\n" % defence_char["Name"])
        else:
            print("Their HP has dropped to %d.\n" % defence_char["HP"])
    else:
        print("%s evaded the attack!\n" % defence_char["Name"])
    return defence_char


def combat_round(rebel, imperial):
    """ Allow user to play one single round of combat.

    PARAM: opponent_one, a dictionary
    PARAM: opponent_two, a dictionary
    PRECONDITION: opponent_one must be a dictionary containing a complete jedi
    PRECONDITION: opponent_two must be a dictionary containing a complete jedi
    """
    print("\n" + line)
    while rebel["HP"] > 0 and imperial["HP"] > 0:
        rebel = attack(imperial, rebel)
        if rebel["HP"] <= 0:
            break
        else:
            imperial = attack(rebel, imperial)

    if rebel["HP"] > 0:
        print("%s's HP is %d.\n\n" % (rebel["Name"], rebel["HP"]) + line + "\n")
    imperial["HP"] = 5
    return rebel


imperial_forces = [{"Name": "Stormtrooper", "HP": 5, "Dexterity": 5},
                   {"Name": "Shocktrooper", "HP": 5, "Dexterity": 6},
                   {"Name": "Imperial Officer", "HP": 5, "Dexterity": 7},
                   {"Name": "Bounty Hunter", "HP": 5, "Dexterity": 7},
                   {"Name": "Imperial Spy", "HP": 5, "Dexterity": 8},
                   {"Name": "Sith Lord", "HP": 5, "Dexterity": 9},
                   {"Name": "AT-AT Walker", "HP": 5, "Dexterity": 10}]


def encounter_imperial(rebel):
    if randint(1, 10) == 1:
        imperial = imperial_forces[randint(0, 6)]
        fight_or_run = 0
        while fight_or_run != "f" and fight_or_run != "r":
            fight_or_run = input("\nYou have encountered a(n) %s!\n\nYour current have %dHP. 'f' to fight"
                                 ", 'r' to run away: " % (imperial["Name"], rebel["HP"])).strip().lower()
            if fight_or_run == "f":
                combat_round(rebel, imperial)
                if rebel["HP"] <= 0:
                    return rebel
            elif fight_or_run == "r":
                if randint(1, 10) == 1:
                    damage = randint(1, 4)
                    rebel["HP"] -= damage
                    print("%s struck you as you fled! You have taken a %d point hit." % (imperial["Name"], damage))
                else:
                    print("\nYou fled the scene unharmed!")
        sud.print_game_map(sud.create_game_map(rebel))
    return rebel


def main():
    imperial = {"Name": "Stormtrooper", "HP": 5, "Dexterity": 5}
    rebel = {"Name": "Krystal", "HP": 10, "Dexterity": 5}
    combat_round(rebel, imperial)


if __name__ == '__main__':
    main()

