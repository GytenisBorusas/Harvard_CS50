import inflect

p = inflect.engine()

def main():
    all_names = get_all_names()
    message_to_print = message_function(all_names, p)
    print(message_to_print)


def get_all_names():
    names_list = []
    try:
        while True:
            name = input()
            if name:
                names_list.append(name)
    except EOFError:
        pass
    return names_list


def message_function(all_names, p):
    # joined_names = p.join(all_names, final_sep=" and ")
    joined_names = p.join(all_names)
    return f"Adieu, adieu, to {joined_names}".strip()

if __name__ == "__main__":
    main()
