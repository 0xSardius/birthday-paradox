import datetime, random

def getBirthdays(numberOfBirthdays):
    """Returns a list of number random date objects for birthdays"""
    birthdays = []

    for i in range(numberOfBirthdays):
        startOfYear = datetime.date(2001, 1, 1)

        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    """Returns the date object of a birthday that occurs more than once in the birthdays list."""
    if len(birthdays) == len(set(birthdays)):
        return None # All birthdays are unique, so return None
    
    # Compare each birthday to every other birthday
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA # Return the matching birthday

print("""Birthday Paradox

The birthday paradox shows us that in a group of N people, the odds that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, a simulation that does a random process by repeating it on many trial runs) to explore this concept.

""")

# Set up a tuple of month names in order
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')


max_num_birthdays = 200

while True:
    print(f"How many birthdays shall I generate? (Max {max_num_birthdays})")
    response = input("> ")
    if response.isdecimal() and (0 < int(response) <= max_num_birthdays):
        numBDays = int(response)
        break # User has entered a valid amount

print()

# Generate and display the birthdays
print(f"Here are {numBDays} birthdays:")
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Display a comma for each birthday after the first birthday
        print(", ", end="")
        monthName = MONTHS[birthday.month - 1]
        dateText = '{} {}'.format(monthName, birthday.day)
        print(dateText, end="")
print()
print()

#Determine if there are two birthdays that match
match = getMatch(birthdays)

# Display the results:
print("In this simulation, ", end="")
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print("multiple people have a birthday on", dateText)
else:
    print("there are no matching birthdays.")
print()


# Run through 100,000 simulations
print("Generating", numBDays, "random birthdays 100,000 times...")
input("Press Enter to begin...")

print("Let's run another 100,000 simulations.")
simMatch = 0 # How many simulations had matching birthdays in them
for i in range(100_000):
    if i % 10_000 == 0:
        print(i, "simulations run...")
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print("100,000 simulations run.")

# Display simulation results
probability = round(simMatch / 100_000 * 100, 2)
print("Out of 100,000 simulations of", numBDays, "people, there was a") 
print("matching birthday in that group", simMatch, "times. This means")
print("that", numBDays, "people have a", probability, "% chance of having")
print("a matching birthday in their group.")


