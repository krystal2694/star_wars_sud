"""Create a Pokemon Character."""
from random import randint
# A01089672
# Krystal Wong


def choose_pokemon_name():
    name = input("What is your name? ")
    return name.title()


pokemon_types_dict = {1: "Normal", 2: "Fire", 3: "Electric", 4: "Fairy", 5: "Psychic", 6: "Ice",
                      7: "Grass", 8: "Poison", 9: "Ghost", 10: "Water", 11: "Bug", 12: "Dark"}


def choose_pokemon_type():
    """Return user's selection of their desired Pokémon type."""

    print("What type of Pokemon are you?")
    # provide user with information needed to make their choice
    print("------------------------------------------------")
    for key, value in pokemon_types_dict.items():
        print(key, value)

    selection = int(input("Enter the corresponding number: ").strip())
    print("------------------------------------------------")
    for number, char_class in pokemon_types_dict.items():
        if selection == number:
            return char_class
    else:
        print("You must choose a Pokémon type from the list above.")
        return choose_pokemon_type()


def create_pokemon(name, pokemon_type):
    """Create a Pokemon.

    PARAM: name, a string
    PARAM: pokemon type, a string
    PRECONDITION: name must be a string
    PRECONDITION: pokemon type must be a string
    POSTCONDITION: create a Pokemon complete with name, Type, HP, Dexterity
    RETURN: a dictionary consisting of all information required for a new Pokemon
    """

    pokemon = {"Name": name,
               "Type": pokemon_type,
               "HP": 10,
               "Dexterity": randint(1, 10),
               "Coordinates": [5, 5]}

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
