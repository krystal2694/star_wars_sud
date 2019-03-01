"""Create a Pokemon Character."""
# A01089672
# Krystal Wong


def choose_character_name():
    name = input("What is your name? ")
    return name.title()


def choose_class():
    """Return user's selection of their desired Pokémon type."""

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
        return choose_class()
