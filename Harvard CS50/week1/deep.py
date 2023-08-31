
def main():
    user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
    lower_case_user_input = user_input.lower()
    no_space_user_input = lower_case_user_input.replace(" ", "")

    if no_space_user_input == "42":
        print("Yes")
    elif no_space_user_input == "forty-two":
        print("Yes")
    elif lower_case_user_input == "forty two":
        print("Yes")
    else:
        print("No")


main()



