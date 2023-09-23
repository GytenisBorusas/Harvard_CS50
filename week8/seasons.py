



from datetime import date
import sys


def main():
    year, month, day = get_date()
    calculated_time = calculation(year, month, day)
    print_ready = format_time(calculated_time)
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

def calculation():
    today_year, today_month, today_day = datetime.date.today()



def format_time():
    ...
    return 






if __name__ == "__main__":
    main()



