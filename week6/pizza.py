

import sys
import csv
from tabulate import tabulate



def main():
    if len(sys.argv) < 2:
        print("Too few comman-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many comman-line arguments")
        sys.exit(1)
    elif not sys.argv[1].endswith('.csv'):
        print("Not a csv file")
        sys.exit(1)

    try:
        table_data = formated_table(sys.argv[1])
        print_table(table_data)
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

def formated_table(filename):
    with open(filename, 'r') as file:
        menu = csv.DictReader(file)

        headers = next(menu)
        rows = [row for row in menu]

        return headers, rows
    
def print_table(data):
        headers, rows = data
        print(tabulate(rows, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    main()