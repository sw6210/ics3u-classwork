def main():
    # function 1
    fruit = input("Enter your favourite fruit: ")
    name = input("Enter your name: ")
    message = fruit_and_name(fruit, name)
    print(message)
    print()


    # function 2
    while True:
        try:
            word = input("Enter a word: ")
            n = int(input("Enter an integer: "))
            break
        except ValueError:
            print("Invalid input. Must enter an integer.")
    word_repeated = word_msg(word, n)
    print(word_repeated)
    print()


    # function 3
    while True:
        try:
            a = int(input("Enter an integer: "))
            b = int(input("Enter another integer: "))
            break
        except ValueError:
            print("Invalid input. Must enter an integer.")
    sum_of_nums = add_two_nums(a, b)
    print(f"The sum of the two integers is {sum_of_nums}")
    print()


    # function 4
    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Invlaid input. Must enter an integer.")
    ticket_price = get_ticket_price(age)
    print(f"The price for your ticket is ${ticket_price}")



def fruit_and_name(fruit: str, name: str) -> str:
    """Determines the user's favourite fruit and their name.

    Args:
        fruit: The name of a fruit.
        name: The user's name.

    Returns:
        A string with both the name of the fruit and the user. 
    """

    return f"Hello {name}, your favourite fruit is {fruit}."


def word_msg(word: str, n: int) -> str:
    """Takes a word and repeats it a certain number of times.

    Args:
        word: A word.
        n: A positive integer.

    Returns:
        A string with the word repeated n times.
    """
    
    return word * n


def add_two_nums(a: int, b: int) -> int:
    """Determines the sum of two numbers.

    Args:
        a: An integer.
        b: Another integer.

    Returns:
        The sum of a and b.
    """

    return a + b


def get_ticket_price(age: int) -> float:
    """Determines the ticket price based on the age entered.

    Args:
        age: A positive integer.

    Returns:
        The appropriate ticket price as a float.
    """
    ticket_price = 0
    if age < 4:
        ticket_price = 0.00
    elif 4 <= age < 18:
        ticket_price = 7.99
    elif 18 <= age < 50:
        ticket_price = 9.99
    elif age >= 50:
        ticket_price = 4.99
    else:
        print("Invalid age.")
    
    return ticket_price

if __name__ == "__main__":
    main()
