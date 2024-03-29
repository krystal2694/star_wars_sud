class Student:
    """A class representing a student."""

    def __init__(self, first_name: str, last_name: str, student_num: str, status: bool, *final_grades: int)-> None:
        """Create a new student.

        PRECONDITION: first_name and last_name must be composed of alphabetical characters
        PRECONDITION: first_name and last_name must not be blank
        PRECONDITION: student_num must be in the format A########
        A student can be created with no grades; if a student has no grades, the student will
        be created with a new empty list of grades. If any of the requirements is not met,
        a ValueError will be thrown and the student will not be created."""

        self.__last_name = None
        self.__status = None
        self.set_last_name(last_name)
        self.set_status(status)

        if first_name.isalpha() is False:
            raise ValueError("First name must only be made up of alphabetical characters!")
        self.__first_name = first_name.title()

        if len(student_num) != 9 or student_num[0] != "A" or student_num[1:].isdigit() is False:
            raise ValueError("The student number must be the character A, followed by 8 digits!")
        self.__student_num = student_num

        self.__final_grades = []
        for grade in final_grades:
            if int(grade) < 0 or int(grade) > 100:
                raise ValueError("A grade cannot be less than 0 or greater than 100!")
            self.__final_grades.append(int(grade))

    def __repr__(self)-> str:
        """Return a string representation of this student that looks like:
        FirstName LastName A######## True 90 80 76 100 62 42"""

        return "%s %s %s %s %s" % (self.__first_name, self.__last_name, self.__student_num,
                                   str(self.__status), " ".join((map(str, self.__final_grades))))

    def __str__(self)-> str:
        """Return a string representation of this student that looks like:
        Name: Krystal Wong, Student Number: A########, In Good Standing: True, Grades: 90 80 76 100 62 42"""

        return "Name: %s %s, Student Number: %s, In Good Standing: %s, Grades: %s"\
               % (self.__first_name, self.__last_name, self.__student_num,
                   self.__status, " ".join((map(str, self.__final_grades))))

    def set_first_name(self, last_name: str) -> None:
        """Set last name of student."""
        if last_name.isalpha():
            self.__last_name = last_name.title()
        else:
            raise ValueError("First name must only be made up of alphabetical characters!")

    def get_first_name(self)-> str:
        """Return first name of student."""
        return self.__first_name

    def get_last_name(self)-> str:
        """Return last name of student."""
        return self.__last_name

    def set_last_name(self, last_name: str)-> None:
        """Set last name of student."""
        if last_name.isalpha():
            self.__last_name = last_name.title()
        else:
            raise ValueError("Last name must only be made up of alphabetical characters!")

    def get_student_num(self)-> str:
        """Return student number of student."""
        return self.__student_num

    def get_status(self)-> list:
        """Return status of student."""
        return self.__status

    def set_status(self, status: bool)-> None:
        """Set status of student."""
        self.__status = status

    def add_final_grade(self, new_grade: int)-> None:
        """Add grade to list of student's final grades."""

        if new_grade < 0 or new_grade > 100:
            raise ValueError("\nA grade cannot be less than 0 or greater than 100!\nGrade could not be added.")
        self.__final_grades.append(new_grade)

    def add_final_grades(self, new_grades: list):
        """Add list of grades to student's list of final grades."""

        for grade in new_grades:
            self.add_final_grade(grade)

    def get_average(self) -> float:
        """Return student's average as a float."""

        # if student has no grades, return -1 to signify that student has no average
        if len(self.__final_grades) == 0:
            return -1
        else:
            return sum(self.__final_grades) / len(self.__final_grades)


def main():
    krystal = Student("Krystal", "Wong", "A01089662", True, 94, 95, 89, 99)
    print(krystal)


if __name__ == '__main__':
    main()
