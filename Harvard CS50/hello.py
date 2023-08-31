# Remote whitespace from str
# name = name.strip()

# Capitalize first letter of each word
# name = name.title()

# Split user's name into first name and last name
# first, last = name.split()

# Print out "Hellow + user name from the previous line"
# print(f"Hello, {first}")


def main():
    name = input("What is your name? ") 
    hello(name)


def hello(to="World"):
    print("Hello,", to)


main()





