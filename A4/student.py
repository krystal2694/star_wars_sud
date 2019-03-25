class Student:
    """A class representing a student."""

    def __init__(self, first_name: str, last_name: str, student_num: str, status: str):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.student_num = student_num
        self.status = status
        self.final_grades = []


def main():
    pass


if __name__ == '__main__':
    main()
