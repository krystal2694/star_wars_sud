"""A Student Management System."""
from student import Student
import doctest
import sys
# Krystal Wong
# A01089672


separator = "--------------------------------------------------"


def enter_grades()-> list:
    """Allow user to enter student grades."""

    print("Enter the student's final grades.\nEnter 'done' when finished or if there are no grades to enter.")
    user_input = ""
    final_grades = []
    while user_input != "done":
        user_input = input("Enter a grade: ")
        if user_input.isdigit():
            final_grades.append(int(user_input))
    return final_grades


def in_good_standing():
    status = ""
    while status != "Y" and status != "N":
        status = (input("Is the student in good standing? (Y/N): ").upper()).strip()
        if status == "Y":
            return True
        elif status == "N":
            return False


def collect_student_info()-> list:
    """Collect student information from user."""

    print("\nPlease enter the students' information.")
    first_name = input("First Name: ").title().strip()
    last_name = input("Last Name: ").title().strip()
    student_num = input("Student Number in format A########: ").title().strip()
    status = in_good_standing()
    final_grades = enter_grades()
    student_info = [first_name, last_name, student_num, status, final_grades]
    return student_info


def add_student(student_info: list)-> None:
    """Add student to system."""

    if student_exists(student_info[2]) is False:
        try:
            new_student = Student(student_info[0], student_info[1], student_info[2], student_info[3], *student_info[4])
        except ValueError as e:
            print(e)
        else:
            if file_write(new_student):
                print("\nStudent successfully added:")
                print(str(new_student) + "\n")
            else:
                print("\nStudent could not be written to file.\n")
    else:
        print("\nThe student number you entered already exists in the system!\n")


def file_write(new_student: object)-> bool:
    """Append student at the end of student file.

    PRECONDITION: new_student must be an object of the class Student
    """
    with open('students.txt', 'a') as file_obj:
        file_obj.write(repr(new_student) + "\n")

    with open('students.txt') as file_obj:
        contents = file_obj.read()
    return True if repr(new_student) in contents else False


def student_exists(student_num: str)-> bool:
    """Verify that student exists in file."""

    with open('students.txt') as file_obj:
        contents = file_obj.read()
    if student_num in contents.split():
        return True
    else:
        return False


def file_delete_student(student_num: str)-> bool:
    """Delete student from file."""

    with open('students.txt') as file_obj:
        original_file_size = len(file_obj.read())
        file_obj.seek(0)
        new_list = [line for line in file_obj if student_num not in line]

    with open('students.txt', 'w') as file_obj:
        for student in new_list:
            file_obj.write(student)

    with open('students.txt') as file_obj:
        new_file_size = len(file_obj.read())

    return True if original_file_size > new_file_size else False


def delete_student()-> None:
    """Delete student from system."""

    student_num = input("Enter the student number: ").title()
    if student_exists(student_num):
        if file_delete_student(student_num):
            print("\nStudent successfully deleted.\n")
        else:
            print("\nThe student could not be deleted.\n")
    else:
        print("\nThe student number you entered is not on file.\n")


def file_read()-> list:
    """Return list of student objects from students.txt."""

    students_list = []
    with open('students.txt') as file_obj:
        for line in file_obj:
            tokens = line.split()
            students_list.append(Student(*tokens))
    return students_list


def calculate_class_average()-> float:
    """Calculate the class average."""

    student_averages = []
    for student in file_read():
        if student.get_student_average() > -1:
            student_averages.append(student.get_student_average())
    return sum(student_averages)/len(student_averages)


def print_class_list()-> None:
    """Print a list of all students in the system."""

    print("\n--Class List--\n")
    for student in file_read():
        print(student)
    print("\n")


def add_grade_to_student(student: Student, new_grade: int)-> None:
    try:
        student.add_final_grade(new_grade)
    except ValueError as e:
        print(e)
    else:
        print("\nGrade successfully added!\n")


def add_grade()-> None:
    """Add a grade for a specific student."""

    student_num = input("Enter the student number of the student you would like to add the grade to: ").strip()
    new_grade = input("Enter the new grade: ").strip()
    if student_exists(student_num) and new_grade.isdigit():
        student_list = file_read()
        for student in student_list:
            if student.get_student_num() == student_num:
                add_grade_to_student(student, int(new_grade))

        with open('students.txt', 'w') as file_obj:
            for each_student in student_list:
                file_obj.write(repr(each_student) + "\n")
    else:
        print("\nGrade could not be added.\n")


menu_options = {1: "Add student", 2: "Delete student", 3: "Calculate class average",
                4: "Print class list", 5: "Add grade", 6: "Quit"}


def print_menu()-> None:
    """Print system menu."""

    print(separator)
    for num, options in menu_options.items():
        print(str(num) + ". " + options)


def menu_loop()-> None:
    """Provide user with menu infinitely."""

    while True:
        print_menu()
        determine_user_choice()


def determine_user_choice()-> None:
    """Execute user's choice of option."""

    user_input = input("\nEnter the corresponding number: ")
    if user_input == "1":
        add_student(collect_student_info())
    elif user_input == "2":
        delete_student()
    elif user_input == "3":
        print("\nThe class average is %.2f.\n" % calculate_class_average())
    elif user_input == "4":
        print_class_list()
    elif user_input == "5":
        add_grade()
    elif user_input == "6":
        sys.exit()
    else:
        print("That is not a valid choice.\n")


def main():
    """Execute the program."""
    doctest.testmod()
    print(separator + "\nWelcome to the Student Database Management System")
    menu_loop()


if __name__ == '__main__':
    main()
