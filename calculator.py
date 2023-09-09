# x = float(input("What's x? "))
# y = float(input("What's y? "))

# z = round(x + y, 1)

# print(f"{z:,}")

def main():
    x = input("What is x? ")
    print("x squared is", square(x))

def square(n):
    return n * n

if __name__ == "__main__":
    main()