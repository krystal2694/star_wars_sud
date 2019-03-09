"""Battle between two Star Wars characters."""
from random import randint
import imperial
import rebel


line = "-------------------------------------------------------------------\n"


def encounter_imperial():
    """Encounter member of imperial force."""
    if randint(1, 5) == 1:
        # choose member of imperial force by random
        index = randint(0, 6)
        fight_or_run = 0
        while fight_or_run != "f" and fight_or_run != "r":
            fight_or_run = input("\nYou have encountered a(n) %s!\n\nYour current have %dHP. 'f' to fight"
                                 ", 'r' to run away: " % (imperial.get_name(index), rebel.get_hp())).strip().lower()
            if fight_or_run == "f":
                combat_round(index)
            elif fight_or_run == "r":
                run_away(index)


def combat_round(index: int):
    """ Round of combat to the death."""
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


def attack(index: int):
    """Attack the enemy."""
    print("You strike!")
    damage = randint(1, 6)

    if randint(1, 20) > imperial.get_dexterity(index):
        imperial.decrease_hp(index, damage)
        print("The %s has taken a %d point hit!" % (imperial.get_name(index), damage))
        if imperial.get_hp(index) <= 0:
            print("\nYou have defeated the %s.\n"
                  "We are one step closer to peace in the galaxy!\n" % imperial.get_name(index))
        else:
            print("Their HP has dropped to %d.\n" % imperial.get_hp(index))
    else:
        print("The %s evaded the attack!\n" % imperial.get_name(index))


def defend(index: int):
    """Character on defence against enemy attack."""
    print("The %s strikes!" % imperial.get_name(index))
    damage = randint(1, 6)

    if randint(1, 15) > rebel.get_dexterity():
        rebel.set_hp(rebel.get_hp() - damage)
        print("You have taken a %d point hit!" % damage)
        if rebel.get_hp() <= 0:
            print("You have been defeated.\n\n%s: Never underestimate the power of the Dark Side."
                  % imperial.get_name(index))
        else:
            print("Your HP has dropped to %d.\n" % rebel.get_hp())
    else:
        print("You evaded the attack!\n")


def run_away(index: int):
    """Run away from enemy."""
    if randint(1, 5) == 1:
        damage = randint(1, 4)
        rebel.set_hp(rebel.get_hp() - damage)
        print("\n" + line + "\nThe %s struck you as you fled!\n\nYou have taken a %d point hit, your HP is %d."
              % (imperial.get_name(index), damage, rebel.get_hp()))
    else:
        print("\n" + line + "\nYou fled the scene unharmed!")


def main():
    encounter_imperial()


if __name__ == '__main__':
    main()
