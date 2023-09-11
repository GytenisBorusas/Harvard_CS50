# names = []

# for _ in range(3):
#     names.append(input("What's your name?"))

# for name in sorted(names):
#     print(f" hello, {name}")

# ----------------------------------------------------------------------------

# name = input("What's your name?")


# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()

# ----------------------------------------------------------------------------

# name = input("What's your name?")


# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# ----------------------------------------------------------------------------

##### read file content

# with open("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print("hello,", line.rstrip())

# ----------------------------------------------------------------------------

### same as above but more condenced

# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello,", line.rstrip())

# ----------------------------------------------------------------------------

### read all the lines, sort them and then print
### it

# names = []

# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names):
#     print(f"hello, {name}")

 # ----------------------------------------------------------------------------

### read all the lines, sort them and then print
### it. Sane as above, but more condensed.

# with open("names.txt") as file:
#     for line in sorted(file):
#         print(f"hello,", line.rstrip()) 

 # ----------------------------------------------------------------------------

### read all the lines, sort them and then print
### it. Sane as above, but more condensed.

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")