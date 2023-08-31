# def main():
#     print_column(3)
#
# def print_column(heigth):
#     for _ in range(heigth):
#         print("#")
# 
# main()

# def main():
#     print_row(3)
# 
# def print_row(width):
#     print("?" * width)
# 
# main()


def main():
    print_square(4)


def print_square(size):
    # for each row in square
    for i in range(size):
        #for each brick in row
        for j in range(size):
            #print brick
            print("#", end="")
        print()

main()

# test

