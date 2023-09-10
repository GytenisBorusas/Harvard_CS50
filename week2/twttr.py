
def main():
    twttr_word = shorten("Input: ")
    print(twttr_word, end="")



def shorten(word):
    vowels = "AEIOUaeiou"
    twttr_list = []
    for letter in word:
            if letter not in vowels:
                 twttr_list.append(letter)
    return twttr_list


if __name__ == "__main__":
    main()