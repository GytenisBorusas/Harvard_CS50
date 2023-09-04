
def main():
    camel_case_str = input("CamelCase: ")
    print(f"snake_case: {camel_to_snake(camel_case_str)}")

def camel_to_snake(camel_case_str):
    snake_case = []

    for char in camel_case_str:
        # If character is uppercase, append underscore and its lowercase
        if char.isupper():
            snake_case.append('_')
            snake_case.append(char.lower())
        # If character is not uppercase, just append it
        else:
            snake_case.append(char)

    # Join the list to a string and return
    return ''.join(snake_case)


if __name__ == "__main__":
    main()