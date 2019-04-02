class Student:
    """A class representing a student."""

    def __init__(self, first_name: str, last_name: str, student_num: str, status: bool, *final_grades: int)-> None:
        """Initialize student attributes."""
        self.__last_name = None
        self.__status = None
        self.set_last_name(last_name)
        self.set_status(status)

        if first_name.isalpha() is False:
            raise ValueError("First name must only be made up of alphabetical characters!\nStudent could not be added.")
        self.__first_name = first_name.title()

        if len(student_num) != 9 or student_num[0] != "A" or student_num[1:].isdigit() is False:
            raise ValueError("The student number must be the character A, followed by 8 digits!"
                             "\nStudent could not be added.")
        self.__student_num = student_num

        self.__final_grades = []
        for grade in final_grades:
            if int(grade) < 0 or int(grade) > 100:
                raise ValueError("A grade cannot be less than 0 or greater than 100!\n Student could not be added.")
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
            raise ValueError("Last name must only be made up of alphabetical characters!\n Student could not be added.")

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
            raise ValueError("A grade cannot be less than 0 or greater than 100!\nGrade could not be added.")
        self.__final_grades.append(new_grade)



def main():
    krystal = Student("Krystal", "Wong", "A01089662", True, 94, 95, 89, 99)
    print(repr(krystal))


if __name__ == '__main__':
    main()
