

import sys
import csv


def main():
    if len(sys.argv) < 2:
        print("Too few comman-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many comman-line arguments")
        sys.exit(1)
    elif not sys.argv[1].endswith('.csv'): # and sys.argv[2].endswith('.csv'):
        print("Not a csv file(s)")
        sys.exit(1)

    try:
        students = read_data(sys.argv[1])
        for student in students:
            # used for troubleshooting
            # print(f"{student['first_name']} {student['last_name']} is in {student['house']}")
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)



def read_data(before_csv):
    students = []
    with open(before_csv, 'r') as file:
        reader = csv.reader(file)
        next(reader) #skips the header

        for line in reader:
            name = line[0]
            house = line [1]
            last_name, first_name = name.split(",")
            student = {"first_name": first_name, "last_name": last_name, "house": house}
            students.append(student)

    return students




# def write_data():







if __name__ == "__main__":
    main()