import random

def main():
    while True:
        try:
            user_level_dificulty = int(input("Level: "))
            if user_level_dificulty > 0:
                break
            else:
                print("Level should be a positive number greater than 0!")
        except ValueError:
            print("Not a valid number")

        
    random_number = random.randrange(1, user_level_dificulty + 1)
    print(random_number)

    congratulation_message = guessing_game(random_number, user_level_dificulty)
    print(congratulation_message, end='')


def guessing_game(random_number, user_level_dificulty):
    user_guess = None

    while user_guess != random_number:
        while True:
            try:
                user_guess = int(input("Guess: "))
                if 1 <= user_guess <= user_level_dificulty:
                    break
                else:
                    print("Guess out of range")
            except ValueError:
                print("Not a valid number")
        
        if user_guess != random_number:
            if user_guess > random_number:
                print("Too large!")
            else:
                print("Too small!")

    return "Just right!"


if __name__ == "__main__":
    main()
