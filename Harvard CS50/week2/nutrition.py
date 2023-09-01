
fruits ={
    'apple:': 130,
    'avocado': 50,
    'banana': 110,
    'apple:': 130,
    'cantaloupe': 50,
    'grapefruit': 60,
    'grapes:': 90,
    'honeydew melon': 50,
    'kiwifruit': 90,
    'lemon:': 15,
    'lime': 20,
    'nectarine': 60,
    'orange:': 80,
    'Pear': 100,
    'plums': 70,
    'strawberries:': 50,
    'sweet Cherries': 100,
    'tangerine': 50,
    'Watermelon:': 80
    }


def main():
    user_input_fruit = input("Input: ")
    print("Calories: " + str(fruits[user_input_fruit]))


main()



