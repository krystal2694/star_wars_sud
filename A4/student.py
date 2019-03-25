class Student:
    """A class representing a student."""

    def __init__(self, first_name: str, last_name: str, student_num: str, status: bool, final_grades: list):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        if len(student_num) == 9 and student_num[0] == "A" and student_num[1:].isdigit():
            self.student_num = student_num
        else:
            raise ValueError("The student number must be the character A, followed by 8 digits!")

        self.status = status
        self.final_grades = final_grades


def main():
    krystal = Student("Krystal", "Wong", "A01089662", True, [])
    print(krystal.final_grades)


if __name__ == '__main__':
    main()
