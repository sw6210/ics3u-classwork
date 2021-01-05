from math import sqrt

# Exercise 81
def main():
    while True:
        try:
            a = int(input("Enter the length of side a in cm: "))
            b = int(input("Enter the length of side b in cm: "))
            break
        except ValueError:
            print("That's not a valid length.")
    hypoteneuse_length = hypoteneuse(a, b)
    print(f"The hypoteneuse of the triangle is {hypoteneuse_length}cm.")

def hypoteneuse(a: int, b: int):
    return sqrt(a*a + b*b)

main()


#  Exercise 82
base_fare = 4.00
rate = 0.25

def main():
    while True:
        try:
            distance = int(input("Enter the number of kilometres traveled: "))
            break
        except ValueError:
            print("Invalid input.")
    fare = total_fare(distance)
    print(f"The total fare is ${fare}.")

def total_fare(distance):
    return base_fare + rate * (distance / 0.14)

main()


# Exercise 83
first_item = 10.95
subsequent_item = 2.95

def main():
    while True:
        try:
            items = int(input("How many items are you purchasing? "))
            break
        except ValueError:
            print("Invalid input.")
    shipping_fee = shipping_charge(items)
    print(f"The shipping charge is ${shipping_fee}.")

def shipping_charge(items: int):
    return first_item + subsequent_item * (items - 1)

main()


# Exercise 84
def main():
    while True:
        try:
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            c = int(input("Enter the third number: "))
            break
        except ValueError:
            print("Invalid input.")
    median_value = median(a, b, c)
    print(f"The median is {median_value}.")
    
def median(a: int, b: int, c: int):
    return a + b + c - min(a, b, c) - max(a, b, c)

main()


# Exercise 85
def main():
    while True:
        try:
            a = int(input("Enter an integer: "))
            if a > 12 or a < 1:
                raise IndexError
            ordinal_number = get_ordinal(a)
            break
        except (IndexError, ValueError):
            print("Invalid input.")
    print(ordinal_number)

def get_ordinal(a: int) -> str:
    ordinal_map = [
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
        "eleventh",
        "twelfth"
    ]
    return ordinal_map[a-1]

main()
