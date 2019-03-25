class Student:
    """A class representing a student."""

    def __init__(self, first_name: str, last_name: str, student_num: str, status: bool):
        self.first_name = first_name
        self.last_name = last_name
        if len(student_num) != 9 or student_num[0] != "A":
            raise ValueError("The student number must be in the format A12345678!")
        else:
            self.student_num = student_num
        self.status = status
        self.final_grades = []


def main():
    Student("Krystal", "Wong", "A01089672", True)


if __name__ == '__main__':
    main()
