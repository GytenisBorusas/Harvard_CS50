

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

# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, home = line.rstrip().split(",")
#         student = {"name": name, "home": house}
#         students.append(student)

# # def get_name(student):
# #     return student["name"]

# # def get_house(student):
# #     return student["house"]

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")

# ---------------------------------------------------------------

# csv reader. Should have worked with more than 3 inputs, but it didnt. 

import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")



