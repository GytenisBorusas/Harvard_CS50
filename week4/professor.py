import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        tries = 3
        
        while tries:
            answer = input(f"{x} + {y} = ")
            
            if answer.isdigit() and int(answer) == x + y:
                score += 1
                break
            else:
                print("EEE")
                tries -= 1
                
        if not tries:
            print(f"{x} + {y} = {x + y}")
            
    print(f"Your score: {score}/10")



def get_level():
    while True:
        try:
            n = int(input("1Level: "))
            if n == 1 or n == 2 or n == 3:
                break
        except ValueError:
            print("Not a valid number")
    return n


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level!")





if __name__ == "__main__":
    main()