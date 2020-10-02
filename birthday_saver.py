from datetime import datetime
import os


# This function returns an integer inputted by the user within a min and max
# It handles errors so the program doesn't stop if the input is invalid
def set_int_val(valName, inputMsg, minVal, maxVal):
    while True:
        val = input(inputMsg)

        try:
            val = int(val)
        except ValueError:
            print("Error:", valName, "must be an integer.")

        while not isinstance(val, int):
            val = input(inputMsg)
            try:
                val = int(val)
            except ValueError:
                print("Error:", valName, "must be an integer.")

        if val < minVal or val > maxVal:
            print("Error:", valName, "must be between", minVal, "and", maxVal, "inclusive.")
        else:
            break

    return val


def add_birthday():
    print()
    name = input("Name: ").strip()
    month = set_int_val("month", "Month (number): ", 1, 12)

    if month == 2:
        maxDay = 29
    else:
        if month > 7:
            maxDay = 30 + abs(month % 2 - 1)
        else:
            maxDay = 30 + month % 2

    day = set_int_val("day", "Day: ", 1, maxDay)

    # Year has to be a leap year so that February 29th can be added
    # Somehow I can use the birthdays dict from below
    birthdays[name] = datetime(4, month, day)
    print("Birthday added!")
    input("Press enter to continue. . . ")


def remove_birthday():
    print()
    name = input("Person's name (q to go back): ")

    if name == "q":
        return

    while name not in birthdays:
        print("Error: there is no", name, "in the current list of birthdays.")
        name = input("Person's name (q to go back): ")

        if name == "q":
            return

    birthdays.pop(name)
    print("Birthday removed!")
    input("Press enter to continue. . . ")


def print_birthdays():
    print()
    for birthday in birthdays:
        print(birthday + ":", birthdays[birthday].strftime("%B %d"))

    input("Press enter to continue. . . ")


def write_to_file():
    print()
    fileName = input("File name: ")
    f = open(fileName, "a")
    f.write("Written at " + str(datetime.now().strftime("%c")) + "\n")

    for birthday in birthdays:
        string = str(birthday) + ": " + str(birthdays[birthday].strftime("%B %d")) + "\n"
        f.write(string)

    f.write("\n")
    f.close()

    print("Birthdays written to", fileName)
    input("Press enter to continue. . . ")


def days_until_birthday():
    print()
    name = input("Person's name (q to go back): ")

    if name == "q":
        return

    while name not in birthdays:
        print("Error: there is no", name, "in the current list of birthdays.")
        name = input("Person's name (q to go back): ")

        if name == "q":
            return

    # Get the amount of days between now and selected birthday
    daysUntil = 0

    if datetime.now().month == birthdays[name].month and datetime.now().day <= birthdays[name].day:
        daysUntil = birthdays[name].day -datetime.now().day
    else:
        if datetime.now().month == 2:
            if datetime.now().year % 4 == 0:
                daysInMonth = 29
            else:
                daysInMonth = 28
        else:
            if datetime.now().month > 7:
                daysInMonth = 30 + abs(datetime.now().month % 2 - 1)
            else:
                daysInMonth = 30 + datetime.now().month % 2

        daysUntil += daysInMonth - datetime.now().day

        if (birthdays[name].month < datetime.now().month and
                birthdays[name].month == 2 and
                birthdays[name].day == 29):
            if not (datetime.now().year + 1) % 4 == 0:
                daysUntil += 28
            else:
                daysUntil += 29
        else:
            daysUntil += birthdays[name].day

        # Get months between
        currentMonth = datetime.now().month + 1
        deltaYear = 0 # Deltayear is used just in case the next year is a leap year
        while currentMonth != birthdays[name].month:
            if currentMonth == 2:
                if (datetime.now().year + deltaYear) % 4 == 0:
                    daysUntil += 29
                else:
                    daysUntil += 28
            else:
                daysUntil += 30 + currentMonth % 2

            currentMonth += 1
            if currentMonth > 12:
                currentMonth = 1
                deltaYear += 1

    # Display final answer
    if daysUntil == 0:
        print("It is", name + "'s birthday!")
    else:
        print("There are", daysUntil, "days until", name + "'s birthday!")

    input("Press enter to continue. . . ")


######## MAIN LOOP ########

# A dictionary that stores names associated with birthdays
birthdays = {}

while True:
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Print welcome message
    print("\n" + "*" * 80)
    print("Birthday storing application".center(80))
    print("*" * 80 + "\n")

    # Print list of possible actions
    print("1: Add birthday")
    print("2: Remove birthday")
    print("3: Print list")
    print("4: Write birthdays to file")
    print("5: Caculate days until chosen birthday")
    print("6: Quit\n")

    action = set_int_val("action", "Action (1/2/3/4/5/6): ", 1, 6)

    if action == 1:
        add_birthday()
    elif action == 2:
        remove_birthday()
    elif action == 3:
        print_birthdays()
    elif action == 4:
        write_to_file()
    elif action == 5:
        days_until_birthday()
    else:
        confirm = input("Are you sure? (y/n): ").lower()
        if confirm in ["y", "yes"]:
            break

