"""Battle between two Star Wars characters."""
# A01089672
# Krystal Wong
# 28/02/2019
from random import randint
import imperial
import rebel


line = "-------------------------------------------------------------------\n"


def determine_enemy()-> int:
    """Determine which enemy the character may encounter."""
    index = randint(0, len(imperial.imperial_forces) - 1)
    return index


def encounter_enemy(index: int)-> None:
    """Encounter member of imperial force.

    PRECONDITION: index must be an int representing an existing index in imperial_forces
    POSTCONDITION: Encounters member of imperial force corresponding to index"""

    fight_or_run = ""
    while fight_or_run != "f" and fight_or_run != "r":
        fight_or_run = input("\nYou have encountered a(n) %s!\n\nYour current have %dHP. 'f' to fight"
                             ", 'r' to run away: " % (imperial.get_name(index), rebel.get_hp())).strip().lower()
        if fight_or_run == "f":
            combat_round(index)
        elif fight_or_run == "r":
            run_away(index)


def combat_round(index: int)-> None:
    """Round of combat to the death.

    PRECONDITION: index must be an int representing an existing index in imperial_forces
    POSTCONDITION: Fight member of imperial force corresponding to index"""

    print("\n" + line + "\n%s: Prepare to die, rebel scum!!\n" % imperial.get_name(index))
    while rebel.get_hp() > 0 and imperial.get_hp(index) > 0:
        attack(index)
        if imperial.get_hp(index) <= 0:
            break
        else:
            defend(index)

    if rebel.get_hp() > 0:
        print("Your HP is %d.\n\n" % rebel.get_hp() + line)

    # reset imperial force's HP to 5 for next encounter
    imperial.set_hp(index, 5)


def attack(index: int)-> None:
    """Attack the enemy.

    PRECONDITION: index must be an int representing an existing index in imperial_forces
    POSTCONDITION: Attack member of imperial force corresponding to index"""

    print("You strike!")
    # determine if hit was effective
    if randint(1, 15) > imperial.get_dexterity(index):
        damage = randint(1, 6)
        imperial.set_hp(index, imperial.get_hp(index) - damage)
        print("The %s has taken a %d point hit!" % (imperial.get_name(index), damage))
        if imperial.get_hp(index) <= 0:
            print("\nYou have defeated the %s.\n"
                  "We are one step closer to peace in the galaxy!\n" % imperial.get_name(index))
        else:
            print("Their HP has dropped to %d.\n" % imperial.get_hp(index))
    else:
        print("The %s evaded the attack!\n" % imperial.get_name(index))


def defend(index: int)-> None:
    """Character on defence against enemy attack.

    PRECONDITION: index must be an int representing an existing index in imperial_forces
    POSTCONDITION: Defend against member of imperial force corresponding to index"""

    print("The %s strikes!" % imperial.get_name(index))
    # determine if hit was effective
    if randint(1, 15) > rebel.get_dexterity():
        damage = randint(1, 6)
        rebel.set_hp(rebel.get_hp() - damage)
        print("You have taken a %d point hit!" % damage)
        if rebel.get_hp() <= 0:
            print("You have been defeated.\n\n%s: Never underestimate the power of the Dark Side.\n"
                  % imperial.get_name(index))
        else:
            print("Your HP has dropped to %d.\n" % rebel.get_hp())
    else:
        print("You evaded the attack!\n")


def run_away(index: int)-> None:
    """Run away from enemy.

    PRECONDITION: index must be an int representing an existing index in imperial_forces
    POSTCONDITION: Run away from member of imperial force corresponding to index"""

    if randint(1, 5) == 1:
        damage = randint(1, 4)
        rebel.set_hp(rebel.get_hp() - damage)
        print("\n" + line + "\nThe %s struck you as you fled!\n\nYou have taken a %d point hit, your HP is %d."
              % (imperial.get_name(index), damage, rebel.get_hp()))
    else:
        print("\n" + line + "\nYou fled the scene unharmed!")


def main():
    print(run_away(2))


if __name__ == '__main__':
    main()
