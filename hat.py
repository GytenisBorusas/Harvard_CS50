

# import random

# class Hat:
#     def __init__(self):
#         self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

#     def sort(self, name):
#         print(name, "is in", random.choice(self.houses))

# hat = Hat()
# hat.sort("Harry")

# def main():
#     ...

# if __name__ == "__main__":
#     main()

# ---------------------------------------------------------------------------





import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry")


# if __name__ == "__main__":
#     main()


    

# ---------------------------------------------------------------------------

