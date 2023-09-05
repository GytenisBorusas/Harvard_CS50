
from emoji import emojize

def main():
    user_input = input("Input: ")

    emojized_input = emojize(user_input, language='en')
    print(emojized_input)

if __name__ == "__main__":
    main()