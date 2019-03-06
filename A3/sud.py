"""A Star Wars SUD Game."""
import battle
import rebel
# A01089672
# Krystal Wong


line = "-------------------------------------------------------------------\n" \

introduction = """
  .       .     o88888888888888  d88b  .  8888888b.  .       .      
      .     .   Y88<88888888888 j8PY8i    888   )88      .     .
.   .   .    .   Y8b.   888    ,8P  Y8, . 88888888'    .     .   .
__________________Y88b  888 .  88888888   888  Y8b________________
::::::::::88888888888P  888   d8Y    Y8b  888   Y888888:::::::::::
::::::::::    .     .         .             .      .   :::::::::::
::::::::::Y8b  d88b  d8P  d88b   . 8888888b.  o88888888:::::::::::
___________88ij8888ij88' j8PY8i    888   )88  Y88<88888___________
 .     .   '8888PY8888' ,8P  Y8,   88888888'   Y8b.   .      .   
    .     . Y88P  Y88P  88888888 . 888  Y8b_____>88b     .      .
  .      .   Y8"  "8P  d8P    Y8b  888   Y888888888P  .     .    . \n
""" + line + "\nCloaked Figure: Wake up! Wake up!\n\n" \
               "You: ..huh? Who are you? What are you doing in my home?!\n\n" \
               "Cloaked Figure: There's no time, you must come with me.\n\n" \
               "You: I'm not going anywhere with you until you tell me who you are!\n\n" \
               "*The cloaked figure removes his hood*\n\n" \
               "Cloaked Figure: I.. am Luke Skywalker. I sense that you are strong\n" \
               "with The Force, and I need your help.\n\n" + line


instructions = "This is your map. '⛒' represents where you are on the map.\n" \
               "\n" \
               "Type: 'n' to move north.\n" \
               "      's' to move south.\n" \
               "      'e' to move east.\n" \
               "      'w' to move west.\n" \
               "      'quit' to exit game.\n\n" \
               "BEWARE, there are many disturbances in the force.."

exit_statement = "\n" + line + "\nThe Rebellion thanks you for your service.\n\n" \
                               "Return soon, the battle against the Dark Side has only just begun.\n\n" + line

commands = ["quit", "continue", "n", "s", "w", "e"]

directions = ["n", "s", "e", "w"]


def print_game_map():
    game_map = [["   " for _ in range(11)] for _ in range(11)]
    rebel_symbol = " ⛒"
    game_map[rebel.get_coordinates()[0]][rebel.get_coordinates()[1]] = rebel_symbol

    print("\n" + "✨ " * 14)
    for i in game_map:
        print("✨", end="")
        for x in i:
            print(x, end="")
        print("✨")
    print("✨ " * 14 + "\n")


def heal_rebel():
    if rebel.get_hp() < 10:
        rebel.increment_hp()
        print("You're healing! Your HP is %d." % rebel.get_hp())


def reset_game():
    rebel.set_hp(10)
    rebel.set_coordinates([5, 5])
    print_game_map()


def continue_or_exit():
    if rebel.get_hp() <= 0:
        play_again = input(line + "\nYou have been defeated by the Galactic Empire. Play again? (y/n): ")
        if play_again == "n":
            return "quit"
        elif play_again == "y":
            reset_game()
            return "continue"


def game_play():
    action = 0
    while action != "quit":
        action = input().strip().lower()
        if action not in commands:
            print("I do not understand.")
        elif action in directions:
            temp = rebel.get_coordinates()[:]
            rebel.move_character(action)

            # if character moved, they heal and have a chance of encountering an enemy
            if temp[0] != rebel.get_coordinates()[0] or temp[1] != rebel.get_coordinates()[1]:
                heal_rebel()
                battle.encounter_imperial()
                action = continue_or_exit()


def main():
    print(introduction)
    rebel.choose_name()
    rebel.choose_rebel_class(rebel.get_name())
    print(instructions)
    print_game_map()
    game_play()
    print(exit_statement)


if __name__ == '__main__':
    main()
