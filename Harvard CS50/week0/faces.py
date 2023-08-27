
def main():
    user_input = input()
    smily_faces_replaced = user_input.replace(":)", "🙂")
    smily_faces_replaced = smily_faces_replaced.replace(":(", "🙁")  # Use the already replaced string
    print(smily_faces_replaced)

main()