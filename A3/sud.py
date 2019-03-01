"""A Pokemon SUD Game."""
from random import randint
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


def create_game_map(coordinates):
    game_map = []
    for _ in range(5):
        row = []
        game_map.append(row)
        for _ in range(5):
            row.append("   ")

    pokemon_symbol = "(@)"
    game_map[coordinates[0]][coordinates[1]] = pokemon_symbol

    return game_map

def print_game_map(game_map):
    print("-" * 17)
    for i in game_map:
        print("|", end="")
        for x in i:
            print(x, end="")
        print("|")
    print("-" * 17)


def main():
    # print(pokemon_art)
    # print("Welcome to the world of Pokémon!")
    # print("------------------------------------------------")
    # name = character.choose_pokemon_name()
    # print("Hello, %s! What type of Pokémon are you?" % name)
    # pokemon_type = character.choose_pokemon_type()
    # print("Fantastic! We've been looking for a %s type Pokémon to join us!" % pokemon_type)
    coordinates = [2, 2]
    print_game_map(create_game_map(coordinates))




if __name__ == '__main__':
    main()
