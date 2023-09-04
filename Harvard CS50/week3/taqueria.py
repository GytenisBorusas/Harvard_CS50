
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}



def main():
    total = menu_input("Item: ")
    
    # print(user_input_titlecased)
    print(f"Total: ${total:.2f}")


def menu_input(prompt):

    total_amount = 0.0

    while True:
        try:
            menu_input = input(prompt)
            user_input_lower = menu_input.lower()
            user_input_titlecased = user_input_lower.title()
        
            if user_input_titlecased in menu:
                total_amount = total_amount + menu[user_input_titlecased]
                print(f"Total: ${total_amount:.2f}")

        except EOFError:
            break

    return total_amount

main()