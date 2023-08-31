# students = ["Hermione", "Harry", "Ron", "Draco"]

# for student in students:
#     print(student)



# for i in range(len(students)):
#     print(i + 1, students[i])

# houses = ["Gryffindor", "Griffindor", "Griffindor", "Slytherin"]


# students = {
#     "Hermione": "Gryffindor", 
#     "Harry": "Gryffindor", 
#     "Ron": "Gryffindor", 
#     "Draco": "Slytherin"
#     }
# 
# for student in students:
#     print(student, students[student], sep="---> ")

Students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "jack russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in Students:
    print(student["name"], student["house"], student["patronus"], sep="---> ")