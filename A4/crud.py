"""A Student Management System."""
from student import Student
import sys
# Krystal Wong
# A01089672


def add_student():
    pass


def file_write(student: object)-> bool:
    pass


menu_options = {1: "Add student", 2: "Delete student", 3: "Calculate class average", 4: "Print class list", 5: "Quit"}


def print_menu():
    print("What would you like to do?\n")
    for num, options in menu_options.items():
        print(str(num) + ". " + options)


def menu():
    while True:
        print_menu()
        user_input = input("Enter the corresponding number:\n")
        if user_input == 1:
            pass
        elif user_input == 2:
            pass
        elif user_input == 3:
            pass
        elif user_input == 4:
            pass
        elif user_input == 5:
            sys.exit()


def main():
    print_menu()


if __name__ == '__main__':
    main()
