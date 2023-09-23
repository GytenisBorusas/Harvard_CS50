



import datetime
import sys
import inflect


def main():
    year, month, day = get_date()
    minutes = calculation(year, month, day)
    print_ready = format_time(minutes)
    print(f"{print_ready}")



def get_date():
    date_of_birth = input("Date of Birth: ")
    try:
        birth_str_year, birth_str_month, birth_str_day = date_of_birth.split("-")
        try:
            birth_int_year = int(birth_str_year)
            birth_int_month = int(birth_str_month)
            birth_int_day = int(birth_str_day)
        except ValueError:
            print("Invalid date")
            sys.exit(1)
    except ValueError:
        print("Invalid date") 
        sys.exit(1)      
    return birth_int_year, birth_int_month, birth_int_day

def calculation(birth_year, birth_month, birth_day):
    today = datetime.date.today()

    try:
        birthday = datetime.date(birth_year, birth_month, birth_day)
    except ValueError:
        print("Invalid date")
        sys.exit(1)


    delta = today - birthday
    days_since = delta.days
    minutes_since = days_since * 24 * 60

    # print(f"{days_since} days since my birth")
    print(f"{minutes_since} minutes since my birth")
    return minutes_since


def format_time(time_in_minutes):
    p = inflect.engine()
    words = p.number_to_words(time_in_minutes)
    words = words.replace(" and", "")
    # words = words.replace(", ", " ")
    # print(f"{words}")

    return words






if __name__ == "__main__":
    main()



