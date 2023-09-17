

import re
import sys


def main():
    # print(validate(input("IPv4 Address: ")))
    user_ip_address = validate()
    print(user_ip_address)



# Expects an IPv4 address as input as a str and 
# then returns True or False, respectively, if that input is a valid IPv4 address or not
def validate():
    user_input = str(input("IPv4 Address: "))
    try:
        str_oct1, str_oct2, str_oct3, str_oct4 = user_input.split(".")
    except ValueError:
        print(f"False1 - ValueError")

    try:
        oct1 = int(str_oct1)
        oct2 = int(str_oct2)
        oct3 = int(str_oct3)
        oct4 = int(str_oct4)
    except UnboundLocalError:
        print(f"False2 - UnboundLocalError")
    except ValueError:
        print(f"False3 - ValueError")

    
    try:
        if 0 <= oct1 and oct2 and oct3 and oct4 <= 255:
            validation_statement = str("True")
        else:
            validation_statement = str("False")
    except UnboundLocalError:
        print(f"False4 - UnboundLocalError")
        return validation_statement


if __name__ == "__main__":
    main()