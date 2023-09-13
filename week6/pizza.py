

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
        pizza_type, small_price, large_price = formated_table(sys.argv[1])
        print(f"{pizza_type}, {small_price}, {large_price}")
    except FileNotFoundError:
        print("file does not exist")
        sys.exit(1)

def formated_table(filename):
    with open(filename, 'r') as file:
        menu = csv.DictReader(file)
        headers = next(menu)

        first_column_name = menu.fieldnames[0]

        for row in menu:
            pizza_type = row[first_column_name]
            small_price = row['Small']
            large_price = row['Large']
            return pizza_type, small_price, large_price


if __name__ == "__main__":
    main()