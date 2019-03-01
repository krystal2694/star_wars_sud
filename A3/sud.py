"""A Pokemon SUD Game."""
from random import randint
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
    for _ in range(5):
        row = []
        game_map.append(row)
        for _ in range(5):
            row.append("   ")

    pokemon_symbol = "(@)"
    game_map[pokemon["Coordinates"][0]][pokemon["Coordinates"][1]] = pokemon_symbol

    return game_map


def print_game_map(game_map):
    print("-" * 17)
    for i in game_map:
        print("|", end="")
        for x in i:
            print(x, end="")
        print("|")
    print("-" * 17)


def instructions():
    print("This is your map. '(@)' represents where you are on the map.\n"
          "Type 'n' to move north.\n"
          "Type 's' to move south.\n"
          "Type 'e' to move east.\n"
          "Type 'w' to move west.")


def move_character(pokemon):
    directions = ["n", "s", "e", "w"]
    decision = input().strip().lower()
    if decision not in directions:
        print("I do not understand.")
        return pokemon

    if decision == "n" and pokemon["Coordinates"][0] != 0:
            pokemon["Coordinates"][0] -= 1
    elif decision == "s" and pokemon["Coordinates"][0] != 4:
            pokemon["Coordinates"][0] += 1
    elif decision == "e" and pokemon["Coordinates"][1] != 4:
            pokemon["Coordinates"][1] += 1
    elif decision == "w" and pokemon["Coordinates"][1] != 0:
            pokemon["Coordinates"][1] -= 1
    else:
        print("you've reached the edge of the forest, you cannot go this way.")
        return move_character(pokemon)

    print_game_map(create_game_map(pokemon))
    return pokemon




def main():
    # print(pokemon_art)
    # print("Welcome to the world of Pokémon!")
    # print("------------------------------------------------")
    # name = character.choose_pokemon_name()
    # print("Hello, %s! What type of Pokémon are you?" % name)
    # pokemon_type = character.choose_pokemon_type()
    # print("Fantastic! We've been looking for a %s type Pokémon to join us!" % pokemon_type)
    instructions()
    pikachu = {"Name": "Pikachu", "Type": "electric", "HP": 10, "Dexterity": 10, "Coordinates": [2, 2]}
    print_game_map(create_game_map(pikachu))


if __name__ == '__main__':
    main()
