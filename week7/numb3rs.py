

import re
import sys


def main():
    user_input = input("IPv4 Address: ")
    is_ip_valid = validate(user_input)
    print(f"{is_ip_valid}")



# Expects an IPv4 address as input as a str and 
# then returns True or False, respectively, if that input is a valid IPv4 address or not
def validate(user_input):
    validation_statement = False

    try:
        str_oct1, str_oct2, str_oct3, str_oct4 = user_input.split(".")
    

        try:
            oct1 = int(str_oct1)
            oct2 = int(str_oct2)
            oct3 = int(str_oct3)
            oct4 = int(str_oct4)
        
            if (0 <= oct1 <= 255) and (0 <= oct2 <= 255) and (0 <= oct3 <= 255) and (0 <= oct4 <= 255):
                validation_statement = True
            else:
                validation_statement = False

        except ValueError:
            # error_message = (f"False1 - ValueError")
            pass
    except ValueError:
        # error_message = (f"False2 - ValueError")
        pass

    return validation_statement


if __name__ == "__main__":
    main()