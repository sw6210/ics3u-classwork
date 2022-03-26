import time

hours_spent = 0
screen_time = 0

def recommended_screen_time() -> int:
    """Tells the user how many hours they should be spending looking at a screen based on their age.

    Returns:
        An integer representing the number of hours they have set their screen time to.

    Done by: Sarah
    """
    global screen_time

    while True:
        try:
            age = int(input("Please enter the age of the user of this device: "))
            if age < 4:
                recommended_time = 0
            elif age >= 4 and age < 8:
                recommended_time = 1
            elif age >= 8 and age < 12:
                recommended_time = 2
            else:
                recommended_time = 3
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    while True:
        print(f"Your recommended screen time is {recommended_time} hours.")
        print()
        print("Would you like to set this as your limit?")
        print("[y]es")
        print("[n]o")
        choice = input(">>> ").lower()
        print()
        if choice == "y":
            screen_time = recommended_time
            break
        elif choice == "n":
            while True:
                screen_time = int(input("Enter the amount of hours you would like as a limit: "))
                if screen_time >= 5:
                    print("That seems like too many hours! Are you sure you would like to set this as your limit? ")
                    print("[y]es")
                    print("[n]o")
                    choice = input(">>> ").lower()
                    print()
                    if choice == "y":
                        break
                    elif choice == "n":
                        print("Please re-enter your choice.")
                    else:
                        print("Invalid input.")
                elif screen_time < 0:
                    print("Invalid input.")
                else:
                    break
            break
        else:
            print("Invalid input.")
    print()
    print(f"You have set your screen time limit to {screen_time} hours.")
    return screen_time

      
def reminders(hours_spent: int, screen_time: int):
    """Creates notifications every so often to remind the user to take 20 second breaks.
    
    Args:
        hours_spent: An integer representing how many hours the user has spent on their device.
        screen_time: An integer representing the number of hours the user should be spending.

    Done by: Sarah
    """
    if hours_spent == screen_time * 60 - 30:
        print("You have 30 minutes left of screen time.")
    elif hours_spent == screen_time:
        print("You have run out of screen time.")
    elif hours_spent > screen_time:
        print("Looks like you have gone over your screen time limit!")
    else:
        while hours_spent < screen_time:
            print("Remember to take breaks in between! Rest your eyes and take some time to stretch.")
            time.sleep(1200)
      
recommended_screen_time()
reminders(hours_spent, screen_time)


def brightness():
    """Lowers the brightness of the screen during a specific time frame.

    Done by: Nolan
    """
    pass



def screen_colour():
    """Changes the tint and contrast of the screen depending on time of day.

    Done by: Nolan
    """
    pass





def	text_size():
	"""Adjusts the size of any text, including text from different websites that use their own text size.
	
	Asks the user if the text is comfortably readable whenever they open a new page/website and adjusts depending on their answer.

	Returns reajusted text depending on the answer

	Done by: Kimberly
	"""

	visible = input("It looks like you're on a new page. Is the text readable for you? ")

	if visible == "Yes":
		print("Good!")

	elif visible == "No":
		size = input("Is the text too large or too small? ")
		
		if size == ("large"):
			print("The text has been shrunk.")

		elif size == ("small"):
			print("The size has been increased.")

def screen_distance():
	"""Determines how far the user is from the screen of the device.

	Asks user for their distance from the computer, tells them if they are too close or too far from the screen.

	Returns a message depending if the user is too close, too far or a good distance

	Done by: Kimberly
	"""
	distance = int(input("How far are you from your screen? (cm) "))

	if distance <= 49:
		print("You're too close to the screen, you should move back.")

	elif 50 <= distance <= 100:
		print("You're a good distance from your computer!")

	elif distance > 101:
		print("You're too far from your computer screen, move closer.")

text_size()
screen_distance()
