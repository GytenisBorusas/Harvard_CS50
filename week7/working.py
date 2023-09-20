

import re
import sys

def main():
    s = input("Hours: ")
    time_from, time_to = convert(s)
    print(f"{time_from} to {time_to}")


def convert(s):
    match = re.search(r'(\d{1,2})(:(\d{2}))?\s*([APM]{2})\s*to\s*(\d{1,2})(:(\d{2}))?\s*([APM]{2})', s, re.IGNORECASE)

    if not match:
        raise ValueError("Invalid time format")
        sys.exit(1)

    first_hour = int(match.group(1))
    first_minute = int(match.group(3)) if match.group(3) else 0
    first_am_or_pm = match.group(4).upper()

    second_hour = int(match.group(5))
    second_minute = int(match.group(7)) if match.group(7) else 0
    second_am_or_pm = match.group(8).upper()

    if first_am_or_pm == "PM" and first_hour != 12:
        first_hour += 12
    elif first_am_or_pm == "AM" and first_hour == 12:
        first_hour = 0

    if second_am_or_pm == "PM" and second_hour != 12:
        second_hour += 12
    elif second_am_or_pm == "AM" and second_hour == 12:
        second_hour = 0

    # if from_hours == 24:
    #     from_hours = 0
    # elif from_hours > 24:
    #     raise ValueError
    #     sys.exit(1)
    
    # if to_hours == 24:
    #     to_hours = 0
    # elif to_hours > 24:
    #     raise ValueError
    #     sys.exit(1)
        

    if int(first_minute) >= 60:
        raise ValueError
        sys.exit(1)

    
    if int(second_minute) >= 60:
        raise ValueError
        sys.exit(1)

     

    time_from = str(f"{first_hour:02}:{first_minute:02}")
    time_to = str(f"{second_hour:02}:{second_minute:02}")

    return time_from, time_to


if __name__ == "__main__":
    main()



    