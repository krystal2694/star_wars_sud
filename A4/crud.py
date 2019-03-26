"""A Student Management System."""
from student import Student
import sys
# Krystal Wong
# A01089672


def enter_grades()-> list:
    print("Enter the student's final grades. Enter 'done' when finished.")
    user_input = ""
    final_grades = []
    while user_input != "done":
        user_input = input("Enter a grade: ")
        final_grades.append(user_input)
    return final_grades[:-1]


def add_student():
    print("\nPlease enter the student's information.")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    student_num = input("Student Number - format(A12345678): ")
    status = bool(input("Student Status - True for in good standing, False for not in good standing: ").title())
    final_grades = enter_grades()
    try:
        new_student = Student(first_name, last_name, student_num, status, final_grades)
    except ValueError:
        print("Could not add student, please try again.")
    else:
        if file_write(new_student):
            print("Student successfully added.")
        else:
            print("Student could not be written to file.")


def file_write(new_student)-> bool:
    with open('students.txt', 'a') as file_obj:
        start = file_obj.tell()
        file_obj.write(new_student.get_info() + "\n")
        end = file_obj.tell()
    return True if start != end else False


menu_options = {1: "Add student", 2: "Delete student", 3: "Calculate class average", 4: "Print class list", 5: "Quit"}


def print_menu():
    print("\nWhat would you like to do?\n")
    for num, options in menu_options.items():
        print(str(num) + ". " + options)


def menu():
    while True:
        print_menu()
        user_input = input("\nEnter the corresponding number: ")
        if user_input == "1":
            add_student()
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        elif user_input == "5":
            sys.exit()
        else:
            print("That is not a valid choice.")


def main():
    print("Welcome to the Student Database Management System")
    menu()


if __name__ == '__main__':
    main()
