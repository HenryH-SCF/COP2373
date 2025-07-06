# Henry Huitema
# This program collects grade information about students taking a class that gives three exams.
# The user is first prompted for a number of grades to be entered. It then takes students' full names
# and grades as user inputs, stores them in a CSV file named grades.csv, then prints the contents of
# grades.csv in a tabular format.

import csv

def csvWrite():
    with open("grades.csv", "w", newline="") as csvfile:
        # Prompt user for how many grades need to be entered. If user input cannot be converted to an integer,
        # default to one row.
        try:
            gradesEntered = int(input("How many grades would you like to enter? "))
        except:
            print("Could not read user input! Using default value of 1...")
            gradesEntered = 1

        csvwriter = csv.writer(csvfile, delimiter=",")
        # Set up a while loop to guarantee that the specified number of rows are entered, even if
        # the code within the try block throws an exception.
        iterations = 0
        while iterations < gradesEntered:
            try:
                firstName = input("Student first name: ")
                lastName = input("Student last name: ")
                examOne = int(input("Exam one grade: "))
                examTwo = int(input("Exam two grade: "))
                examThree = int(input("Exam three grade: "))
                csvwriter.writerow([firstName, lastName, examOne, examTwo, examThree])
                iterations += 1
            except:
                print("An error has occurred!")
        csvfile.close()

def csvRead():
    with open("grades.csv", "r", newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        # Print a header row for the 'table'
        print(f"First name | Last name | Exam One | Exam Two | Exam Three")
        for row in csvreader:
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")
    csvfile.close()

def main():
    csvWrite()
    csvRead()

if __name__ == "__main__":
    main()
