# Henry Huitema

import numpy as np
import csv

def csvToArray(fileName):
    twoDimensionList = []
    with open(fileName, "r", newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        for row in csvreader:
            twoDimensionList.append(row)
    return np.array(twoDimensionList).astype(object)

def main():
    dataArray = csvToArray("grades.csv")
    # Exam One
    dataArray[:, 2] = dataArray[:,2].astype(int)
    # Exam Two
    dataArray[:, 3] = dataArray[:, 3].astype(int)
    # Exam Three
    dataArray[:, 4] = dataArray[:, 4].astype(int)

    print(dataArray[:3,:], '\n')

    print(f"Exam 1 Average: {np.mean(dataArray[:,2])}")
    print(f"Exam 2 Average: {np.mean(dataArray[:,3])}")
    print(f"Exam 3 Average: {np.mean(dataArray[:,4])}\n")

    print(f"Exam 1 Median: {np.median(dataArray[:,2])}")
    print(f"Exam 2 Median: {np.median(dataArray[:, 3])}")
    print(f"Exam 3 Median: {np.median(dataArray[:, 4])}\n")

    print(f"Exam 1 Standard Deviation: {np.std(dataArray[:,2])}")
    print(f"Exam 2 Standard Deviation: {np.std(dataArray[:, 3])}")
    print(f"Exam 3 Standard Deviation: {np.std(dataArray[:, 4])}\n")

    print(f"Exam 1 Lowest Score: {np.min(dataArray[:,2])}")
    print(f"Exam 2 Lowest Score: {np.min(dataArray[:, 3])}")
    print(f"Exam 3 Lowest Score: {np.min(dataArray[:, 4])}\n")

    print(f"Exam 1 Highest Score: {np.max(dataArray[:,2])}")
    print(f"Exam 2 Highest Score: {np.max(dataArray[:, 3])}")
    print(f"Exam 3 Highest Score: {np.max(dataArray[:, 4])}\n")

    print(f"All Exams Average: {np.mean(dataArray[:,2:5])}")
    print(f"All Exams Median: {np.median(dataArray[:,2:5])}")
    print(f"All Exams Standard Deviation: {np.std(dataArray[:,2:5])}")
    print(f"Overall Lowest Score: {np.min(dataArray[:,2:5])}")
    print(f"Overall Highest Score: {np.max(dataArray[:,2:5])}\n")

    print(f"{np.sum(dataArray[:, 2] >= 60)} student(s) passed Exam One.")
    print(f"{np.sum(dataArray[:, 2] < 60)} student(s) failed Exam One.")
    print(f"{np.sum(dataArray[:, 3] >= 60)} student(s) passed Exam Two.")
    print(f"{np.sum(dataArray[:, 3] < 60)} student(s) failed Exam Two.")
    print(f"{np.sum(dataArray[:, 4] >= 60)} student(s) passed Exam Three.")
    print(f"{np.sum(dataArray[:, 4] < 60)} student(s) failed Exam Three.")
    print(f"{(np.mean(dataArray[:,2:5] >= 60)) * 100}% of exams were completed with a passing grade.")



if __name__ == "__main__":
    main()