

import sys
import validators


def main():
    s = input("What is your email? ").strip()
    returned_validation = validation_of_email(s)
    if returned_validation == True:
        print("Valid")
    else:
        print(f"Invalid")
    
def validation_of_email(s):
    return_value = False

    if validators.email(s) == True:
        return_value = True
    else:
        return_value = False
    
    return return_value



if __name__ == "__main__":
    main()


