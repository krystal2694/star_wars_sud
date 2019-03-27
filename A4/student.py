class Student:
    """A class representing a student."""

    def __init__(self, first_name: str, last_name: str, student_num: str, status: str, *final_grades: str):
        if first_name.isalpha():
            self.first_name = first_name.title()
        else:
            print("First name must only be made up of alphabetical characters!")
            raise ValueError

        if last_name.isalpha():
            self.last_name = last_name.title()
        else:
            print("Last name must only be made up of alphabetical characters!")
            raise ValueError

        if len(student_num) == 9 and student_num[0] == "A" and student_num[1:].isdigit():
            self.student_num = student_num
        else:
            print("The student number must be the character A, followed by 8 digits!")
            raise ValueError

        self.status = status

        self.final_grades = []
        for grade in final_grades:
            if int(grade) < 0 or int(grade) > 100:
                print("A grade cannot be less than 0 or greater than 100!")
                raise ValueError
            else:
                self.final_grades.append(grade)


    def get_final_grades(self):
        return self.final_grades

    def get_final_grades_str(self):
        grades = ""
        if len(self.final_grades) > 0:
            for grade in self.final_grades:
                grades += grade + " "
        return grades

    def get_info(self):
        return self.first_name + " " + self.last_name + " " + self.student_num + " " + self.status \
               + " " + self.get_final_grades_str()


def main():
    krystal = Student("Krystal", "Wong", "A01089662", "True", "94", "95", "89", "99")
    print(krystal.get_info())


if __name__ == '__main__':
    main()
