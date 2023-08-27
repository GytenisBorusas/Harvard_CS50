# user_number = int(input("How many times to print 'meow'? "))
#
# while user_number > 0:
#     print("meow")
#     user_number -= 1


# user_number = int(input("How many times to print 'meow'? "))
#
# for _ in range(user_number):
#     print("meow")



# user_number = int(input("How many times to print 'meow'? "))
#
# print("meow\n" * user_number, end="")



# while True:
#     n = int(input(" What's n? "))
#     if n > 0:
#         break
# 
# for _ in range(n):
#     print("meow")
        



def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input(" What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()