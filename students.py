

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")

# ---------------------------------------------------------------

# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student ={}
#         student["name"] = name
#         student["house"] = house
#         students.append(student)

# for student in students:
#     print(f"{student['name]} is in {student['house']}")



# ---------------------------------------------------------------

# same as above but shortened syntax

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)


def get_name(student):
    return student["name"]

def get_house(student):
    return student["house"]

for student in sorted(students, key=get_house, reverse=True):
    print(f"{student['name']} is in {student['house']}")

