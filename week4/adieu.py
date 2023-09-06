
import inflect

p = inflect.engine()



def main():
    all_names = get_all_names("Name: ")

    message_to_print = message_function(all_names, p)

    print(message_to_print)
    # print(f"Adieu, adieu, to {all_names}")


def get_all_names():
    name_list = []

    while True:
        try:
            names = input("Name: ")

            if name and name not in names:
                names.append(name)
        except EOFError:
            break

    return names


def message_function(all_names, p):
    joined_names = p.join(names, final_sep=" and ")

    return f"Adieu, adieu, to {joined_names}"


if __name__ == "__main__":
    main()


    

# import inflect

# p = inflect.engine()

# def main():
#     all_names = name_input("Name: ")

#     if all_names:
#         print(f"Adieu, adieu, to {all_names}")


# def name_input(prompt):

#     name_list = []

#     while True:
#         try:
#             name_entry = input(prompt)
#             if not name_entry:
#                 break

#             name_entry_lower = name_entry.lower()
#             name_entry_titlecased = name_entry_lower.title()

#             if name_entry_titlecased not in name_list:
#                 name_list = name_list + [f"{name_entry_titlecased}"]

#         except EOFError:
#             break

#     return p.join(name_list, final_sep=" and ")




# if __name__ == "__main__":
#     main()


