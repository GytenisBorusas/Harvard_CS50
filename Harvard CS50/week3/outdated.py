
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


def main():

    user_date_input = identify_format("Date: ")
    print(f"{user_date_input}")





def identify_format(prompt):
    # get input from the user
    date_str = input(prompt)

    # Check for the "9/8/1636" format
    if re.match(r"\d{1,2}/\d{1,2}/\d{4}", date_str):
        return "Short format"

    # Check for the "September 8, 1636" format
    try:
        datetime.strptime(date_str, '%B %d, %Y')
        return "Long format"
    except ValueError:
        pass

    return "Unknown format"


main()