"""A Star Wars SUD Game."""
import battle
import character
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
               "\n" \
               "BEWARE, there are many disturbances in the force.."

commands = ["quit", "n", "s", "w", "e"]

directions = ["n", "s", "e", "w"]


def create_game_map(rebel):
    game_map = []
    for _ in range(11):
        row = []
        game_map.append(row)
        for _ in range(11):
            row.append("   ")

    rebel_symbol = " ⛒"
    game_map[rebel["Coordinates"][0]][rebel["Coordinates"][1]] = rebel_symbol

    return game_map


def print_game_map(game_map):
    print("\n" + "✨ " * 14)
    for i in game_map:
        print("✨", end="")
        for x in i:
            print(x, end="")
        print("✨")
    print("✨ " * 14 + "\n")


def heal_rebel(rebel):
    if rebel["HP"] < 10:
        rebel["HP"] += 1
        print("You're healing! Your HP is %d." % rebel["HP"])
    return rebel


def move_character(rebel, direction):
    if direction == "n" and rebel["Coordinates"][0] != 0:
            rebel["Coordinates"][0] -= 1
    elif direction == "s" and rebel["Coordinates"][0] != 10:
            rebel["Coordinates"][0] += 1
    elif direction == "e" and rebel["Coordinates"][1] != 10:
            rebel["Coordinates"][1] += 1
    elif direction == "w" and rebel["Coordinates"][1] != 0:
            rebel["Coordinates"][1] -= 1
    else:
        print("Don't leave the galaxy %s, you cannot leave us in the hands of the Galactic Empire!" % rebel["Name"])
        return rebel

    print_game_map(create_game_map(rebel))
    return rebel


def reset_game(rebel):
    rebel["HP"] = 10
    rebel["Coordinates"] = [5, 5]
    print_game_map(create_game_map(rebel))
    return rebel


def main():
    print(introduction)
    name = character.choose_name()
    rebel_class = character.choose_rebel_class(name)
    rebel = character.create_rebel(name, rebel_class)
    print(instructions)
    print_game_map(create_game_map(rebel))
    action = 0
    while action != "quit":
        action = input().strip().lower()
        if action not in commands:
            print("I do not understand.")
        elif action in directions:
            temp = rebel["Coordinates"][:]
            rebel = move_character(rebel, action)
            if temp[0] != rebel["Coordinates"][0] or temp[1] != rebel["Coordinates"][1]:
                rebel = heal_rebel(rebel)
                rebel = battle.encounter_imperial(rebel)
                if rebel["HP"] <= 0:
                    print(line)
                    play_again = input("You have been defeated by the Galactic Empire. Play again? (y/n): ")
                    if play_again == "n":
                        action = "quit"
                    elif play_again == "y":
                        rebel = reset_game(rebel)
    print("\n" + line + "\nThe Rebellion thanks you for your service.\n"
                        "\nReturn soon, the battle against the Dark Side has only just begun.\n\n" + line)


if __name__ == '__main__':
    main()
