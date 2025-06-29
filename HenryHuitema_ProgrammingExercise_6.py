# Henry Huitema
# This program uses regular expressions to validate a user supplied phone number,
# social security number, and ZIP code.

import re

def validatePhoneNumber(userString):
    # Pattern is three digits, hyphen, three digits, hyphen, four digits.
    pattern = r'\d{3}-\d{3}-\d{4}$'
    if re.match(pattern, userString):
        print("Valid phone number!")
    else:
        print("Invalid phone number!")


def validateSSN(userString):
    # Pattern is three digits, hyphen, two digits, hyphen, four digits.
    pattern = r'\d{3}-\d{2}-\d{4}$'
    if re.match(pattern, userString):
        print("Valid social security number!")
    else:
        print("Invalid social security number!")

def validateZipCode(userString):
    # This function will match two different ZIP code formats: Five digits alone,
    # or five digits followed by a hyphen and four digits.
    pattern1 = r'\d{5}$'
    pattern2 = r'\d{5}-\d{4}$'
    if re.match(pattern1, userString):
        print("Valid ZIP code!")
    else:
        print("Invalid ZIP code!")

def main():
    validatePhoneNumber(input("Enter phone number: "))
    validateSSN(input("Enter social security number: "))
    validateZipCode(input("Enter ZIP code: "))


if __name__ == "__main__":
    main()
