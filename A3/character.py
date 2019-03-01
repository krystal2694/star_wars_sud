"""Create a Pokemon Character."""
from random import randint
# A01089672
# Krystal Wong


def choose_pokemon_name():
    name = input("What is your name? ")
    return name.title()


def choose_pokemon_type():
    """Return user's selection of their desired Pokémon type."""

    print("What type of Pokemon are you?")
    # provide user with information needed to make their choice
    classes = {1: "water", 2: "fire", 3: "electric", 4: "fairy", 5: "psychic", 6: "ice",
               7: "grass", 8: "poison", 9: "ghost", 10: "steel", 11: "bug", 12: "dark"}
    print("------------------------------------------------")

    for key, value in classes.items():
        print(key, value)

    selection = int(input("Enter the corresponding number: ").strip())
    print("------------------------------------------------")
    for number, char_class in classes.items():
        if selection == number:
            return char_class
    else:
        print("You must choose a Pokémon type from the list above.")
        return choose_pokemon_type()


def create_pokemon(name):
    """Create a Pokemon.

    PARAM: name, a string
    PRECONDITION: name must be a string
    POSTCONDITION: create a Pokemon complete with name, Type, HP, Dexterity
    RETURN: a dictionary consisting of all information required for a new Pokemon
    """

    pokemon_type = choose_pokemon_type()

    pokemon = {"Name": name,
               "Type": pokemon_type,
               "HP": 10,
               "Dexterity": randint(1, 5)}

    return pokemon


def print_pokemon(pokemon):
    """Print the parameter.

    PARAM: character, a dictionary
    PRECONDITION: character must be a dictionary
    POSTCONDITION: print contents of parameter in a nice format
    RETURN: a nicely formatted string
    """

    for key, value in pokemon.items():
        print(key + ": " + str(value))

