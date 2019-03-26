class Student:
    """A class representing a student."""

    def __init__(self, first_name: str, last_name: str, student_num: str, status: bool, final_grades: list):
        if len(first_name.split()) == 0:
            print("First name cannot be blank!")
            raise ValueError
        else:
            self.first_name = first_name.title()

        if len(last_name.split()) == 0:
            print("Last name cannot be blank!")
            raise ValueError
        self.last_name = last_name.title()

        if len(student_num) == 9 and student_num[0] == "A" and student_num[1:].isdigit():
            self.student_num = student_num
        else:
            print("The student number must be the character A, followed by 8 digits!")
            raise ValueError

        self.status = status

        for grade in final_grades:
            if int(grade) < 0 or int(grade) > 100:
                print("A grade cannot be less than 0 or greater than 100!")
                raise ValueError
            else:
                self.final_grades = final_grades

    def get_grades(self):
        grades = ""
        for grade in self.final_grades:
            grades += str(grade) + " "
        return grades

    def get_info(self):
        return (self.first_name + " " + self.last_name + " " + self.student_num + " " + str(self.status)
                + " " + self.get_grades())


def main():
    krystal = Student("Krystal", "Wong", "A01089662", True, [94, 95, 89, 99])
    print(krystal.get_info())


if __name__ == '__main__':
    main()
