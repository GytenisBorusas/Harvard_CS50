

import sys
import csv


def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    input_csv = sys.argv[1]
    output_csv = sys.argv[2]

    if not (input_csv.endswith('.csv') and output_csv.endswith('.csv')):
        print("Not a csv file(s)")
        sys.exit(1)


    try:
        students = read_data(sys.argv[1])
        for student in students:
            # used for troubleshooting
            write_data(students, output_csv)
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
            house = line [1].strip()
            last, first = name.split(",")
            student = {"first": first, "last": last, "house": house}
            students.append(student)

    return students

def write_data(students, after_csv):
    # Define the header
    fieldnames = ['first', 'last', 'house']

    with open(after_csv, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        # Write header
        writer.writeheader()
        # Write student data
        writer.writerows(students)



if __name__ == "__main__":
    main()