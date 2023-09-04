
import re
from datetime import datetime

month_names = {
        "january": ["january", "1"],
        "february": ["february", "2"],
        "march": ["march", "3"],
        "april": ["april", "4"],
        "may": ["may", "5"],
        "june": ["june", "6"],
        "july": ["july", "7"],
        "august": ["august", "8"],
        "september": ["september", "9"],
        "october": ["october", "10"],
        "november": ["november", "11"],
        "december": ["december", "12"]
}


def get_month_number(month_name):
    for key, values in month_names.items():
        if month_name.lower() in values:
            return values[1]
    return None  # Return None if month not found


def identify_format(prompt):
    date_str = input(prompt)

    # Check for the "9/8/1636" format
    if re.match(r"\d{1,2}/\d{1,2}/\d{4}", date_str):
        month, day, year = date_str.split('/')
        return day, month, year

    # Check for the "September 8, 1636" format
    try:
        datetime.strptime(date_str, '%B %d, %Y')
        date_part, year = date_str.split(', ')
        month_name, day = date_part.split(' ')
        month = get_month_number(month_name)
        if not month:  # If month not found, raise a ValueError
            raise ValueError
        return day, month, year

    except ValueError:
        pass

    return "Unknown format"




def main():

    day, month, year = identify_format("Date: ")


    print("Month:", month)
    print("Day:", day)
    print("Year:", year)

main()