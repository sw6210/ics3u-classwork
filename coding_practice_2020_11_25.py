# Exercise 34
x = int(input("Enter an integer: "))
if x % 2 == 1:
    print(x, "is odd.")
else:
    print(x, "is even.")


# Exercise 35
human_years = int(input("Enter the number of human years: "))
if 0 <= human_years <= 2:
    dog_years = human_years * 10.5
    print(f"This is the same as {dog_years} dog years.")
elif human_years > 2:
    dog_years = 21 + (human_years - 2) * 4
    print(f"This is the same as {dog_years} dog years.")
else:
    print("The number you entered is not valid.")


# Exercise 36
letter = input("Enter a letter of the alphabet: ")
if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("The letter you entered is a vowel.")
elif letter == "y":
    print("The letter you entered is sometimes a vowel and sometimes a consonant.")
else:
    print("The letter you entered is a consonant.")


# Exercise 37
x = int(input("Enter the number of sides: "))
if  x == 3:
    print("The shape is a triangle.")
elif x == 4:
    print("The shape is a quadrilateral.")
elif x == 5:
    print("The shape is a pentagon.")
elif x == 6:
    print("The shape is a hexagon.")
elif x == 7:
    print("The shape is a heptagon.")
elif x == 8:
    print("The shape is an octagon.")
elif x == 9:
    print("The shape is a nonagon.")
elif x == 10:
    print("The shape is a decagon.")
else:
    print("The number of sides is not supported by the program.")


# Exercise 38:
month = (input("Enter the name of a month: "))
if month == "April" or month == "June" or month == "September" or month == "November":
    days = 30
elif month == "January" or month == "March"or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
    days = 31
elif month == "February":
    days = "28 or 29"
else:
    print("Invalid input.")
print(f"{month} has {days} days in it.")


# Exercise39
sound_level =  int(input("Enter the sound level in decibels: "))
if sound_level >= 40 and sound_level <= 70:
    print(f"{sound level} decibels is in between a quiet room and an alarm clock.")
elif sound_level >= 70 and sound_level <= 106:
    print(f"{sound level} decibels is in between an alarm clock and a gas lawnmower.")
elif sound_level >= 106 and sound_level <= 130:
    print(f"{sound level} decibels is in between a gas lawnmower and a jackhammer.")
else:
    print("The value you have inputted is not supported by this program.")



# Exercise 40:
length_a = float(input("Enter the length of a side: "))
length_b = float(input("Enter the length of another side: "))
length_c = float(input("Enter the length of the last side: "))

if length_a == length_b and length_b == length_c:
    triangle = "equilateral"
elif length_a == length_b or length_b == length_c or length_c == length_a:
    triangle = "isosceles"
else:
    triangle = "scalene"
print(fIt is a(n) {triangle} triangle.")


# Exercise 41
note_name = input("Enter the note name: ").upper()
note = note_name[0]
octave = int(note_name[1])
if note == "C":
    frequency = 261.63
elif note == "D":
    frequency = 293.66
elif note == "E":
    frequency = 329.63
elif note == "F":
    frequency = 349.23
elif note == "G":
    frequency = 392.00
elif note == "A":
    frequency = 440.00
elif note == "B":
    frequency = 493.88
frequency = frequency / 2 ** (4 - octave)
print(f"The frequncy of {note_name} is {frequency}.")


# Exercise 42
frequency = float(input("Enter the frequency of the note: "))
if frequency >= 260.63 and frequency <= 262.63:
    note = "C4"
elif frequency >= 292.66 and frequency <= 293.66:
    note = "D4"
elif frequency >= 328.63 and frequency <= 330.63:
    note = "E4"
elif frequency >= 348.23 and frequency <= 350.23:
    note = "F4"
elif frequency >= 391.00 and frequency <= 393.00:
    note = "G4"
elif frequency >= 439.00 and frequency <= 441.00:
    note = "A4"
elif frequency >= 492.88 and frequency <= 494.88:
    note = "B4"
else:
    print("The frequency does not correspond to a known note.")
print(f"The frequency produces the note {note}.")


# Exercise 45
row = int(input("Enter the row number of the position: "))
column = input("Enter the column letter of the position: ")
if row % 2 == 0 and column == "b" or column == "d" or column == "f" or column == "h":
    print("The square of the position is black.")
elif row % 2 == 1 and column == "a" or column == "c" or column == "e" or column == "g":
    print("The square of the position is black.")
else:
    print("The square of the position is white.")
