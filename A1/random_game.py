"""This program allows the user to play one round of rock, paper scissors with the computer."""

# Krystal Wong
# A01089672
# 02/02/2019
import random
import colour_mixer


def rock_paper_scissors():
    """Generate a random number in the range [0,2] to play a game of rock, paper, scissors with the user."""

    user_choice = colour_mixer.clean_input(input("Choose rock, paper, or scissors: "))
    if user_choice == "Rock":
        user_choice = 0
    elif user_choice == "Paper":
        user_choice = 1
    elif user_choice == "Scissors":
        user_choice = 2
    else:
        print("You did not enter rock, paper, or scissors. Try again!")

    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        print("Computer's choice: Rock")
    elif computer_choice == 1:
        print("Computer's choice: Paper")
    elif computer_choice == 2:
        print("Computer's choice: Scissors")

    # determine game outcome
    if computer_choice == user_choice:
        print("It's a tie!")
    elif computer_choice == 0 and user_choice == 1:
        print("Paper beats rock - you win!")
    elif computer_choice == 0 and user_choice == 2:
        print("Rock beats scissors - you lose :(")
    elif computer_choice == 1 and user_choice == 0:
        print("Paper beats rock - you lose :(")
    elif computer_choice == 1 and user_choice == 2:
        print("Scissors beat paper - you win!")
    elif computer_choice == 2 and user_choice == 0:
        print("Rock beats scissors - you win!")
    elif computer_choice == 2 and user_choice == 1:
        print("Scissors beats paper - you lose :(")


def main():
    rock_paper_scissors()


if __name__ == '__main__':
    main()
