from typing import List

def main():
    student_list = []
    mark_list = []

    # get user's name
    name = user_name()
    print()

    # display welcome message
    welcome_message = return_name_message(name)
    print(welcome_message)
    print()

    # ask for number of marks
    number = int(input("Enter the number of students: "))
    number_of_student_marks = number_of_marks(number)
    print()

    # report names and marks
    report = student_mark_report(student_list, mark_list)
    print(report)


def user_name():
    name = input("Please enter your name: ")
    valid = False
    while valid == False:
        if len(name) >= 2 and len(name) <= 15:
            valid = True
        else:
            print ("Invalid input. Please enter your name again.")
    return name
    

def return_name_message(name: str) -> str:
    return f"Hello, {name}. Welcome to the Markbook Program."


def number_of_marks(number: int) -> int:
    valid = False
    while valid == False:
        if number < 0:
            print("Invalid input.")
        else: 
            valid = True
    return number


def student_mark_report(students: List[str], marks: List[int]) -> str:
    i = 0
    while i < number_of_student_marks:
        student = input("Enter a student's name: ")
        student_list.append(student)
        mark = input("Enter his/her mark: ")
        mark_list.append(mark)
        print()
        i += 1
    

def failing_students(marks: List[int]) -> int:
    i = 0
    fail = False
    count = 0
    while i < len(marks):
        if marks[i] < 50:
            fail = True
            count += 1
        else:
            ()
        i += 1
    return count



if __name__ == "__main__":
    main()
