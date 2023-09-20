

import re
import sys

def main():
    s = input("Hours: ")
    time_from, time_to = convert(s)
    print(f"{time_from} to {time_to}")


def convert(s):
    match = re.search(r'(\d{1,2})(:(\d{2}))?\s*([APM]{2})\s*to\s*(\d{1,2})(:(\d{2}))?\s*([APM]{2})', s, re.IGNORECASE)
    first_hour = match.group(1)
    first_minute = match.group(3) if match.group(3) else '00'
    first_am_or_pm = match.group(4)
    second_hour = match.group(5)
    second_minute = match.group(7) if match.group(7) else '00'
    second_am_or_pm = match.group(8)

    if first_am_or_pm == "PM":
        from_hours = int(first_hour) + 12
    else:
        from_hours = int(first_hour)

    if second_am_or_pm == "PM":
        to_hours = int(second_hour) + 12
    else:
        to_hours = int(second_hour)



    time_from = str(f"{from_hours}:{first_minute}")
    time_to = str(f"{to_hours}:{second_minute}")

    return time_from, time_to


if __name__ == "__main__":
    main()



    