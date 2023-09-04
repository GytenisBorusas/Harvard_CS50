
# try:
#     x = int(input("Whats x?  "))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")

#-----------------------------------------------------

# while True:
#     try:
#         x = int(input("Whats x? "))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break

# print(f"x is {x}")

#-----------------------------------------------------
# def main():
#     x = get_init()
#     print(f"x is {x}")

# def get_init():
#     while True:
#         try:
#             x = int(input("Whats x? "))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             break

#     return x

# main()

#-----------------------------------------------------
# def main():
#     x = get_init()
#     print(f"x is {x}")

# def get_init():
#     while True:
#         try:
#             x = int(input("Whats x? "))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             return x
        

# main()


#-----------------------------------------------------
def main():
    x = get_init("What's x? ")
    print(f"x is {x}")

def get_init(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            print("x is not an integer")
        else:
            return x
        

main()