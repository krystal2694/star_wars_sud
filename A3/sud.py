"""A Pokemon SUD Game."""
import battle
import character
# A01089672
# Krystal Wong


pokemon_art = """/
                                .::.                          
                              .;:**'                       
                              `                              
  .:XHHHHk.              db.   .;;.     dH  MX               
oMMMMMMMMMMM       ~MM  dMMP :MMMMMR   MMM  MR      ~MRMN     
QMMMMMb  "MMX       MMMMMMP !MX' :M~   MMM MMM  .oo. XMMM 'MMM
  `MMMM.  )M> :X!Hk. MMMM   XMM.o"  .  MMMMMMM X?XMMM MMM>!MMP
   'MMMb.dM! XM M'?M MMMMMX.`MMMMMMMM~ MM MMM XM `" MX MMXXMM 
    ~MMMMM~ XMM. .XM XM`"MMMb.~*?**~ .MMX M t MMbooMM XMMMMMP 
     ?MMM>  YMMMMMM! MM   `?MMRb.    `""'   !L"MMMMM XM IMMM
      MMMX   "MMMM"  MM       ~%:           !Mh.""' dMI IMMP  
      'MMM.                                             IMX
       ~M!M                                             IMP   

    """


def create_game_map(pokemon):
    game_map = []
    for _ in range(11):
        row = []
        game_map.append(row)
        for _ in range(11):
            row.append("   ")

    pokemon_symbol = " ⛒"
    game_map[pokemon["Coordinates"][0]][pokemon["Coordinates"][1]] = pokemon_symbol

    return game_map


def print_game_map(game_map):
    print("\n" + "🌲" * 22)
    for i in game_map:
        print("🌲", end="")
        for x in i:
            print(x, end="")
        print(" 🌲")
    print("🌲" * 22 + "\n")


def instructions():
    print("This is your map. '(@)' represents where you are on the map.\n"
          "Type 'n' to move north.\n"
          "Type 's' to move south.\n"
          "Type 'e' to move east.\n"
          "Type 'w' to move west.\n"
          "BEWARE: The forrest is full of wild Pokemon..\n")


def heal_pokemon(pokemon):
    if pokemon["HP"] < 10:
        pokemon["HP"] += 1
        print("You're healing! Your HP is %d." % pokemon["HP"])
    return pokemon


def move_character(pokemon, direction):
    if direction == "n" and pokemon["Coordinates"][0] != 0:
            pokemon["Coordinates"][0] -= 1
    elif direction == "s" and pokemon["Coordinates"][0] != 10:
            pokemon["Coordinates"][0] += 1
    elif direction == "e" and pokemon["Coordinates"][1] != 10:
            pokemon["Coordinates"][1] += 1
    elif direction == "w" and pokemon["Coordinates"][1] != 0:
            pokemon["Coordinates"][1] -= 1
    else:
        print("you've reached the edge of the forest, you cannot go this way.")
        return pokemon

    print_game_map(create_game_map(pokemon))
    return pokemon


def main():
    print(pokemon_art)
    print("Welcome to the world of Pokémon!")
    print("------------------------------------------------")
    name = character.choose_pokemon_name()
    print("Hello, %s! What type of Pokémon are you?" % name)
    pokemon_type = character.choose_pokemon_type()
    print("Fantastic! We've been looking for a %s type Pokémon to join us!" % pokemon_type)
    print("------------------------------------------------")
    pokemon = character.create_pokemon(name, pokemon_type)
    instructions()
    print_game_map(create_game_map(pokemon))
    commands = ["quit", "n", "s", "w", "e"]
    directions = ["n", "s", "e", "w"]
    action = 0
    while action != "quit":
        action = input().strip().lower()
        if action not in commands:
            print("I do not understand.")
        if action in directions:
            temp = pokemon["Coordinates"][:]
            pokemon = move_character(pokemon, action)
            if temp[0] != pokemon["Coordinates"][0] or temp[1] != pokemon["Coordinates"][1]:
                pokemon = heal_pokemon(pokemon)
                pokemon = battle.encounter_pokemon(pokemon)
                if pokemon["HP"] <= 0:
                    print("------------------------------------------------")
                    play_again = input("GAME OVER. Play again? (y/n): ")
                    if play_again == "n":
                        action = "quit"
                    elif play_again == "y":
                        pokemon["HP"] = 10
                        pokemon["Coordinates"] = [5, 5]
                        print_game_map(create_game_map(pokemon))
    print("------------------------------------------------")
    print("Thanks for playing, see you next time!")


if __name__ == '__main__':
    main()
