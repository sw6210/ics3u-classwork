# main
------
from typing import List

def main():
    # Ask teacher for name (function 1)
    teacher_name = get_name("Enter your name: ")

    # Print out a welcome message (function 2)
    welcome_message = print_welcome_message(teacher_name)
    print(welcome_message)
    print()

    # Ask how many student marks they want to enter (function 3)
    class_size = get_positive_integer("Enter the number of students in your class: ")
    print()

    # Use number to create loop
    student_names = []
    student_marks = []
    i = 0
    while i < class_size:
        # Get student name and add to list of names
        name = get_name(f"Enter student {i + 1}'s name: ")
        student_names.append(name)

        # Get student mark and add to list of marks
        mark = get_positive_integer("Enter his/her mark: ")
        student_marks.append(mark)
        print()
        i += 1

    # Display report of student names and marks (function 4)
    print("Mark Report")
    print("-----------")
    display_report(student_names, student_marks)
    print()

    # Display number of failing students (function 5)
    fails = number_of_fails(student_marks)
    print(f"{fails} student(s) failed.")


    # Calculate class average
    class_average = calc_class_average(student_marks, class_size)
    print (f"The class average is {class_average}%.")


def get_name(name):
    while True:
        name = input(name)
        if len(name) >=2 and len(name) <= 15:
            return name
        else:
            print("Name must be 2 to 5 characters long.")


def print_welcome_message(name: str) -> str:
    return f"Hello {name}. Welcome to the Markbook Program."


def get_positive_integer(number):
    while True:
        number = int(input(number))
        try:
            if number < 0:
                print("Invalid. Must be a positive number.")
                print()
        except ValueError:
            print("Must input an integer.")


def display_report(student_names: List, student_marks: List) -> str:
    i = 0
    while i < len(student_names):
        print(student_names [i], student_marks[i])
        i += 1


def number_of_fails(student_marks: List) -> int:
    count = 0
    for i in student_marks:
        if i < 50:
            count += 1
    return count


def calc_class_average(student_marks: List, class_size: int) -> float:
    average = round(sum(student_marks) / class_size, 2)
    return average


if __name__ == "__main__":
    main()
    
    
# tests
-------

from main import print_welcome_message
from main import number_of_fails
from main import calc_class_average

def test_print_welcome_message():
    assert print_welcome_message("Bob") == "Hello, Bob. Welcome to the Markbook Program."

student_marks = [
        [24, 53, 75, 98, 45, 65, 87, 89, 78],
        [76, 98, 54, 69],
        [23, 53, 79, 90, 88, 96],
        [76, 89],
    ]

class_size = [9, 4, 6, 2]


def test_print_welcome_message():
    assert print_welcome_message("Bob") == "Hello, Bob. Welcome to the Markbook Program."


def test_number_of_fails():
    assert number_of_fails(student_marks[0]) == 2
    assert number_of_fails(student_marks[1]) == 0
    assert number_of_fails(student_marks[2]) == 1
    assert number_of_fails(student_marks[3]) == 0


def test_calc_class_average():
    assert calc_class_average(student_marks[0], class_size[0]) == 68.22
    assert calc_class_average(student_marks[1], class_size[1]) == 74.25
    assert calc_class_average(student_marks[2], class_size[2]) == 71.50
    assert calc_class_average(student_marks[3], class_size[3]) == 82.50
