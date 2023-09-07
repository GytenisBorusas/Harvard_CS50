
import random

def main():
    user_level_dificulty = int(input("Level: "))

    random_number = random.randrange(1, user_level_dificulty + 1)
    print(random_number)

    user_guess = int(input("Guess: "))
    while user_guess != random_number:
        if user_level_dificulty > user_guess > random_number:
            print("Too large!")
        elif 0 < user_guess < random_number:
            print("Too small!")
        
        user_guess = int(input("Guess: "))
    
    print("Just right!")

main()

