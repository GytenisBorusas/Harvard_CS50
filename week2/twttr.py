
def main():
    user_input = input("Input: ")
    vowels = "AEIOUaeiou"
    for letter in user_input:
            if letter not in vowels:
                print(letter, end="")


main()