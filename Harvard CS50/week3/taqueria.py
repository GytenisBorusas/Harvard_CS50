
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
    user_input = input("Item: ")
    user_input_lower = user_input.lower()
    user_input_titlecased = user_input_lower.title()
    print(user_input_titlecased)

main()