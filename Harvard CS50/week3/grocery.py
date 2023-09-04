
def main():
    grocery_list = {}
    while True:
        try:
            user_input = input()
            user_input_capitalized = user_input.capitalize()

            if user_input_capitalized in grocery_list:
                grocery_list[user_input_capitalized] += 1
            else:
                grocery_list[user_input_capitalized] = 1
        except EOFError:
            break
    
    for item, count in grocery_list.items():
        print(f"{count} {item}")

main()
    