"""A Student Management System."""
from student import Student
import sys
# Krystal Wong
# A01089672


separator = "--------------------------------------------------\n"


def enter_grades()-> list:
    print("Enter the student's final grades.\nEnter 'done' when finished or if there are no grades to enter.")
    user_input = ""
    final_grades = []
    while user_input != "done":
        user_input = input("Enter a grade: ")
        final_grades.append(user_input)
    return final_grades[:-1]


def collect_student_info()-> list:
    print("\nPlease enter the student's information.")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    student_num = input("Student Number - format(A12345678): ").title()
    status = bool(input("Student Status - True for in good standing, False for not in good standing: ").title())
    final_grades = enter_grades()
    student_info = [first_name, last_name, student_num, status, final_grades]
    return student_info


def add_student(student_info: list)-> None:
    try:
        new_student = Student(student_info[0], student_info[1], student_info[2], student_info[3], student_info[4])
    except ValueError:
        print("Could not add student, please try again.")
    else:
        if file_write(new_student):
            print("\nStudent successfully added.")
        else:
            print("Student could not be written to file.")


def file_write(new_student: Student)-> bool:
    with open('students.txt', 'a') as file_obj:
        start = file_obj.tell()
        file_obj.write(new_student.get_info() + "\n")
        end = file_obj.tell()
    return True if start != end else False


def verify_student_exists(student_num: str)-> bool:
    with open('students.txt') as file_obj:
        contents = file_obj.read()
    if student_num in contents.split():
        return True
    else:
        return False


def file_delete_student(student_num: str)-> bool:
    with open('students.txt') as file_obj:
        new_list = [line for line in file_obj if student_num not in line]
        original_file_size = len(file_obj.read())

    with open('students.txt', 'w') as file_obj:
        for student in new_list:
            file_obj.write(student)

    with open('students.txt') as file_obj:
        new_file_size = len(file_obj.read())

    return True if original_file_size != new_file_size else False


def delete_student():
    student_num = input("Enter the student number: ").title()
    if verify_student_exists(student_num):
        if file_delete_student(student_num):
            print("\nStudent successfully deleted.")
        else:
            print("\nThe student could not be deleted.")
    else:
        print("\nThe student does not exist.")


def calculate_class_average():
    class_average = []
    for student in file_read():
        grades = list(map(int, student[4:]))
        class_average.append(sum(grades)/len(grades))
    return sum(class_average)/len(class_average)


def file_read()-> list:
    with open('students.txt') as file_obj:
        lines = file_obj.readlines()
    students_list = []
    for line in lines:
        students_list.append(line.split())
    return students_list


def print_class_list():
    print("Class List\n")
    for student in file_read():
        print("Name: %s %s, Student Number: %s, Status: %s, Grades: "
              % (student[0], student[1], student[2], student[3]), end="")
        for grade in student[4:-1]:
            print("%s " % grade, end="")
        print(str(student[-1]) + "\n")


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
            add_student(collect_student_info())
        elif user_input == "2":
            delete_student()
        elif user_input == "3":
            print("\nThe class average is %.2f." % calculate_class_average())
        elif user_input == "4":
            pass
        elif user_input == "5":
            sys.exit()
        else:
            print("That is not a valid choice.")


def main():
    print(separator + "Welcome to the Student Database Management System\n" + separator)
    # menu()
    # print(file_read())
    print_class_list()


if __name__ == '__main__':
    main()
