
def main():
    joint_word = shorten("Input: ")
    # print(f"{twttr_word} print from main", end="")
    print(joint_word, end="")



def shorten(prompt):
    user_input = input(prompt)
    vowels = "AEIOUaeiou"
    twttr_list = []
    for letter in user_input:
            if letter not in vowels:
                 twttr_list.append(letter)
                 # print(f"{twttr_list} print from shorten")
            joint_word = ''.join(twttr_list)
    return joint_word


if __name__ == "__main__":
    main()