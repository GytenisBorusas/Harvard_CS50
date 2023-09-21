

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
    if validators.email(s):
        return True
    else:
        return False


if __name__ == "__main__":
    main()


