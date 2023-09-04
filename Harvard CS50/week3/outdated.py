import re
from datetime import datetime

month_names = {
    "january": ["january", "1"],
    # ... [rest of the dictionary unchanged]
}

def get_month_number(month_name):
    # [this function is unchanged]

def identify_format(prompt):
    date_str = input(prompt)

    # Check for the "9/8/1636" format
    if re.match(r"\d{1,2}/\d{1,2}/\d{4}", date_str):
        month, day, year = date_str.split('/')
        if int(month) >= 13:  # Note: converted month to integer for comparison
            return "Invalid month"
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
    while True:
        result = identify_format("Date: ")
        
        if isinstance(result, str) and result == "Invalid month":
            # print("Invalid month! Please try again.")
            continue  # This will jump back to the start of the loop
        
        if result == "Unknown format":
            # print("Unknown format! Please try again.")
            continue  # This will jump back to the start of the loop
        
        # If we got here, it means we have a valid format.
        day, month, year = result
        print(f"{year}-{month.zfill(2)}-{day.zfill(2)}")
        break  # Exit the loop as we have a valid date now

main()
