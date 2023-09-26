
# def main():
#     user_input = input("Greeting: ")
#     user_input = user_input.lower()
#     user_input = user_input.replace(" ", "")
#     symbols = list(user_input)
#
#    hello_list = ['h', 'e', 'l', 'l', 'o']
    # h_list = ['h']

    # if symbols[0:5] == hello_list:
    #     print("$0")
    # elif symbols[0] == ['h]']:
    #     print("$20")
    # else:
    #     print("$100")
    #
    #     # test variables
    #     print(symbols[0:5])


# ---------------------------------------

# Week 1 submitted homework

# def main():
#     user_input = input("Greeting: ")
#     user_input = user_input.lower()
#     user_input = user_input.replace(" ", "")


#     if user_input.startswith("hello"):
#         print("$0")
#     elif user_input.startswith("h"):
#         print("$20")
#     else:
#         print("$100")

# if __name__ == "__main__":
#     main()

# ---------------------------------------
# week 5 homework for unit test


def main():
    user_input = input("Greeting: ")
    print(value(user_input))

def value(greeting):
    greeting = greeting.lower().replace(" ", "")

    if greeting.startswith("hello"):
        return "$0"
    elif greeting.startswith("h"):
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()
