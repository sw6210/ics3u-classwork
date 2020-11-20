# Create a program that will ask the user for their favourite colour. Have the program output a message saying something like: "Blue?! No way, that's my favourite colour too!".
favourite_colour = (input("What is your favourite colour? "))
print(f"{favourite_colour}?! No way, that's my favourite colour too!")

# 2. Create a program that asks how many cans come in a pack. Then ask teh user how many packs there are. Output a message indicating the total number of cans.
cans = int(input("How many cans come in a pack?: "))
packs = int(input("How many packs are there?: "))
total_cans = cans * packs
print(f"There are {total_cans} cans in total.")

# 3. Ask the user for the three dimensions of a rectangular prism. Output the volume.
length = int(input("Enter the length of the rectangular prism: "))
width = int(input("Enter the width of the rectangular prism: "))
height = int(input("Enter the height of the rectangular prism: "))
volume = length * width * height
print(f"The volume of the rectangular prism is {volume} units squared.")
