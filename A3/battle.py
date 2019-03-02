"""Battle between two Pokemon."""
from random import randint
import sud


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
        print(defence_char["Name"] + " has taken a " + str(damage) + " point hit!")
        if defence_char["HP"] <= 0:
            print(defence_char["Name"] + " has perished.")
            print(offence_char["Name"] + " is the winner!")
        else:
            print("Their HP has dropped to " + str(defence_char["HP"]) + ".")
    else:
        print("They missed!")
    return defence_char


def combat_round(pokemon, wild_pokemon):
    """ Allow user to play one single round of combat.

    PARAM: opponent_one, a dictionary
    PARAM: opponent_two, a dictionary
    PRECONDITION: opponent_one must be a dictionary containing a complete pokemon
    PRECONDITION: opponent_two must be a dictionary containing a complete pokemon
    """
    while pokemon["HP"] > 0 and wild_pokemon["HP"] > 0:
        pokemon = attack(wild_pokemon, pokemon)
        if pokemon["HP"] <= 0:
            break
        else:
            wild_pokemon = attack(pokemon, wild_pokemon)

    if pokemon["HP"] > 0:
        print("%s's HP is %d." % (pokemon["Name"], pokemon["HP"]))
    wild_pokemon["HP"] = 5
    return pokemon


pokedex = [{"Name": "Snorlax", "Type": "Normal", "HP": 5, "Dexterity": 5},
           {"Name": "Jiggly Puff", "Type": "Fairy", "HP": 5, "Dexterity": 6},
           {"Name": "Rattata", "Type": "Normal", "HP": 5, "Dexterity": 4},
           {"Name": "Ghastly", "Type": "Ghost", "HP": 5, "Dexterity": 6},
           {"Name": "Charmander", "Type": "Fire", "HP": 5, "Dexterity": 9}]


def encounter_pokemon(pokemon):
    if randint(1, 10) == 1:
        wild_pokemon = pokedex[randint(0, 4)]
        fight_or_run = 0
        while fight_or_run != "f" and fight_or_run != "r":
            fight_or_run = input("A wild %s appeared! Your current have %dHP. 'f' to fight, 'r' to run: "
                                 % (wild_pokemon["Name"], pokemon["HP"])).strip().lower()
            if fight_or_run == "f":
                combat_round(pokemon, wild_pokemon)
                if pokemon["HP"] <= 0:
                    return pokemon
            elif fight_or_run == "r":
                if randint(1, 10) == 1:
                    damage = randint(1, 4)
                    pokemon["HP"] -= damage
                    print("%s struck you as you fled! %s has taken a %d point hit."
                          % (wild_pokemon["Name"], pokemon["Name"], pokemon["HP"]))
                else:
                    print("You have fled successfully!")
        sud.print_game_map(sud.create_game_map(pokemon))
    return pokemon


def main():
    pikachu = {"Name": "Pikachu", "Type": "electric", "HP": 10, "Dexterity": 2}
    jigglypuff = {"Name": "Jigglypuff", "Type": "fairy", "HP": 10, "Dexterity": 2}
    combat_round(pikachu, jigglypuff)
    # encounter_pokemon(pikachu)


if __name__ == '__main__':
    main()

