import random


def main():
    ...


def get_level():
    while True:
        try:
            n = int(input("1Level: "))
            if n == 1 or n == 2 or n == 3:
                break
        except ValueError:
            print("Not a valid number")


def generate_integer(level):
    ...





if __name__ == "__main__":
    main()