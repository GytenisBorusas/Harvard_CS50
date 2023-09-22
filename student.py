


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


# def main():
#     student = get_student()
#     print(f"{student['name']} from {student['house']}")

# def get_student():
#     student = {}
#     student["name"] = input("Name: ")
#     student["house"] = input("House: ")
#     return student

#     # same as above
#     # name = input("Name: ")
#     # house = input("House: ")
#     # return {"name": name, "house": house}

# if __name__ == "__main__":
#     main()



# ---------------------------------------


# def main():
#     student = get_student()
#     if student["name"] == "Padma":
#         student["house"] = "Ravenclaw"
#     print(f"{student['name']} from {student['house']}")

# def get_student():
#     student = {}
#     student["name"] = input("Name: ")
#     student["house"] = input("House: ")
#     return student

#     # same as above
#     # name = input("Name: ")
#     # house = input("House: ")
#     # return {"name": name, "house": house}

# if __name__ == "__main__":
#     main()


# ---------------------------------------



# # learning class'es
# class Student:
#     def __init__(self, name, house):
#         self.name = name 
#         self.name = house

# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")

# def get_student():
#     # student = Student()
#     # student.name = input("Name: ")
#     # student.house = input("House: ")
#     # return student

#     # same as above - storing two variables inside of the Student class variable 'student'
#     name = input("Name: ")
#     house = input("House: ")
#     student = Student(name, house)
#     return student

# if __name__ == "__main__":
#     main()




# ---------------------------------------



# learning class'es
class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Griff", "Huff", "Raven", "Slyth"]:
            raise ValueError("Invalid house")
        self.name = name 
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐎"
            case "Otter":
                return "🦦"
            case "Jack":
                return "🐶"
            case _:
                return "👉"

def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()



