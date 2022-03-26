import time
import random
from typing import List

board = []
rows = 6
columns = 7
users_turn = False
win = False
full_column = False
users_wins = 0
computers_wins = 0
columns_chosen = []

def main():
    empty_slots = 42

    # instructions
    print("WELCOME TO CONNECT 4!")
    print()
    print("In this game, you will be given 21 discs.") 
    print("The objective is to get 4 of your discs in a straight line.")
    print("This can be done vertically, horizontally, or diagonally.")
    print()

    # get name
    users_name = get_name()
    print(f"Hello, {users_name}.")
    print()

    # go first or second
    while True:
        print("Would you like to go first?")
        print("[y]es")
        print("[n]o")
        choice = input(">>> ").lower()
        if choice == "y":
            users_turn = True
            print()
            break
        elif choice == "n":
            users_turn = False
            print()
            break
        else:
            print("Invalid input.")
            print()

    print("You will be playing as O. The computer will be playing as X.")
    print()

    # print board
    generate_board(columns, rows)

    # play game
    while win == False:
        print(whos_turn(users_turn))
        while True:
            if users_turn == True:
                column = users_move("Enter the column you would like to drop your disc in (1-7): ")
                check_full_column(column, columns_chosen)
                if full_column == True:
                    print("Looks like this column is full! Pick another column.")
                    print()
                else:
                    users_turn = False
                    break
            else:
                column = computers_move(full_column)
                print(f"The computer chose column {column}.")
                users_turn = True
                break
        columns_chosen.append(column)
        update_board(column, users_turn)
        empty_slots -= 1
        if empty_slots == 0:
            print("It's a tie!")
            break
        print()
        check_win(board)

    print()

    # scoreboard
    time.sleep(1)
    print()
    scoreboard(users_name, users_wins, computers_wins)
    print()

    # play again
    play_again()



def get_name():
    """Ensures the user inputs a valid name and creates a short welcome message.

    """
    while True:
        name = input("Please enter your name: ")
        if len(name) < 2 or len(name) > 15:
            print("Must be between 2 and 15 characters.")
        else:
            break
    return name


def generate_board(columns: int, rows: int):
    """Generates the board for the game.

    Args:
        columns: An integer.
        rows: An integer.
    """
    time.sleep(1)
    print("Generating board...")
    print()
    time.sleep(1)
    r = 0
    while r < rows:
        board.append(["___"] * columns) 
        board.append("")
        r += 1
    board.append("   1      2      3      4      5      6      7")
    for i in board:
        print(i)
        time.sleep(0.2)


def whos_turn(users_turn: bool) -> str:
    """Determines who's turn it is and calls the appropriate function. 

    Args:
        users_turn: True or False. True if it's the user's turn, false otherwise.

    Returns:
        A string that says who's turn it is.
    """
    if users_turn == True:
        print()
        print()
        return "It's your move."
    else:
        print()
        print()
        return "It's the computer's move."


def users_move(column_choice: int) -> int:
    """Determines which column the user would like to place their piece in and ensures that it is valid input.

    Args:
        column_choice: An integer.

    Returns:
        The column the user chose.
    """
    while True:
        try:
            choice = int(input(column_choice))
            if choice >= 1 and choice <= 7:
                break
            else:
                print("Looks like you picked a column outside of the board!")
                print()
        except ValueError:
            print("Invalid input. Must enter a number from 1-7.")
            print()
    return choice


def computers_move(full_column: bool) -> int:
    """Determines which column the computer will move.

    Args:
        full_column: True or False. True if the column is full, false otherwise.

    Returns:
        The column the computer chose.
    """
    choice = random.randint(1, 7)
    check_full_column(choice, columns_chosen)
    if full_column == True:
        choice = random.randint(1, 7)
    time.sleep(1)
    return choice
    

def update_board(column: int, users_turn: bool):
    time.sleep(1)
    """Provides an updated or current version of the board according to the user's and computer's move.

    Args:
        column: An integer from 1 to 7.
        users_turn: True or False. True if it's the user's turn, false otherwise.
    """
    # try:
    last_empty_row = 10
    while board[last_empty_row][column - 1] != "___":
        last_empty_row -= 2
    if users_turn == False:
        board[last_empty_row][column - 1] = "_O_"
    else:
        board[last_empty_row][column - 1] = "_X_"
    # except IndexError:
    #     print("Looks like the column is full.")
    
    for i in board:
        print(i)
    time.sleep(1.5)


def check_full_column(column: int, columns_chosen: List) -> bool:
    """Determines whether or not the column that was chosen is already full.

    Args:
        column: An integer from 1-7.
        columns_chosen: A list with all of the columns chosen every turn.
    
    Returns:
        True if the column is full. False otherwise.
    """
    count = 0
    for i in columns_chosen:
        if i == column:
            count += 1
            if count >= 6:
                global full_column
                full_column = True
            else:
                full_column = False
    return full_column
            



def check_win(board: List) -> bool:
    """Determines whether or not the user or the computer has 4 of their pieces in a row.

    Args:
        board: The current game board.

    Returns:
    True if there's a win. False otherwise.
    """
    
    global win
    global users_wins
    global computers_wins

    # horizontal
    for r in range(rows):
        for c in range(columns - 3):
            if board[2 * r][c] == "_O_" and board[2 * r][c + 1] == "_O_" and board[2 * r][c + 2] == "_O_" and board[2 * r][c + 3] == "_O_":
                win = True
                print("You won!")
                users_wins += 1
            elif board[2 * r][c] == "_X_" and board[2 * r][c + 1] == "_X_" and board[2 * r][c + 2] == "_X_" and board[2 * r][c + 3] == "_X_":
                win = True
                computers_wins += 1

                
    # vertical
    for r in range(rows - 3):
        for c in range(columns):
            if board[2 * r][c] == "_O_" and board[2 * r + 2][c] == "_O_" and board[2 * r + 4][c] == "_O_" and board[2 * r + 6][c] == "_O_":
                win = True
                print("You won!")
                users_wins += 1
            elif board[2 * r][c] == "_X_" and board[2 * r + 2][c] == "_X_" and board[2 * r + 4][c] == "_X_" and board[2 * r + 6][c] == "_X_":
                win = True
                print("You lost.")
                computers_wins += 1
    

    # diagonal (/)
    for r in range(4, rows + 1):
        for c in range(columns - 3):
            if board[2 * r - 2][c] == "_O_" and board[2 * r - 4][c + 1] == "_O_" and board[2 * r - 6][c + 2] == "_O_" and board[2 * r - 8][c + 3] == "_O_":
                win = True
                print("You won!")
                users_win += 1
            elif board[2 * r - 2][c] == "_X_" and board[2 * r - 4][c + 1] == "_X_" and board[2 * r - 6][c + 2] == "_X_" and board[2 * r - 8][c + 3] == "_X_":
                win = True
                print("You lost.")
                computers_win += 1
    

    # diagonal (\)
    for r in range (4, rows + 1):
        for c in range(3, columns):
            if board[2 * r - 2][c] == "_O_" and board[2 * r - 4][c - 1] == "_O_" and board[2 * r - 6][c - 2] == "_O_" and board[2 * r - 8][c - 3] == "_O_":
                win = True
                print("You won!")
                users_win += 1
            elif board[2 * r - 2][c] == "_X_" and board[2 * r - 4][c - 1] == "_X_" and board[2 * r - 6][c - 2] == "_X_" and board[2 * r - 8][c - 3] == "_X_":
                win = True
                print("You lost.")
                computers_win += 1
    
    return win



def scoreboard(name: str, users_wins: int, computers_wins: int) -> str:
    """Updates the scoreboard of the number of wins the user has to the number of wins the computer has.

    Args:
        name: The player's name.
        users_wins: An integer.
        computers_wins: An integer.
    """
    print("------------------------")
    print("       SCOREBOARD")
    print("------------------------")
    spaces = " " * (20 - len(name))
    print(f" {name}{spaces}{users_wins}")
    print(f" COMPUTER            {computers_wins}")


def play_again():
    global win
    print("Would you like to play again?")
    print("[y]es")
    print("[n]o")
    choice = input(">>> ").lower()
    if choice == "y":
        print()
        board.clear()
        columns_chosen.clear()
        win = False
        main()
    elif choice == "n":
        print("Thanks for playing!")
    else:
        print("Invalid input.")



if __name__ == "__main__":
    main()
