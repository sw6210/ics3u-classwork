# 1
def add_3_numbers(a: int, b: int, c: int):
    return a + b + c

result = add_3_numbers(1, 2, 3)
print(result)


# 2
def name_and_age(name: str, age: int):
    print(f"Your name is {name} and you are {age} years old.")

name_and_age("bob", 5)


# 3
def avg_of_2_numbers(a: int, b: int):
    return (a + b) / 2

result = avg_of_2_numbers(5, 2)
print(result)


# 4
def largest_number(a: int, b: int, c: int):
    if a > b and a > c:
        return (a)
    elif b > a and b > c:
        return (b)
    else: 
        return (c)

result = largest_number(5, 4, 6)
print(result)


# 5
def first_2_characters(string: str):
    return string[0:2]

result = first_2_characters("hello")
print(result)
