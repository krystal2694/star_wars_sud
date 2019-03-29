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
            final_grades.append(user_input)
    return final_grades


def collect_student_info()-> list:
    """Collect student information from user."""
    print("\nPlease enter the students' information.")
    first_name = input("First Name: ").title().strip()
    last_name = input("Last Name: ").title().strip()
    student_num = input("Student Number - format(A12345678): ").title().strip()
    status = (input("In Good Standing (True/False): ").title()).strip()
    final_grades = enter_grades()
    student_info = [first_name, last_name, student_num, status, final_grades]
    return student_info


def add_student(student_info: list)-> None:
    """Add student to system."""
    try:
        new_student = Student(student_info[0], student_info[1], student_info[2], student_info[3], *student_info[4])
    except ValueError as e:
        print(e)
        print("Student could not be added.")
    else:
        if file_write(new_student):
            print("\nStudent successfully added:")
            print(str(new_student) + "\n")
        else:
            print("Student could not be written to file.")


def file_write(new_student: object)-> bool:
    """Append student at the end of student file.

    PRECONDITION: new_student must be an object of the class Student
    >>> new_student = Student("Krystal", "Wong", "A01089672", "True", "95")
    >>> file_write(new_student)
    True
    """
    with open('students.txt', 'a') as file_obj:
        start = file_obj.tell()
        file_obj.write(str(new_student) + "\n")
        end = file_obj.tell()
    return True if start != end else False


def student_exists(student_num: str)-> bool:
    """Verify that student exists in file."""
    with open('students.txt') as file_obj:
        contents = file_obj.read()
    if student_num in contents.split():
        return True
    else:
        print("\nThe student does not exist.\n")
        return False


def file_delete_student(student_num: str)-> bool:
    """Delete student from file."""
    with open('students.txt') as file_obj:
        new_list = [line for line in file_obj if student_num not in line]
        original_file_size = len(file_obj.read())

    with open('students.txt', 'w') as file_obj:
        for student in new_list:
            file_obj.write(student)

    with open('students.txt') as file_obj:
        new_file_size = len(file_obj.read())

    return True if original_file_size != new_file_size else False


def delete_student()-> None:
    """Delete student from system."""
    student_num = input("Enter the student number: ").title()
    if student_exists(student_num):
        if file_delete_student(student_num):
            print("\nStudent successfully deleted.")
        else:
            print("\nThe student could not be deleted.")


def file_read()-> list:
    """Return list of student objects from students text file."""
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
        if len(student.get_final_grades()) > 0:
            grades = list(map(int, student.get_final_grades()))
            student_averages.append(sum(grades)/len(grades))
    return sum(student_averages)/len(student_averages)


def print_class_list()-> None:
    """Print a list of all students in the system."""
    print("\n--Class List--\n")
    for student in file_read():
        print("Name: %s %s, Student Number: %s, In Good Standing: %s, Grades:%s"
              % (student.get_first_name(), student.get_last_name(), student.get_student_num(),
                 student.get_status(), " ".join(student.get_final_grades())))
    print("\n")


def add_grade()-> None:
    """Add a grade for a specific student."""
    student_num = input("Enter the student number of the student you would like to add the grade to: ").strip()
    if student_exists(student_num):
        new_grade = input("Enter the new grade: ").strip()
        student_list = file_read()
        for student in student_list:
            if student.get_student_num() == student_num:
                student.add_final_grade(new_grade)

        with open('students.txt', 'w') as file_obj:
            for each_student in student_list:
                file_obj.write(str(each_student) + "\n")
        print("Grade successfully added!")


menu_options = {1: "Add student", 2: "Delete student", 3: "Calculate class average",
                4: "Print class list", 5: "Add grade", 6: "Quit"}


def print_menu()-> None:
    """Print system menu."""
    print(separator)
    for num, options in menu_options.items():
        print(str(num) + ". " + options)


def menu()-> None:
    """Execute user's choice of option."""
    while True:
        print_menu()
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
            print("That is not a valid choice.")


def main():
    """Execute the program."""
    print(separator + "\nWelcome to the Student Database Management System")
    menu()
    doctest.testmod()


if __name__ == '__main__':
    main()
