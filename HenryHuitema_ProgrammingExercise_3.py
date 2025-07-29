# Henry Huitema
# This program collects a list of monthly expenses from the user, and uses the reduce method
# to find and display the highest expense, lowest expense, and total expenses.

import functools

def getHigher(a, b):
    # If a is greater than b, return a. If a is less than b, return b.
    # If a and b are equal, it doesn't matter which is returned, so return b.
    if a > b:
        return a
    else:
        return b

def getLower(a, b):
    # If a is greater than b, return b. If a is less than b, return a.
    # If a and b are equal, it again doesn't matter which is returned, so return b.
    if a < b:
        return a
    else:
        return b

def keyFromValue(tar, dict):
    for key, val in dict.items():
        if val == tar:
            return key
    return ''

def main():
    keepGoing = 'y'
    expenses = {}
    # Use a while loop to take as many inputs as the user would like to provide
    while keepGoing.strip().lower() == 'y':
        try:
            expenseType = input("Input expense type: ")
            expenseAmount = float(input("Input monthly expense: "))
            expenses[expenseType] = expenseAmount
        except:
            print("Invalid input!")
        keepGoing = input("Would you like to enter another expense? (y/n) ")

    lowestExpense = functools.reduce(getLower, expenses.values())
    highestExpense = functools.reduce(getHigher, expenses.values())

    print(f"Lowest expense: {keyFromValue(lowestExpense, expenses)} (${lowestExpense})")
    print(f"Highest expense: {keyFromValue(highestExpense, expenses)} (${highestExpense})")
    print(f"Total expenses: ${functools.reduce(lambda a, b: a + b, expenses.values())}")


if __name__ == "__main__":
    main()