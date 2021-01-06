def main():
    original_string = input("Enter the word that needs centering: ")
    while True: 
        try:
            width = int(input("Enter the width of the terminal: "))
            break
        except ValueError:
            print("Invalid number.")
    new_string = center_string(original_string, width)
    print(new_string)


def center_string(original_string: str, width: int) -> str:
    left_spaces = (width - len(original_string)) // 2
    new_string = " " * left_spaces + original_string
    return new_string


def tests():
    assert center_string("a", 3) == " a"
    assert center_string("aa", 4) == " aa"
    assert center_string("b", 5) == "  b"
    assert center_string("hello", 11) == "   hello"
    assert center_string("same_length", 1) == "same_length"
    print("all passed!")


if __name__ == "__main__":
    tests()
    main()
