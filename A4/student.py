class Student:
    """A class representing a student."""

    def __init__(self, first_name: str, last_name: str, student_num: str, status: str, *final_grades: str)-> None:
        """Initialize student attributes."""
        self.last_name = None
        self.status = None
        self.set_last_name(last_name)
        self.set_status(status)

        if first_name.isalpha() is False:
            raise ValueError("First name must only be made up of alphabetical characters!")
        self.first_name = first_name.title()

        if len(student_num) != 9 or student_num[0] != "A" or student_num[1:].isdigit() is False:
            raise ValueError("The student number must be the character A, followed by 8 digits!")
        self.__student_num = student_num

        self.final_grades = []
        for grade in final_grades:
            if int(grade) < 0 or int(grade) > 100:
                raise ValueError("A grade cannot be less than 0 or greater than 100!")
            self.final_grades.append(grade)

    def __str__(self)-> str:
        return self.first_name + " " + self.last_name + " " + self.__student_num + " " + self.status \
               + " " + " ".join(self.final_grades)

    def get_first_name(self)-> str:
        """Return first name of student."""
        return self.first_name

    def get_last_name(self)-> str:
        """Return last name of student."""
        return self.last_name

    def set_last_name(self, last_name: str)-> None:
        """Set last name of student."""
        if last_name.isalpha():
            self.last_name = last_name.title()
        else:
            raise ValueError("Last name must only be made up of alphabetical characters!")

    def get_student_num(self)-> str:
        """Return student number of student."""
        return self.__student_num

    def get_final_grades(self)-> list:
        """Return list of student's final grades."""
        return self.final_grades

    def get_status(self)-> list:
        """Return status of student."""
        return self.status

    def set_status(self, status: str)-> None:
        """Set status of student."""
        if status != "True" and status != "False":
            raise ValueError("Status can only be 'True' or 'False'.")
        self.status = status

    def add_final_grade(self, new_grade: str)-> None:
        """Add grade to list of student's final grades."""
        if int(new_grade) < 0 or int(new_grade) > 100:
            raise ValueError("A grade cannot be less than 0 or greater than 100!")
        self.final_grades.append(new_grade)


def main():
    krystal = Student("Krystal", "Wong", "A01089662", "True", "94", "95", "89", "99")
    print(krystal)
    # krystal.add_final_grade("100")
    # print(krystal.get_info())


if __name__ == '__main__':
    main()
