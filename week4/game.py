
import random

def main():
    while True:
        try:
            user_level_dificulty = int(input("Level: "))
            break
        except ValueError:
            print("Not a valid number")
        
    random_number = random.randrange(1, user_level_dificulty + 1)
    print(random_number)

    congratulation_message = guessing_game(random_number, user_level_dificulty)
    print(congratulation_message)




def guessing_game(random_number, user_level_dificulty):
    while True:
        try:
            user_guess = int(input("Guess: "))
            break
        except ValueError:
            print("Not a valid number")

    while user_guess != random_number:
        if user_level_dificulty > user_guess > random_number:
            print("Too large!")
        elif 0 < user_guess < random_number:
            print("Too small!")

        while True:
            try:
                user_guess = int(input("Guess: "))
                break
            except ValueError:
                print("Not a valid number")

    return "Just right"
        

if __name__ == "__main__":
    main()



