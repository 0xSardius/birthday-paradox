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
    
