class Student:
    """A class representing a student."""

    def __init__(self, first_name: str, last_name: str, student_num: str, status: str, *final_grades: str):
        self.first_name = None
        self.last_name = None
        self.status = None

        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_status(status)

        if len(student_num) != 9 or student_num[0] != "A" or student_num[1:].isdigit() is False:
            raise ValueError("The student number must be the character A, followed by 8 digits!")
        self.__student_num = student_num

        self.final_grades = []
        for grade in final_grades:
            if int(grade) < 0 or int(grade) > 100:
                print("A grade cannot be less than 0 or greater than 100!")
                raise ValueError
            self.final_grades.append(grade)

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        if len(first_name.strip()) == 0 or first_name.isalpha() is False:
            raise ValueError("First name must only be made up of alphabetical characters!")
        self.first_name = first_name.title()

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        if last_name.isalpha():
            self.last_name = last_name.title()
        else:
            raise ValueError("Last name must only be made up of alphabetical characters!")

    def get_student_num(self):
        return self.__student_num

    def get_final_grades(self):
        return self.final_grades

    def get_status(self):
        return self.status

    def set_status(self, status):
        if status != "True" and status != "False":
            raise ValueError("Status can only be 'True' or 'False'.")
        self.status = status

    def get_info(self):
        return self.first_name + " " + self.last_name + " " + self.__student_num + " " + self.status \
               + " " + " ".join(self.final_grades)

    def add_final_grade(self, new_grade):
        if int(new_grade) < 0 or int(new_grade) > 100:
            raise ValueError("A grade cannot be less than 0 or greater than 100!")
        self.final_grades.append(new_grade)


def main():
    krystal = Student("Krystal", "Wong", "A01089662", "True", "94", "95", "89", "99")
    print(krystal.get_info())
    krystal.add_final_grade("100")
    print(krystal.get_info())


if __name__ == '__main__':
    main()
