


# def main():
#     name = get_name()
#     house = get_house()
#     print(f"{name} from {house}")

# def get_name():
#     return input("Name: ")

# def get_house():
#     return input("House: ")

# if __name__ == "__main__":
#     main()


# ---------------------------------------


# def main():
#     student = get_student()
#     if student[0] == "Paddma":
#         student[1] = "Ravenclaw"
#     print(f"{student[0]} from {student[1]}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return [name, house]

# if __name__ == "__main__":
#     main()



# ---------------------------------------


def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student

    # same as above
    # name = input("Name: ")
    # house = input("House: ")
    # return {"name": name, "house": house}

if __name__ == "__main__":
    main()


