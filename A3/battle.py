"""Battle between two Star Wars characters."""
from random import randint
import sud
import imperial
import rebel


line = "-------------------------------------------------------------------\n"


def encounter_imperial():
    if randint(1, 5) == 1:
        index = randint(0, 6)
        fight_or_run = 0
        while fight_or_run != "f" and fight_or_run != "r":
            fight_or_run = input("\nYou have encountered a(n) %s!\n\nYour current have %dHP. 'f' to fight"
                                 ", 'r' to run away: " % (imperial.get_name(index), rebel.get_hp())).strip().lower()
            if fight_or_run == "f":
                combat_round(index)
                if rebel.get_hp() <= 0:
                    return None
            elif fight_or_run == "r":
                run_away(index)
        sud.print_game_map(sud.create_game_map(rebel))


def combat_round(index):
    """ Allow user to play one single round of combat.

    PARAM: opponent_one, a dictionary
    PARAM: opponent_two, a dictionary
    PRECONDITION: opponent_one must be a dictionary containing a complete rebel
    PRECONDITION: opponent_two must be a dictionary containing a complete rebel
    """

    print("\n" + line + "\n%s: Prepare to die, rebel scum!!\n" % imperial.get_name(index))
    while rebel.get_hp() > 0 and imperial.get_hp(index) > 0:
        attack(index)
        if imperial.get_hp(index) <= 0:
            break
        else:
            defend(index)

    if rebel.get_hp() > 0:
        print("%s's HP is %d.\n\n" % (rebel.get_name(), rebel.get_hp()) + line + "\n")
    imperial.set_hp(index, 5)


def attack(index):
    print("%s strikes!" % rebel.get_name())
    damage = randint(1, 6)

    if randint(1, 20) > imperial.get_dexterity(index):
        imperial.decrease_hp(index, damage)
        print("%s has taken a %d point hit!" % (imperial.get_name(index), damage))
        if imperial.get_hp(index) <= 0:
            print("%s has been defeated.\n" % imperial.get_name(index))
        else:
            print("Their HP has dropped to %d.\n" % imperial.get_hp(index))
    else:
        print("%s evaded the attack!\n" % imperial.get_name(index))


def defend(index):
    print("%s strikes!" % imperial.get_name(index))
    damage = randint(1, 6)

    if randint(1, 20) > rebel.get_dexterity():
        rebel.decrease_hp(damage)
        print("%s has taken a %d point hit!" % (rebel.get_name(), damage))
        if rebel.get_hp() <= 0:
            print("%s has been defeated.\n" % rebel.get_name())
        else:
            print("Their HP has dropped to %d.\n" % rebel.get_hp())
    else:
        print("%s evaded the attack!\n" % rebel.get_name())


def run_away(index):
    if randint(1, 7) == 1:
        damage = randint(1, 4)
        rebel.decrease_hp(damage)
        print("\n" + line + "\nThe %s struck you as you fled!\n\nYou have taken a %d point hit, your HP is %d."
              % (imperial.get_name(index), damage, rebel.get_hp()))
    else:
        print("\n" + line + "\nYou fled the scene unharmed!")


def main():
    encounter_imperial()


if __name__ == '__main__':
    main()
