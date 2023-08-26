

name = input("What is your name? ")

# if name == "Harry" or name == "Ron" or name == "Hermione":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")


match name:
    case "Harry", "Ron", "Hermione":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
        

