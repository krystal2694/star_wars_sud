"""A Star Wars SUD Game."""
# A01089672
# Krystal Wong
import sys
import battle
import rebel


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
               "Cloaked Figure: My name is.. Luke Skywalker. I sense that you are strong\n" \
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

directions = ["n", "s", "e", "w"]


def game_map():
    """Print game map."""
    game_board = [["   " for _ in range(11)] for _ in range(11)]
    rebel_symbol = " ⛒"
    game_board[rebel.get_row()][rebel.get_column()] = rebel_symbol

    print("\n" + "✨ " * 14)
    for row in game_board:
        print("✨", end="")
        for column in row:
            print(column, end="")
        print("✨")
    print("✨ " * 14 + "\n")


def is_valid_move(direction: str)-> bool:
    """Determine if character move in within bounds."""
    if direction == "n" and rebel.get_row() == 0:
        return False
    elif direction == "s" and rebel.get_row() == 10:
        return False
    elif direction == "e" and rebel.get_column() == 10:
        return False
    elif direction == "w" and rebel.get_column() == 0:
        return False
    return True


rebel_class_dict = {"1": ["Knowledge", "Jedi"], "2": ["Strength", "Rebel Fighter"], "3": ["Wit", "Smuggler"]}


def determine_rebel_class()-> None:
    """Determine class of character based on their most valuable trait."""

    selection = user_quit(input("\n" + line + "\nTell me, %s, what do you consider to be your most valuable trait?\n\n"
                                "1 Knowledge\n2 Strength\n3 Wit\n\nEnter the number: " % rebel.get_name()).strip())

    for number, rebel_class in rebel_class_dict.items():
        if selection == number:
            print("\n" + line + "\nAh! I think you would make a great.. %s!\n" % rebel_class[1] +
                  "\nNow, come with me %s.\n\nWe have a galaxy to save!\n\n" % rebel.get_name() + line)
            rebel.set_class(rebel_class[1])
            return None
    else:
        print("You must choose one from the list above.")
        return determine_rebel_class()


def move_character(action: str):
    """Move character north, south, east, or west."""
    if action == "n":
        rebel.set_row(rebel.get_row() - 1)
    elif action == "s":
        rebel.set_row(rebel.get_row() + 1)
    elif action == "e":
        rebel.set_column(rebel.get_column() + 1)
    elif action == "w":
        rebel.set_column(rebel.get_column() - 1)


def heal_character():
    """Heal character if they are not already at full health."""
    if rebel.get_hp() < 10:
        rebel.set_hp(rebel.get_hp() + 1)
        print("You're healing! Your HP is %d." % rebel.get_hp())


def game_play():
    """Game play, where the magic happens."""
    while True:
        action = user_quit(input().strip().lower())
        if action in directions:
            if is_valid_move(action) is True:
                move_character(action)
                heal_character()
                battle.encounter_enemy(battle.determine_enemy())
                restart_or_exit()
            else:
                print("Do not leave the galaxy %s, you cannot leave us in the hands of the Galactic Empire!"
                      % rebel.get_name())
        else:
            print("I do not understand.")


def restart_or_exit():
    """Restart or exit game if player is defeated."""
    if rebel.get_hp() <= 0:
        play_again = ""
        while play_again != "n" and play_again != "y":
            play_again = input(line + "\nYou have been defeated by the Galactic Empire. Play again? (y/n): ")
            if play_again == "n":
                user_quit("quit")
            elif play_again == "y":
                reset_game()
    game_map()


def reset_game():
    """Reset character HP and position."""
    rebel.set_hp(10)
    rebel.set_row(5)
    rebel.set_column(5)


def user_quit(message)-> str:
    """Exit and save game when user enters 'quit'."""
    if message == "quit":
        print(exit_statement)
        # rebel.save_character()
        sys.exit()
    else:
        return message


def main():
    """Execute the program."""
    print(introduction)
    rebel.set_name()
    determine_rebel_class()
    print(instructions)
    game_map()
    game_play()


if __name__ == '__main__':
    main()
