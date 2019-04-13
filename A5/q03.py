# Krystal Wong
# A01089672
# Theoren Leveille
# A01070327
# 08/04/2019
import os


def back_up(filename: str)-> None:
    """Create a back up file with the same file name, with the extension '.bak'"""

    file_contents = []
    try:
        with open(filename) as file_object:
            for line in file_object:
                file_contents.append(line)
    except FileNotFoundError:
        print("The file does not exist!")
        return

    backup_file_name = os.path.splitext(filename)[0] + ".bak"

    with open(backup_file_name, 'w') as file_object:
        for line in file_contents:
            file_object.write(line)

    check_file(backup_file_name, file_contents)


def check_file(filename: str, original_file_contents: list)-> None:
    """Print a message to indicate whether the file has been backed up successfully."""

    with open(filename) as file_object:
        new_file_contents = []
        for line in file_object:
            new_file_contents.append(line)

    if original_file_contents == new_file_contents:
        print("Generated " + filename)
    else:
        print("Your file could not be backed up.")


def main():
    my_file = 'importantFile.txt'
    back_up(my_file)


if __name__ == '__main__':
    main()
